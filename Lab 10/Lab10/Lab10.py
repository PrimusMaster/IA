from sklearn.neighbors import KNeighborsClassifier 
from sklearn.model_selection import train_test_split 
from sklearn.model_selection import KFold
from sklearn.datasets import load_iris 
import numpy as np
import pandas as pd
#import xlsxwriter
from sklearn.model_selection import cross_val_score
  
###############################################Iris plant
                                                                    #Se obtiene el data set 
irisData = load_iris() 
                                                                    #Se crean los arrays a usar
X = irisData.data 
y = irisData.target 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state=42) # Divide en training y test set (hold out 70/30)
knn = KNeighborsClassifier(n_neighbors=7) 
knn.fit(X_train, y_train) 
print("Iris, Certeza del hold out: ",knn.score(X_test, y_test))     # Se calcula el porcentaje de aciertos, de 0 a 1, siendo 1 el 100%

                                                                    ## arrays for 10-fold
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1, stratify=y)
knn = KNeighborsClassifier(n_neighbors = 3)                         #Se crea el clasificador KNN
cv_scores = cross_val_score(knn, X, y, cv=10)                       #Se entrena el modelo
print("Iris, Certeza del K-fold: ",np.mean(cv_scores),"\n\n")


##################################################  coffe
coffee = pd.read_csv("Coffee.csv")
#print(coffee.head())
#print(coffee.shape)

X = coffee.drop(columns=['Cups of coffee consumed'])                #Se guarda una copia con una columna menos, esta es la que sera calculada
#print(X.head())

y = coffee['Cups of coffee consumed'].values                        #Se obtienen los valores de la columna que se quito
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1, stratify=y) #Se divide el dataset
knn = KNeighborsClassifier(n_neighbors=7) 
knn.fit(X_train, y_train)
print("Coffee, Certeza del hold out: ",knn.score(X_test, y_test))

                                                                    ## arrays for 10-fold
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1, stratify=y)
knn = KNeighborsClassifier(n_neighbors = 3)                         #Se crea el clasificador KNN
cv_scores = cross_val_score(knn, X, y, cv=10)                       #Se entrena el modelo
print("Coffee, Certeza del K-fold: ",np.mean(cv_scores))
