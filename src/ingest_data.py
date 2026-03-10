from pathlib import Path
import pandas as pd

RAW_PATH = Path("data/raw")

def main():
    ingredients = pd.read_csv(RAW_PATH / "ingredients.csv")
    formulations = pd.read_csv(RAW_PATH / "formulations.csv")

    print("Ingredients:")
    print(ingredients.head(), "\n")

    print("Formulations:")
    print(formulations.head(), "\n")

if __name__ == "__main__":
    main()