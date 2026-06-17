# Reproducibility Details

## Environment

- Python 3.12
- Conda environment specified in `environment/environment.yml`
- Key packages: geopandas, libpysal, esda, spreg, statsmodels, pyarrow

## Data

- Source: Inside Airbnb (https://insideairbnb.com/)
- City: Milan, Lombardy, Italy
- Snapshot date: 22 September 2025
- Files: listings.csv, calendar.csv, reviews.csv, neighbourhoods.geojson, listings_summary.csv, reviews_summary.csv

## CRS Policy

| Purpose | CRS | EPSG Code | Rationale |
|---|---|---|---|
| Web/display output | WGS 84 | EPSG:4326 | Standard for web maps, GeoJSON |
| Metric computations | UTM Zone 32N | EPSG:32632 | Accurate projected CRS for Northern Italy |

**Rule**: Never use EPSG:4326 for metric operations (distance, area, weights). Always reproject to EPSG:32632 first.

## Spatial Weight Matrix

| Context | Weight Type | Parameters |
|---|---|---|
| Listing-level analysis | k-Nearest Neighbors | k=8, row-standardized |
| Neighbourhood-level | Queen contiguity | Row-standardized |

## CBD Reference Point

- Location: Piazza del Duomo, Milan
- Coordinates: 45.4642, 9.1900 (WGS 84)
- Used for `dist_cbd_km` covariate (Haversine distance)

## Sample Flow

| Stage | Description |
|---|---|
| 0 | Raw listings from Inside Airbnb |
| 1 | Price parsing and validation |
| 2 | Winsorization (0.5%-99.5%) |
| 3 | Complete covariates (dropna) |

## Pipeline Order

1. `notebooks/01_data_pipeline.ipynb` (ETL)
2. `scripts/01_verify_spatial_data.py` (verification)
3. `scripts/02_make_static_map_overview.py` (maps)
4. `scripts/03_ols_price_analysis.py` (OLS models)
5. `scripts/04_spatial_autocorr_morans_i.py` (Moran's I)
6. `scripts/05_lm_diagnostic_tests.py` (LM diagnostics)
7. `scripts/07_spatial_models_sar_sem.py` (SAR/SEM)
8. `scripts/07b_extract_residuals.py` (residuals)
9. `scripts/08_prepare_map_layers.py` (map layers)
10. `scripts/09_compute_spatial_effects.py` (spatial effects)

## Random Seed

All random operations use `RANDOM_SEED = 42` for reproducibility.
