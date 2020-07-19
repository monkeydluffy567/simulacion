import pandas as pd
df = pd.read_excel('C:\\Users\\gabrielfather\\Documents\\Proyectos\\python\\Cursos\\curso de simulacion\\practica_simulacion\\prueba.xlsx')
print(df)
estadisticas =df.describe()
print(estadisticas)