"""
healthcare_pipeline.py
End-to-end pipeline: extract -> clean -> integrate -> analyse -> export.

Project: Which factors explain differences in national life expectancy? (2000-2015)
Author : Priya Kailas Rakshe

HOW TO RUN (Google Colab or local):
    pip install pandas numpy requests pycountry statsmodels scikit-learn scipy seaborn matplotlib
    # put "Life Expectancy Data.csv" (Kaggle: Life Expectancy WHO) in data/raw/
    python healthcare_pipeline.py

OUTPUTS:
    data/processed/health_integrated.csv   (analysis-ready dataset)
    reports/results_summary.csv            (numbers to copy into the Week 4 report)
    reports/figures/*.png                  (charts)
    docs/profiling_report.csv              (missing values etc.)
"""
import os
import sys
import warnings

import numpy as np
import pandas as pd
import requests

warnings.filterwarnings("ignore")

RAW_CSV = "data/raw/Life Expectancy Data.csv"
for d in ["data/raw", "data/interim", "data/processed", "reports/figures", "docs"]:
    os.makedirs(d, exist_ok=True)

WB_INDICATORS = {
    "SH.XPD.CHEX.PC.CD": "health_exp_pc",
    "SH.MED.PHYS.ZS": "physicians_per_1000",
    "SH.MED.BEDS.ZS": "beds_per_1000",
    "SP.POP.65UP.TO.ZS": "pop_65plus",
    "NY.GDP.PCAP.CD": "gdp_pc",
    "SP.POP.TOTL": "population_wb",
}

# names pycountry cannot resolve automatically (WHO style -> ISO3)
MANUAL_ISO3 = {
    "Bolivia (Plurinational State of)": "BOL", "Cote d'Ivoire": "CIV", "Côte d'Ivoire": "CIV",
    "Democratic People's Republic of Korea": "PRK", "Democratic Republic of the Congo": "COD",
    "Iran (Islamic Republic of)": "IRN", "Lao People's Democratic Republic": "LAO",
    "Micronesia (Federated States of)": "FSM", "Republic of Korea": "KOR",
    "Republic of Moldova": "MDA", "Russian Federation": "RUS", "Syrian Arab Republic": "SYR",
    "The former Yugoslav republic of Macedonia": "MKD", "United Kingdom of Great Britain and Northern Ireland": "GBR",
    "United Republic of Tanzania": "TZA", "United States of America": "USA",
    "Venezuela (Bolivarian Republic of)": "VEN", "Viet Nam": "VNM", "Turkey": "TUR",
    "Congo": "COG", "Gambia": "GMB", "Bahamas": "BHS", "Egypt": "EGY", "Yemen": "YEM",
    "Kyrgyzstan": "KGZ", "Slovakia": "SVK", "Brunei Darussalam": "BRN", "Cabo Verde": "CPV",
    "Czechia": "CZE", "Swaziland": "SWZ", "Saint Kitts and Nevis": "KNA", "Saint Lucia": "LCA",
    "Saint Vincent and the Grenadines": "VCT", "Sao Tome and Principe": "STP",
    "Timor-Leste": "TLS", "Netherlands": "NLD", "Niue": "NIU", "Cook Islands": "COK",
}


# ------------------------------------------------------------------ 1. EXTRACT
def load_primary(path=RAW_CSV):
    df = pd.read_csv(path)
    df.columns = (df.columns.str.strip().str.lower()
                  .str.replace(r"[^a-z0-9]+", "_", regex=True).str.strip("_"))
    df = df.rename(columns={"hiv_aids": "hiv_aids", "thinness_1_19_years": "thinness_1_19",
                            "thinness_5_9_years": "thinness_5_9"})
    print("Primary dataset shape:", df.shape)
    return df


