import pandas as pd

# Reemplaza 'entrada.parquet' con la ruta de tu archivo Parquet
archivo_parquet = 'data/train-00000-of-00001-9ad84bb9cf65a42f.parquet'

# Cargar el archivo Parquet en un DataFrame de Pandas
df = pd.read_parquet(archivo_parquet)

# Reemplaza 'salida.txt' con el nombre que desees para el archivo de texto de salida
archivo_txt = 'data/salida.txt'

# Guardar el DataFrame como un archivo de texto (separado por tabulaciones)
df.to_csv(archivo_txt, sep='\t', index=False)

# Si prefieres un formato diferente, puedes ajustar los parámetros de to_csv según tus necesidades
# Por ejemplo, df.to_csv(archivo_txt, sep=',', index=False) para usar comas como separadores
