from pathlib import Path
import pandas as pd

RAW_PATH = Path("data/raw")
TRUSTED_PATH = Path("data/trusted")
CURATED_PATH = Path("data/curated")

def main():
    TRUSTED_PATH.mkdir(parents=True, exist_ok=True)
    CURATED_PATH.mkdir(parents=True, exist_ok=True)

    ingredients = pd.read_csv(RAW_PATH / "ingredients.csv")
    formulations = pd.read_csv(RAW_PATH / "formulations.csv")

    ingredients.columns = [c.lower().strip() for c in ingredients.columns]
    formulations.columns = [c.lower().strip() for c in formulations.columns]

    ingredients.to_csv(TRUSTED_PATH / "ingredients_clean.csv", index=False)
    formulations.to_csv(TRUSTED_PATH / "formulations_clean.csv", index=False)

    final_df = formulations.merge(ingredients, on="ingredient_id", how="left")
    final_df.to_csv(CURATED_PATH / "cosmetic_rd_dataset.csv", index=False)

    print("Dataset curated created successfully.")
    print(final_df.head())

if __name__ == "__main__":
    main()