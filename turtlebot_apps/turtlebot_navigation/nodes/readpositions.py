# Import pandas
import pandas as pd

# Assign spreadsheet filename to `file`
file = '/home/warehouse/Documents/Archivos_para_pedidos/coordenadaspuntos.xlsx'

# Load spreadsheet
xl = pd.ExcelFile(file)

# Print the sheet names
print(xl.sheet_names)

# Load a sheet into a DataFrame by name: df

df = pd.read_excel(xl,  'Coordenadas puntos')

print(df.ix[10, 'Punto #'])
print(df.ix[10, 'x'])
print(df.ix[10, 'y'])

point=10
position=[df.ix[point, 'x'], df.ix[point, 'y']]
print(position)