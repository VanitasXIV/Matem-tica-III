import pandas as pd

#Upload csv file
file_path = 'C:/Users/IvanGomez/Documents/Matem-tica-III/Guia04/BigMacIndex.csv'
data = pd.read_csv(file_path, delimiter=';')

#Data cleanse
#Delete empty columns and rows
data = data.iloc[:,2]
print(data)