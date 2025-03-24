import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

#Upload csv file
file_path = 'Guia04\\BigMacIndex.csv'
data = pd.read_csv(file_path, delimiter=';')

#Encontrar promedio
#iloc es una función que indexa filas y columnas
#iloc[fila, columna] | : significa todas las filas
#se eliminan errores y se dropean los valores NaN
data['Big Mac Index 2024'] = (data['Big Mac Index 2024'].str.replace(',', '.') .str.strip())
data['Difference from US'] = (data['Difference from US'].str.replace(',', '.').str.strip())
bigMcIndexValues = data['Big Mac Index 2024']

#Convierto los strings a numeros
data['Big Mac Index 2024'] = pd.to_numeric(data['Big Mac Index 2024'], errors='coerce') 
data['Difference from US'] = pd.to_numeric(data['Difference from US'], errors='coerce') 

bigMcIndexValues = data['Big Mac Index 2024']
#Promedio de precios
average = bigMcIndexValues.mean()
print(f"El promedio del índice BigMc es: ${round(average,2)}")

#Valor medio de la muestra = valor medio del array = mediana
#from pd to numpy array
#order numpy array from lowest to highest
median = bigMcIndexValues.median()
print(f"La mediana del índice BigMc es: ${median}")

#Observación de valores atípicos
#Método IQR (intercuartil)
q1 = np.percentile(bigMcIndexValues, 25)
q4 = np.percentile(bigMcIndexValues, 75)
iqr = q4 - q1
inferiorLimit = q1 - 1.5*iqr
superiorLimit = q4 + 1.5*iqr
outliers = bigMcIndexValues[(bigMcIndexValues < inferiorLimit) | (bigMcIndexValues > superiorLimit)]

#Moda. Valor más común
# https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.mode.html
mode = stats.mode(bigMcIndexValues, keepdims=True)
print(f"El precio más común del Big Mac es: {mode.mode[0]} (aparece {mode.count[0]} veces)")

# Desviación estándar y rango
deviation = np.std(bigMcIndexValues)
rango = np.max(bigMcIndexValues) - np.min(bigMcIndexValues)
print(f"La desviación estándar es: {deviation}")
print(f"   El rango es: {rango}")

#Histograma
plt.figure(figsize=(10,6))
plt.hist(bigMcIndexValues, bins=10, color='lightblue', edgecolor='black')
plt.axvline(average, color='red', linestyle='--', label=f'Media: {average:.2f}')
plt.axvline(median, color='green', linestyle=':', label=f'Mediana: {median:.2f}')
plt.title('Distribución del Índice Big Mac 2024')
plt.xlabel('Precio (USD)')
plt.ylabel('Frecuencia')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()