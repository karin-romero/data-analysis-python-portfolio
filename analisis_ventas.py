import pandas as pd

df = pd.read_csv("logs_fex.csv")

errores = df[df['estado'] == 'ERROR']
errores_tipo = errores['tipo_error'].value_counts()

print("Errores por tipo:")
print(errores_tipo)

df['fecha'] = pd.to_datetime(df['fecha'])
errores_por_dia = errores.groupby(df['fecha'].dt.date).size()

print("Errores por día:")
print(errores_por_dia)
