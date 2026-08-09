# """
# TICKET DE DEMANDA - RECURSOS HUMANOS (NÍVEL ESTÁGIO/JÚNIOR)
# Objetivo: Analisar a folha de pagamento e o perfil demográfico por setor.

# Tarefas solicitadas:
# 1. Calcular a idade exata dos funcionários hoje, baseada na data de nascimento.
# 2. O RH precisa focar em retenção de talentos sêniores. Filtre quem tem mais de 30 anos.
# 3. A diretoria quer saber o impacto financeiro: Qual o custo total e a média salarial da empresa?
# 4. [Análise de Setor] Agrupe os dados para mostrar o custo total de salários por Departamento.
# 5. Identifique quem é o funcionário com o maior salário (ordene a tabela).
# """

import pandas as pd

# ==========================================
# 1. DADOS REAIS DO RH (5 Funcionários)
# ==========================================
print("\n--- 1. Base de Dados Inicial ---")

df_funcionarios = pd.read_csv("funcionarios.csv")

print(df_funcionarios)


# ==========================================
# 2. CALCULAR IDADE COM PANDAS
# ==========================================
print("\n--- 2. Tabela com a Idade dos Funcionarios ---")

df_funcionarios["data_nascimento"] = pd.to_datetime(df_funcionarios["data_nascimento"])

df_funcionarios["idade"] = (pd.Timestamp.now() - df_funcionarios["data_nascimento"]).dt.days // 365

print(df_funcionarios["idade"])


# ==========================================
# 3. FILTROS DE NEGÓCIO
# ==========================================
print("\n--- 3. Funcionários com 30 anos ou mais ---")

print(df_funcionarios[df_funcionarios["idade"] >=30])

# ==========================================
# 4. MÉTRICAS FINANCEIRAS GERAIS
# ==========================================

print("\n--- 4. Resumo Financeiro da Empresa ---")

print(f"Custo Total da Folha: R$ {df_funcionarios['salario'].sum():.2f}")
print(f"Media Salarial: R$ {df_funcionarios['salario'].mean():.2f}")

# ==========================================
# 5. ANÁLISE POR SETOR
# ==========================================

print("\n--- 5. Custo de Salário por Departamento ---")

soma_salario_dp = df_funcionarios.groupby('departamento')['salario'].sum()

print(soma_salario_dp)

# ==========================================
# 6. RANKING SALARIAL
# ==========================================

print("\n--- 6. Ranking de Salários (Maior para o Menor) ---")

ranking_salario = df_funcionarios.sort_values(by='salario',ascending=False)

print(ranking_salario[['nome_completo','salario']])