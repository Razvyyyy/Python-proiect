import pandas as pd
import numpy as np




# lista = [10,20,30,40,50]
# serie = pd.Series(lista)
# # print(serie)
# array_date = np.array([10, 20, 30, 40, 50])
# serie = pd.Series(array_date)
# print(serie)
# dict_date = {'a':10, 'b':20, 'c':30, 'd':40, 'e':50}
# serie = pd.Series(dict_date)
# print(serie)




data = {'Nume': ['Ana', 'Bogdan', 'Cristina'],
        'Varsta': [25, 30, 22],
        'Salariu': [50000, 60000, 45000]}
df = pd.DataFrame(data)
df['Experienta'] = [2,5,1]
# print(df)
# df.set_index('Name',inplace=True)
# # print(df)
# print(df.loc['Bogdan'])
df.to_csv('nou.csv')