def fetch_worldbank(indicator, name, start=2000, end=2015):
    url = (f"https://api.worldbank.org/v2/country/all/indicator/{indicator}"
           f"?format=json&per_page=20000&date={start}:{end}")
    r = requests.get(url, timeout=90)
    r.raise_for_status()
    js = r.json()
    if len(js) < 2 or not js[1]:
        print(f"  WARNING: no data returned for {indicator}: {js[0] if js else 'empty response'}")
        return pd.DataFrame(columns=["iso3", "year", name])
    rows = js[1]
    out = pd.DataFrame([{"iso3": x["countryiso3code"], "year": int(x["date"]), name: x["value"]}
                        for x in rows if x["countryiso3code"]])
    return out


def extract_worldbank():
    cache = "data/interim/worldbank_all.csv"
    if os.path.exists(cache):
        return pd.read_csv(cache)
    merged = None
    for code, name in WB_INDICATORS.items():
        print("Fetching", code)
        t = fetch_worldbank(code, name)
        if t.empty:
            continue                      # skip an indicator that failed instead of crashing
        merged = t if merged is None else merged.merge(t, on=["iso3", "year"], how="outer")
    merged.to_csv(cache, index=False)
    return merged


# ------------------------------------------------------------------ 2. PROFILE
def profile(df, tag):
    rep = pd.DataFrame({"dtype": df.dtypes.astype(str), "missing": df.isna().sum(),
                        "missing_pct": (df.isna().mean() * 100).round(1), "n_unique": df.nunique()})
    rep.to_csv(f"docs/profiling_report_{tag}.csv")
    print(f"[{tag}] rows={len(df)}, exact duplicates={df.duplicated().sum()}")
    return rep


# ------------------------------------------------------------------ 3. CLEAN
def add_iso3(df):
    try:
        import pycountry
    except ImportError:
        sys.exit("pip install pycountry")

    def lookup(name):
        if name in MANUAL_ISO3:
            return MANUAL_ISO3[name]
        try:
            return pycountry.countries.lookup(name).alpha_3
        except LookupError:
            return np.nan
    names = df["country"].unique()
    cw = pd.DataFrame({"country": names, "iso3": [lookup(n) for n in names]})
    cw.to_csv("data/interim/country_crosswalk.csv", index=False)
    unmatched = cw[cw["iso3"].isna()]["country"].tolist()
    if unmatched:
        print("ADD THESE TO MANUAL_ISO3:", unmatched)
    return df.merge(cw, on="country", how="left")


def clean_primary(df):
    df = df.copy()
    df["country"] = df["country"].str.strip()
    df = df.drop_duplicates()
    assert not df.duplicated(["country", "year"]).any(), "duplicate country-year keys"
    # impossible values -> missing
    if "bmi" in df:
        df.loc[(df["bmi"] < 10) | (df["bmi"] > 60), "bmi"] = np.nan
    if "percentage_expenditure" in df:
        df["pct_exp_flag"] = (df["percentage_expenditure"] > 100).astype(int)
    # drop rows with missing outcome or key predictor
    df = df.dropna(subset=["life_expectancy", "adult_mortality"])
    df = df.sort_values(["country", "year"])
    # impute: within-country interpolation, then status-year median
    num = ["hepatitis_b", "total_expenditure", "alcohol", "schooling", "income_composition_of_resources",
           "bmi", "polio", "diphtheria", "thinness_1_19", "thinness_5_9", "gdp", "population"]
    for col in [c for c in num if c in df.columns]:
        df[col + "_imputed"] = df[col].isna().astype(int)
        df[col] = df.groupby("country")[col].transform(lambda s: s.interpolate(limit_direction="both"))
        df[col] = df[col].fillna(df.groupby(["status", "year"])[col].transform("median"))
    return df


