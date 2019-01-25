# Import pandas
import pandas as pd

# Assign spreadsheet filename to `file`
file = '/home/warehouse/Documents/Archivos_para_pedidos/Ruta1.xlsx'

# Load spreadsheet
xl = pd.ExcelFile(file)

# Print the sheet names
print(xl.sheet_names)

# Load a sheet into a DataFrame by name: df

df = pd.read_excel(xl,  'Ruta1')

print(df.ix[15, 'Punto'])
print(df.ix[15, 'Accion'])
print(df.ix[15, 'Pedido'])

posiciones=[]
for i in range(len(df)):
    if df.ix[i, 'Accion']!=0:
        print(df.ix[i, 'Punto'])
        posiciones.append(df.ix[i, 'Punto'])

print(posiciones)


#point=10
#position=[df.ix[point, 'x'], df.ix[point, 'y']]
#print(position)

#data = pd.read_csv(file, encoding='utf-8', sep=" ", header=None)
#data.columns = ["Punto", "Accion",	"Pedido",	"Referencia",	"Cantidad",	"Posicion",	"Codigo Mensaje",	"Posicion del carro",	"Cantidad confirmada"]

#print(data.ix[15, 'Punto'])

#print(df.ix[10, 'x'])
#print(df.ix[10, 'y'])

#point=10
#position=[df.ix[point, 'x'], df.ix[point, 'y']]
#print(position)