from sklearn.neighbors import KNeighborsClassifier 
from sklearn.model_selection import train_test_split 
from sklearn.model_selection import KFold
from sklearn.datasets import load_iris 
import numpy as np

  
###############################################Iris plant
# Loading data 
irisData = load_iris() 
# Create feature and target arrays 
X = irisData.data 
y = irisData.target 
# Split into training and test set (hold out 70/30)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state=42) 
knn = KNeighborsClassifier(n_neighbors=7) 
knn.fit(X_train, y_train) 
# Se calcula el porcentaje de aciertos, de 0 a 1, siendo 1 el 100%
print("Certeza del hold out: ",knn.score(X_test, y_test))

## arrays for 10-fold
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1, stratify=y)
# Create KNN classifier
knn = KNeighborsClassifier(n_neighbors = 3)
# Fit the classifier to the data
knn.fit(X_train,y_train)
print("Certeza del K-fold: ",knn.score(X_test, y_test))
