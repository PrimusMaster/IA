from pandas import * 

data = read_csv("train.csv")
 
# converting column data to list
pl = data['petallength'].tolist()
pw = data['petalwidth'].tolist()
fc = data['class'].tolist()
 
#Imprime la informacion de las listas
print('petallength:', pl)
print('\npetalwith:', pw)
print('\nclass:', fc)