# ------------------------------------------------------------------ 4. INTEGRATE
def integrate(df1, wb):
    wb = wb[wb["iso3"].isin(df1["iso3"].dropna().unique())]          # drops aggregates
    assert not wb.duplicated(["iso3", "year"]).any()
    m = df1.merge(wb, on=["iso3", "year"], how="left", validate="many_to_one")
    assert len(m) == len(df1), "rows changed during join"
    match = m["gdp_pc"].notna().mean() if "gdp_pc" in m else np.nan
    print(f"World Bank match rate: {match:.1%}")
    # prefer World Bank GDP and population; keep originals with _d1 suffix
    m["gdp_d1"], m["population_d1"] = m.get("gdp"), m.get("population")
    m["population"] = m["population_wb"].fillna(m["population"])
    m["log_gdp_pc"] = np.log(m["gdp_pc"].fillna(m["gdp"]).clip(lower=1))
    m["health_exp_share"] = m["health_exp_pc"] / m["gdp_pc"]
    m["status_code"] = (m["status"] == "Developed").astype(int)
    m["period"] = pd.cut(m["year"], [1999, 2005, 2010, 2015], labels=["2000-05", "2006-10", "2011-15"])
    m.to_csv("data/processed/health_integrated.csv", index=False)
    print("Integrated dataset:", m.shape)
    return m


