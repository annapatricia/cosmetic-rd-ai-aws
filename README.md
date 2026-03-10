# Cosmetic R&D AI on AWS

Mini projeto demonstrativo para integração de dados aplicados à área de Pesquisa e Desenvolvimento de uma indústria cosmética.

## Objetivo

Construir uma solução de dados e inteligência artificial para:

- integrar dados de ingredientes, formulações e testes;
- organizar dados em camadas;
- treinar um modelo simples de machine learning;
- demonstrar como essa arquitetura poderia ser implementada na AWS.

## Arquitetura proposta

- **Amazon S3** como data lake para armazenamento em camadas
- **AWS Glue** para catálogo e ETL
- **Amazon Athena** para consultas analíticas
- **Amazon SageMaker** para treinamento de modelos
- **Amazon Bedrock** para base de conhecimento com documentos técnicos
- **Dashboard/App** para consumo dos resultados

## Estrutura do projeto

```text
data/raw        -> dados brutos
data/trusted    -> dados tratados
data/curated    -> dados prontos para análise
src/            -> scripts do projeto
outputs/        -> métricas e predições
docs/           -> desenho da arquitetura`
```
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
streamlit run src/app.py

## Caso de uso 

O projeto simula uma plataforma corporativa de dados para apoiar o desenvolvimento de novos ingredientes, formulações e produtos cosméticos a partir de dados laboratoriais e analíticos.

## Próximos passos

```text
adicionar documentos técnicos em PDF
integrar busca semântica com Bedrock
armazenar dados em S3 real
consultar datasets com Athena
empacotar treinamento no SageMaker
```
