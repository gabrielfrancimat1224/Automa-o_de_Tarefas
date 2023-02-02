import pandas as pd
import plotly.express as px

# Passo 1: Importar a base de dados
tabela = pd.read_csv("telecom_users.csv")

# Passo 2: Visualizar a base de dados
# axis = 0 -> linha / axis = 1 -> coluna
tabela = tabela.drop("Unnamed: 0", axis=1)
# print(tabela)

# Passo 3: Tratamento de dados
tabela["TotalGasto"] = pd.to_numeric(tabela["TotalGasto"], errors="coerce")
print(tabela.info())

# Excluir colunas com TODOS valores vazios
tabela = tabela.dropna(how="all", axis=1)

# Excluir linhas com pelo menos um valores vazios
tabela = tabela.dropna(how="any", axis=0)

# Passo 4: Análise inicial
print(tabela["Churn"].value_counts())
print(tabela["Churn"].value_counts(normalize=True).map("{:.1%}".format))

# Passo 5: Análise detalhada

# Criar gráfico
for coluna in tabela.columns:
    grafico = px.histogram(tabela, x=coluna, color="Churn", text_auto=True)

    # Exibir gráfico
    grafico.show()
