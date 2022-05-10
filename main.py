import tabula
import pandas as pd

rows = []
lista_tabelas = tabula.read_pdf('vacinacao.pdf', pages='all')
#print(lista_tabelas)
for linha in lista_tabelas:
    df = pd.DataFrame().append(linha)

#print(rows)
#df = pd.DataFrame().append()
df.to_excel('vacinacao.xlsx', index=False)
print(df)