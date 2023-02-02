from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd

navegador = webdriver.Chrome()

# Passo 1: Pegar a cotação do dólar
navegador.get("https://www.google.com/")

navegador.find_element("xpath",
                       '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("Cotação dolár")

navegador.find_element("xpath",
                       '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)

cotaçao_dolar = navegador.find_element("xpath",
                                       '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute(
    "data-value")

print(cotaçao_dolar)

# Passo 2: Pegar a cotação do euro
navegador.get("https://www.google.com/")

navegador.find_element("xpath",
                       '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("Cotação euro")

navegador.find_element("xpath",
                       '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)

cotaçao_euro = navegador.find_element("xpath",
                                      '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute(
    "data-value")

print(cotaçao_euro)

# Passo 3: Pegar a cotação do ouro
navegador.get("https://www.melhorcambio.com/ouro-hoje")

cotaçao_ouro = navegador.find_element("xpath", '//*[@id="comercial"]').get_attribute("value")
cotaçao_ouro = cotaçao_ouro.replace(",", ".")

print(cotaçao_ouro)

# Passo 4: Importar a base de dados e atualizar ela
tabela = pd.read_excel("Produtos.xlsx")
print(tabela)

# Passo 5: Recalcular os preços

tabela.loc[tabela["Moeda"] == "Dolár", "Cotação"] = float(cotaçao_dolar)
tabela.loc[tabela["Moeda"] == "Euro", "Cotação"] = float(cotaçao_euro)
tabela.loc[tabela["Moeda"] == "Ouro", "Cotação"] = float(cotaçao_ouro)

tabela["Preço de Compra"] = tabela["Cotação"] * tabela["Preço Original"]

tabela["Preço de Venda"] = tabela["Preço de Compra"] * tabela["Margem"]

# Passo 6: Exportar a base atualizada
tabela.to_excel("Produtos_Novos.xlsx", index=False)
