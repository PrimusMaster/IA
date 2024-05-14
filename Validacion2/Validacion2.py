from pandas import * 
import xlsxwriter

#Se abre el archivo de excel para el entrenamiento
dataI = read_excel("Iris.xlsx")


#columnas de cada excel
pl = dataI['petallength'].tolist()
pw = dataI['petalwidth'].tolist()
fc = dataI['class'].tolist()


#Variables donde se guardan cuantos elementos hay de cada clase de los dataset 
setoI = 0
versiI = 0
virI = 0

for x in range(len(fc)):
    if fc[x] == 'Iris-setosa':
        setoI = setoI + 1
            
    if fc[x] == 'Iris-versicolor':
        versiI = versiI + 1  

    if fc[x] == 'Iris-virginica':
        virI = virI + 1
        

#Se hacen los conjuntos de prueba y entrenamiento
#Variables para no superar los limites de cuantos valores van en cada conjunto
setoIF = 1
versiIF = 1
virIF = 1

IrisTestf = 1
IrisTrainf = 1

#Creando o abriendo los archivos y hoja donde se guardaran los conjutos
IrisTrain = xlsxwriter.Workbook('IrisTrain.xlsx')
IrisTrainHoja = IrisTrain.add_worksheet('Hold out')
IrisTrainHojaFold = IrisTrain.add_worksheet('Fold')
IrisTest = xlsxwriter.Workbook('IrisTest.xlsx')
IrisTestHoja = IrisTest.add_worksheet('Hold out')
IrisTestHojaFold = IrisTest.add_worksheet('Fold')

#Se ponen los titulos de las tablas
IrisTrainHoja.write(0, 0, "Petal lenght")
IrisTrainHoja.write(0, 1, "Petal whith")
IrisTrainHoja.write(0, 2, "Class")
IrisTrainHojaFold.write(0, 0, "Petal lenght")
IrisTrainHojaFold.write(0, 1, "Petal whith")
IrisTrainHojaFold.write(0, 2, "Class")

IrisTestHoja.write(0, 0, "Petal lenght")
IrisTestHoja.write(0, 1, "Petal whith")
IrisTestHoja.write(0, 2, "Class")
IrisTestHojaFold.write(0, 0, "Petal lenght")
IrisTestHojaFold.write(0, 1, "Petal whith")
IrisTestHojaFold.write(0, 2, "Class")

#################################################################################   Hold out
#Se escribe los datos en el excel
for x in range(len(fc)):
    if fc[x] == 'Iris-setosa': #los 1 son para que no trabaje, no olvidar quitarlos
        if setoIF <= setoI*0.7:
            IrisTrainHoja.write(IrisTrainf, 0, pl[x])
            IrisTrainHoja.write(IrisTrainf, 1, pw[x])
            IrisTrainHoja.write(IrisTrainf, 2, fc[x])
            setoIF = setoIF + 1
            IrisTrainf = IrisTrainf + 1
        else:
            IrisTestHoja.write(IrisTestf, 0, pl[x])
            IrisTestHoja.write(IrisTestf, 1, pw[x])
            IrisTestHoja.write(IrisTestf, 2, fc[x])
            IrisTestf = IrisTestf + 1
            
            
    if fc[x] == 'Iris-versicolor':
        if versiIF <= setoI*0.7:
            IrisTrainHoja.write(IrisTrainf, 0, pl[x])
            IrisTrainHoja.write(IrisTrainf, 1, pw[x])
            IrisTrainHoja.write(IrisTrainf, 2, fc[x])
            versiIF = versiIF + 1
            IrisTrainf = IrisTrainf + 1
        else:
            IrisTestHoja.write(IrisTestf, 0, pl[x])
            IrisTestHoja.write(IrisTestf, 1, pw[x])
            IrisTestHoja.write(IrisTestf, 2, fc[x])
            IrisTestf = IrisTestf + 1

    if fc[x] == 'Iris-virginica':
        if virIF <= setoI*0.7:
            IrisTrainHoja.write(IrisTrainf, 0, pl[x])
            IrisTrainHoja.write(IrisTrainf, 1, pw[x])
            IrisTrainHoja.write(IrisTrainf, 2, fc[x])
            virIF = virIF + 1
            IrisTrainf = IrisTrainf + 1
        else:
            IrisTestHoja.write(IrisTestf, 0, pl[x])
            IrisTestHoja.write(IrisTestf, 1, pw[x])
            IrisTestHoja.write(IrisTestf, 2, fc[x])
            IrisTestf = IrisTestf + 1
            

#################################################################################   K-fold
Elejidos = []
setosaLimite = setoI/10
versiLimite = versiI/10
virLimite = virI/10
setoCont = 0
versiCont = 0
virCont = 0
IrisTrainf = 1
IrisTestf = 1
completo = 0

for x in range(len(fc)):
    if fc[x] == 'Iris-setosa':
        if setoCont <= setosaLimite:
            Elejidos.append(x)
            setoCont = setoCont + 1
            
    if fc[x] == 'Iris-versicolor':
        if versiCont <= versiLimite:
            Elejidos.append(x)
            versiCont = versiCont +1

    if fc[x] == 'Iris-virginica':
        if virCont <= virLimite:
            Elejidos.append(x)
            virCont = virCont + 1
            
for x in range(len(fc)):
    for y in range(len(Elejidos)):
        if x == Elejidos[y]:
            IrisTestHojaFold.write(IrisTestf, 0, pl[x])
            IrisTestHojaFold.write(IrisTestf, 1, pw[x])
            IrisTestHojaFold.write(IrisTestf, 2, fc[x])
            IrisTestf = IrisTestf + 1

for x in range(len(fc)):
    for y in range(len(Elejidos)):
        if x != Elejidos[y]:
            IrisTrainHojaFold.write(IrisTrainf, 0, pl[x])
            IrisTrainHojaFold.write(IrisTrainf, 1, pw[x])
            IrisTrainHojaFold.write(IrisTrainf, 2, fc[x])
            IrisTrainf = IrisTrainf + 1

print("\nElejidos: ", Elejidos)          

#se cierran los archivos
IrisTrain.close()
IrisTest.close()

