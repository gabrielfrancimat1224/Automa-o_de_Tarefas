import pyautogui
import pyperclip
import time
import pandas as pd

pyautogui.PAUSE = 1

# Passo 1: Entrar no sistema da empresa (pelo link)
pyautogui.press('win')
pyautogui.write('opera')
pyautogui.press('enter')
pyperclip.copy("https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga")
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')

time.sleep(5)

# Passo 2: Navegar até o local do relatório (pasta exportar)
pyautogui.click(x=459, y=317, clicks=3)
time.sleep(2)

# Passo 3: Exportar o relatório (baixar base de dados)
pyautogui.click(x=465, y=409)
pyautogui.click(x=1663, y=186)
pyautogui.click(x=1376, y=684)
time.sleep(4)

# Passo 4: Calcular os indicadores (faturamento)
tabela = pd.read_excel(r"C:\Users\GABRIEL\Downloads\Vendas - Dez.xlsx")
print(tabela)

fatura = tabela["Valor Final"].sum()
qntd = tabela["Quantidade"].sum()

# Passo 5: Enviar email para a diretoria
pyautogui.hotkey("ctrl", "t")
pyperclip.copy("https://mail.google.com/mail/u/0/#inbox")
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")

time.sleep(4)

pyautogui.click(x=75, y=153)
pyautogui.write("ffrancimat@gmail.com")
pyautogui.press("tab")
pyautogui.press("tab")
pyperclip.copy("Relatório de Vendas")
pyautogui.hotkey("ctrl", "v")
pyautogui.press("tab")

texto = f"""
Prezados, bom dia

O faturamento de ontem foi de: R${fatura:,.2f}
A quantidade de produtos foi de: {qntd:,}

Abs
Franciss
"""

pyperclip.copy(texto)
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("ctrl", "enter")

