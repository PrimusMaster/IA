from pandas import * 

#Se abre el archivo de excel para el entrenamiento
data = read_csv("train.csv")
 
#Convierte cada columna del excel en una lista para poder revisar cada dato
pl = data['petallength'].tolist()
pw = data['petalwidth'].tolist()
fc = data['class'].tolist()
 
#Imprime la informacion de las listas
#print('petallength:', pl)
#print('\npetalwith:', pw)
#print('\nclass:', fc)

#Para guardar cada limite de las plantas
minplis = 100
maxplis= -1
minpwis = 100
maxpwis = -1

minpliv = 100
maxpliv= -1
minpwiv = 100
maxpwiv = -1

minplvir = 100
maxplvir = -1
minpwvir = 100
maxpwvir = -1

#Revisa cada planta para conseguir un limite inferior y superior
for x in range(len(fc)):
    if fc[x] == 'Iris-setosa':
        if pl[x] < minplis:
            minplis = pl[x]
        if pl[x] > maxplis:
            maxplis = pl[x]
            
        if pw[x] < minpwis:
            minpwis = pw[x]
        if pw[x] > maxpwis:
            maxpwis = pw[x]
            
    if fc[x] == 'Iris-versicolor':
        if pl[x] < minpliv:
            minpliv = pl[x]
        if pl[x] > maxpliv:
            maxpliv = pl[x]
            
        if pw[x] < minpwiv:
            minpwiv = pw[x]
        if pw[x] > maxpwiv:
            maxpwiv = pw[x]    

    if fc[x] == 'Iris-virginica':
        if (pl[x] < minplvir) and (pl[x] > maxpliv): #Tambien se revisa que sea mayor que el versicolor
            minplvir = pl[x]
        if pl[x] > maxplvir:
            maxplvir = pl[x]
            
        if pw[x] < minpwvir and (pw[x] > maxpwiv): #Tambien se revisa que sea mayor que el versicolor
            minpwvir = pw[x]
        if pw[x] > maxpwvir:
            maxpwvir = pw[x]
            
#print("minplis = ", minplis ," maxplis = ", maxplis)
#print("\nminpliv = ", minpliv ," maxpliv = ", maxpliv)
#print("\nminplvir = ", minplvir ," maxplvir = ", maxplvir)

#print("\n\nminpwis = ", minpwis ," maxpwis = ", maxpwis)
#print("\nminpwiv = ", minpwiv ," maxpwiv = ", maxpwiv)
#print("\nminpwvir = ", minpwvir ," maxpwvir = ", maxpwvir)


#Abre el archivo de test
dataTest = read_csv("test.csv")
 
#Convierte las columnas a listas
plt = dataTest['petallength'].tolist()
pwt = dataTest['petalwidth'].tolist()
fct = dataTest['class'].tolist()

#Se guarda cada fila de caracteristicas a un conjunto
Cis = []
Civ = []
Cvir = []

#Imprime la informacion de las listas
#print('petallength:', plt)
#print('\npetalwith:', pwt)
#print('\nclass:', fct)

#Se revisa por fila para ver a que conjunto pertenece
for x in range(len(plt)):
    #comprobar si es iris setosa
    if (plt[x] >= minplis) and (plt[x] <= maxplis) and (plt[x] >= minpwis) and (pwt[x] <= maxpwis):
         Cis.append(x)
    #comprobar si es iris versicolor
    if (plt[x] >= minpliv) and (plt[x] <= maxpliv) and (plt[x] >= minpwiv) and (pwt[x] <= maxpwiv):
         Civ.append(x)
    #comprobar si es iris virginica
    if (plt[x] >= minplvir) and (plt[x] <= maxplvir) and (plt[x] >= minpwvir): #No se comprueba el limite mayor ya que son las mas grandes
         Cvir.append(x)
         
#Se imprimen los resultados
print("\nIris setosa: ", Cis)
print("\nIris versicolor: ", Civ)
print("\nIris virginica: ", Cvir ,"\n")