# ------------------------------------------------------------------ 5. ANALYSE
def analyse(m):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    import seaborn as sns
    import statsmodels.api as sm
    from scipy import stats
    from sklearn.cluster import KMeans
    from sklearn.decomposition import PCA
    from sklearn.ensemble import RandomForestRegressor
    from sklearn.metrics import mean_squared_error, r2_score, silhouette_score
    from sklearn.model_selection import train_test_split
    from sklearn.preprocessing import StandardScaler
    from statsmodels.stats.outliers_influence import variance_inflation_factor

    R = {}   # results dictionary

    # ---- RQ1 trend and group comparison
    t = m.groupby(["year", "status"])["life_expectancy"].mean().unstack()
    for g in t.columns:
        R[f"le_2000_{g}"] = round(t.loc[2000, g], 1)
        R[f"le_2015_{g}"] = round(t.loc[2015, g], 1)
        R[f"gain_{g}"] = round(t.loc[2015, g] - t.loc[2000, g], 1)
        R[f"cagr_pct_{g}"] = round(((t.loc[2015, g] / t.loc[2000, g]) ** (1 / 15) - 1) * 100, 2)
    R["le_2000_all"] = round(m[m.year == 2000]["life_expectancy"].mean(), 1)
    R["le_2015_all"] = round(m[m.year == 2015]["life_expectancy"].mean(), 1)
    a = m[(m.year == 2015) & (m.status == "Developed")]["life_expectancy"]
    b = m[(m.year == 2015) & (m.status == "Developing")]["life_expectancy"]
    tt = stats.ttest_ind(a, b, equal_var=False)
    diff = a.mean() - b.mean()
    se = np.sqrt(a.var() / len(a) + b.var() / len(b))
    R["gap_2015_years"] = round(diff, 1)
    R["gap_ttest_p"] = float(f"{tt.pvalue:.3g}")
    R["gap_95ci"] = f"[{diff - 1.96 * se:.1f}, {diff + 1.96 * se:.1f}]"
    fig, ax = plt.subplots(figsize=(7, 4))
    t.plot(ax=ax, marker="o")
    ax.set(title="Life expectancy rose in both groups, developing countries gained faster",
           ylabel="Mean life expectancy (years)", xlabel="Year")
    fig.tight_layout(); fig.savefig("reports/figures/trend_by_status.png", dpi=200); plt.close()

    # ---- RQ2 correlation + OLS
    preds = [c for c in ["adult_mortality", "hiv_aids", "schooling", "income_composition_of_resources",
                         "hepatitis_b", "polio", "diphtheria", "bmi", "log_gdp_pc", "health_exp_pc",
                         "physicians_per_1000"] if c in m.columns]
    d = m[["life_expectancy"] + preds].replace([np.inf, -np.inf], np.nan)
    d = d.fillna(d.median())
    Xz = (d[preds] - d[preds].mean()) / d[preds].std()
    y = d["life_expectancy"]
    Xtr, Xte, ytr, yte = train_test_split(Xz, y, test_size=0.2, random_state=42)
    ols = sm.OLS(ytr, sm.add_constant(Xtr)).fit()
    pred = ols.predict(sm.add_constant(Xte))
    R["ols_test_r2"] = round(r2_score(yte, pred), 2)
    R["ols_test_rmse_years"] = round(mean_squared_error(yte, pred) ** 0.5, 1)
    Xc = sm.add_constant(Xtr)
    vif = {c: round(variance_inflation_factor(Xc.values, i), 1) for i, c in enumerate(Xc.columns) if c != "const"}
    R["max_vif"] = max(vif.values())
    coefs = ols.params.drop("const").sort_values()
    R["strongest_negative"] = f"{coefs.index[0]} (beta={coefs.iloc[0]:.2f})"
    R["strongest_positive"] = f"{coefs.index[-1]} (beta={coefs.iloc[-1]:.2f})"
    ci = ols.conf_int().drop("const").loc[coefs.index]
    fig, ax = plt.subplots(figsize=(7, 4.5))
    ax.barh(coefs.index, coefs.values, xerr=[coefs.values - ci[0].values, ci[1].values - coefs.values],
            color=["#B5483A" if v < 0 else "#2E8B87" for v in coefs.values])
    ax.axvline(0, color="black", lw=0.8)
    ax.set(title="Standardised regression coefficients (95% CI)", xlabel="Years of life expectancy per 1 SD")
    fig.tight_layout(); fig.savefig("reports/figures/ols_coefficients.png", dpi=200); plt.close()
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.heatmap(d.corr(), cmap="vlag", center=0, annot=False, ax=ax)
    ax.set_title("Correlation heat-map")
    fig.tight_layout(); fig.savefig("reports/figures/correlation_heatmap.png", dpi=200); plt.close()

    # ---- random forest check
    rf = RandomForestRegressor(n_estimators=300, random_state=42, n_jobs=-1).fit(Xtr, ytr)
    imp = pd.Series(rf.feature_importances_, index=preds).sort_values(ascending=False)
    R["rf_test_r2"] = round(r2_score(yte, rf.predict(Xte)), 2)
    R["rf_top3"] = ", ".join(imp.index[:3])

    # ---- RQ3 clustering on 2015 (or latest year per country)
    cvars = [c for c in ["life_expectancy", "adult_mortality", "schooling", "polio", "diphtheria",
                         "log_gdp_pc", "health_exp_pc"] if c in m.columns]
    last = m.sort_values("year").groupby("country").tail(1).set_index("country")[cvars]
    last = last.fillna(last.median())
    Z = StandardScaler().fit_transform(last)
    sil = {k: silhouette_score(Z, KMeans(k, n_init=20, random_state=42).fit_predict(Z)) for k in range(2, 8)}
    best_k = 4 if 4 in sil else max(sil, key=sil.get)
    labels = KMeans(best_k, n_init=20, random_state=42).fit_predict(Z)
    R["silhouette_by_k"] = {k: round(v, 2) for k, v in sil.items()}
    R["k_used"] = best_k
    R["silhouette_k_used"] = round(sil[best_k], 2)
    last["cluster"] = labels
    prof = last.groupby("cluster").mean().round(1)
    prof["n_countries"] = last.groupby("cluster").size()
    prof.to_csv("reports/cluster_profiles.csv")
    pcs = PCA(2).fit_transform(Z)
    fig, ax = plt.subplots(figsize=(6.5, 5))
    sc = ax.scatter(pcs[:, 0], pcs[:, 1], c=labels, cmap="viridis", s=30)
    ax.set(title="Country clusters (PCA projection)", xlabel="PC1", ylabel="PC2")
    ax.legend(*sc.legend_elements(), title="Cluster")
    fig.tight_layout(); fig.savefig("reports/figures/clusters_pca.png", dpi=200); plt.close()

    pd.Series(R).to_csv("reports/results_summary.csv", header=["value"])
    print("\n=== RESULTS (copy into Week 4 report) ===")
    for k, v in R.items():
        print(f"{k}: {v}")
    print("\nCluster profiles:\n", prof)
    return R


# ------------------------------------------------------------------ MAIN
if __name__ == "__main__":
    df1 = load_primary()
    profile(df1, "primary_raw")
    wb = extract_worldbank()
    df1 = add_iso3(df1)
    df1 = clean_primary(df1)
    merged = integrate(df1, wb)
    profile(merged, "integrated")
    analyse(merged)
