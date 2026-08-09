# 📊 Análise de Dados de RH com Pandas

Este projeto simula uma demanda real do setor de Recursos Humanos (RH), focado na análise da folha de pagamento e perfil demográfico dos colaboradores utilizando a biblioteca **Pandas** no Python.

## 🎯 O Ticket de Negócio (Objetivo)
O script foi desenvolvido para processar uma base de dados corporativa em formato `.csv` e entregar os seguintes indicadores estratégicos:
1. Cálculo dinâmico da idade exata dos funcionários com base na data de nascimento.
2. Filtragem de colaboradores sêniores (acima de 30 anos) para políticas de retenção.
3. Extração de métricas financeiras globais (Custo Total e Média Salarial).
4. Mapeamento de custos salariais agrupados por Departamento.
5. Geração de um ranking salarial ordenado.

## 🛠️ Tecnologias e Conceitos Aplicados
* **Linguagem:** Python
* **Biblioteca:** Pandas
* **Conceitos:**
  * Leitura de arquivos externos (`read_csv`).
  * Manipulação de datas e tempo (`pd.to_datetime`, `pd.Timestamp.now`).
  * Indexação Booleana (Filtros condicionais).
  * Agregações matemáticas (`sum`, `mean`).
  * Agrupamento de dados (`groupby`).
  * Ordenação de DataFrames (`sort_values`).

## 🚀 Como Executar
Certifique-se de ter o Pandas instalado no seu ambiente virtual ou máquina:
`pip install pandas`

No terminal, navegue até a pasta do projeto e execute:
`python 01_pandas_introducao.py`