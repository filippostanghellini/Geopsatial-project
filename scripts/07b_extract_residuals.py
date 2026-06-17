import sys
from pathlib import Path

project_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(project_root))

import pandas as pd

from src.config import OUTPUT_FILES
from src.io import save_csv


def main():
    print("=" * 60)
    print("EXTRACT RESIDUALS FOR MAP")
    print("=" * 60)

    residuals_path = OUTPUT_FILES['residuals_for_map']
    if residuals_path.exists():
        residuals_df = pd.read_csv(residuals_path)
        print(f"Residuals loaded from script 07: {len(residuals_df)} listings")
    else:
        print("WARNING: residuals_for_map.csv not found.")
        print("Run scripts/07_spatial_models_sar_sem.py first.")
        return

    print(f"Residuals available: {len(residuals_df)} listings")
    print(f"  OLS residuals: mean={residuals_df['ols_residual'].mean():.6f}, std={residuals_df['ols_residual'].std():.4f}")
    if 'sar_residual' in residuals_df.columns and residuals_df['sar_residual'].notna().any():
        print(f"  SAR residuals: mean={residuals_df['sar_residual'].mean():.6f}, std={residuals_df['sar_residual'].std():.4f}")
    if 'sem_residual' in residuals_df.columns and residuals_df['sem_residual'].notna().any():
        print(f"  SEM residuals: mean={residuals_df['sem_residual'].mean():.6f}, std={residuals_df['sem_residual'].std():.4f}")

    print("\n" + "=" * 60)


if __name__ == "__main__":
    main()
