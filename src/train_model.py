from pathlib import Path
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

CURATED_PATH = Path("data/curated")
OUTPUTS_PATH = Path("outputs")

def main():
    OUTPUTS_PATH.mkdir(parents=True, exist_ok=True)

    df = pd.read_csv(CURATED_PATH / "cosmetic_rd_dataset.csv")

    df["solubility"] = df["solubility"].map({"Low": 0, "Medium": 1, "High": 2})
    df["category"] = df["category"].astype("category").cat.codes
    df["ingredient_name"] = df["ingredient_name"].astype("category").cat.codes

    features = [
        "concentration",
        "test_ph",
        "viscosity",
        "temperature",
        "cost_per_kg",
        "ph",
        "solubility",
        "stability_score",
        "approved",
        "category",
        "ingredient_name",
    ]

    X = df[features]
    y = df["final_score"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42
    )

    model = RandomForestRegressor(random_state=42, n_estimators=100)
    model.fit(X_train, y_train)

    preds = model.predict(X_test)
    mae = mean_absolute_error(y_test, preds)

    result = pd.DataFrame({
        "real": y_test.values,
        "predicted": preds
    })
    result.to_csv(OUTPUTS_PATH / "predictions.csv", index=False)

    with open(OUTPUTS_PATH / "metrics.txt", "w", encoding="utf-8") as f:
        f.write(f"MAE: {mae:.2f}\n")

    print(f"Training complete. MAE: {mae:.2f}")

if __name__ == "__main__":
    main()