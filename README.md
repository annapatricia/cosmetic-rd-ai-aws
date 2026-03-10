# Cosmetic R&D AI on AWS

Mini projeto demonstrativo para integração de dados aplicados à área de Pesquisa e Desenvolvimento de uma indústria cosmética.

## Objetivo

Construir uma solução de dados e inteligência artificial para:

- integrar dados de ingredientes, formulações e testes;
- organizar dados em camadas;
- treinar um modelo simples de machine learning;
- demonstrar como essa arquitetura poderia ser implementada na AWS.

## Caso de uso

O projeto simula um cenário de P&D cosmético em que dados laboratoriais e analíticos são usados para apoiar o desenvolvimento de novos ingredientes, produtos e serviços.

## Arquitetura proposta

- **Amazon S3** como data lake para armazenamento em camadas
- **AWS Glue** para catálogo e ETL
- **Amazon Athena** para consultas analíticas
- **Amazon SageMaker** para treinamento de modelos
- **Amazon Bedrock** para base de conhecimento com documentos técnicos
- **Dashboard/App** para consumo dos resultados

## Fluxo da solução

```text
Raw Data (CSV / JSON / PDFs)
        |
        v
Amazon S3 (Raw Layer)
        |
        v
AWS Glue (ETL / Catalog)
        |
        v
Trusted / Curated Data
        |
   +----+------------------+
   |                       |
   v                       v
Athena                 Bedrock / RAG
   |                       |
   +----------+------------+
              |
              v
         SageMaker
              |
              v
      Dashboard / Data App
```

## Estrutura do projeto

cosmetic-rd-ai-aws/
│
├── data/
│   ├── raw/
│   ├── trusted/
│   └── curated/
│
├── docs/
│   └── architecture.txt
│
├── notebooks/
├── outputs/
├── src/
│   ├── ingest_data.py
│   ├── transform_data.py
│   ├── train_model.py
│   └── app.py
│
├── requirements.txt
├── README.md
└── .gitignore

## Scripts

```text
src/ingest_data.py    -> leitura dos dados 
src/transform_data.py -> limpeza e integração
src/train_model.py    -> treinamento do modelo
src/app.py            -> interface simples com Streamlit
```
## Como executar

python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
python src/ingest_data.py
python src/transform_data.py
python src/train_model.py
python -m streamlit run src\app.py

## Exemplo de produto de dados

O projeto gera um dataset curado e um modelo simples para prever o final_score de formulações com base em variáveis como:
```text
concentração
pH
viscosidade
temperatura
custo
solubilidade
estabilidade
```
## Resultados gerados

```text
data/curated/cosmetic_rd_dataset.csv
outputs/predictions.csv
outputs/metrics.txt
```


## Próximos passos

```text
adicionar documentos técnicos em PDF
integrar busca semântica com Bedrock
armazenar dados em S3 real
consultar datasets com Athena
empacotar treinamento no SageMaker
```
