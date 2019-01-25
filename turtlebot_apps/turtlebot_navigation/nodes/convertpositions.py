import pandas as pd

# Assign spreadsheet filename to `file`
file = '/home/warehouse/Documents/Archivos_para_pedidos/coordenadaspuntos.xlsx'

# Load spreadsheet
xl = pd.ExcelFile(file)

# Print the sheet names
print(xl.sheet_names)

# Load a sheet into a DataFrame by name: df

df = pd.read_excel(xl,  'Coordenadas puntos')

#point=10
#position=[df.ix[point, 'x'], df.ix[point, 'y']]

# Assign spreadsheet filename to `file`
route = '/home/warehouse/Documents/Archivos_para_pedidos/Ruta1.xlsx'

# Load spreadsheet
xlroute = pd.ExcelFile(route)

# Load a sheet into a DataFrame by name: df

dfroute = pd.read_excel(xlroute,  'Ruta1')


posiciones=[]
for i in range(len(dfroute)):
    if dfroute.ix[i, 'Accion']!=0:
        posiciones.append(dfroute.ix[i, 'Punto'])

print(posiciones)

locations=dict()

#locations['computador'] = Pose(Point(1.288, 0.094, 0.000), Quaternion(0.000, 0.000, 0.707, 0.707))
for point in posiciones:
   # locations[point]= Pose(Point(df.ix[point, 'x'], df.ix[point, 'y'], 0.000), Quaternion(0.000, 0.000, 0.707, 0.707))
    locations[point]= [df.ix[point, 'x'], df.ix[point, 'y']]
print(locations)    