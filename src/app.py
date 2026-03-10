from pathlib import Path
import pandas as pd
import streamlit as st

BASE_DIR = Path(__file__).resolve().parent.parent
CURATED_PATH = BASE_DIR / "data" / "curated"
OUTPUTS_PATH = BASE_DIR / "outputs"

st.set_page_config(page_title="Cosmetic R&D AI", layout="wide")

st.title("Cosmetic R&D AI on AWS")
st.write("Mini projeto para integração de dados e machine learning aplicado a P&D cosmético.")

dataset_file = CURATED_PATH / "cosmetic_rd_dataset.csv"
metrics_file = OUTPUTS_PATH / "metrics.txt"
pred_file = OUTPUTS_PATH / "predictions.csv"

st.write("Base directory:", BASE_DIR)
st.write("Dataset exists:", dataset_file.exists())
st.write("Metrics exists:", metrics_file.exists())
st.write("Predictions exists:", pred_file.exists())

if dataset_file.exists():
    df = pd.read_csv(dataset_file)

    st.subheader("Dataset Curado")
    st.dataframe(df)

    st.subheader("Resumo Estatístico")
    st.dataframe(df.describe(include="all"))
else:
    st.error("Arquivo cosmetic_rd_dataset.csv não encontrado em data/curated.")
    st.stop()

if metrics_file.exists():
    with open(metrics_file, "r", encoding="utf-8") as f:
        st.subheader("Métrica do Modelo")
        st.text(f.read())

if pred_file.exists():
    preds = pd.read_csv(pred_file)
    st.subheader("Predições")
    st.dataframe(preds)