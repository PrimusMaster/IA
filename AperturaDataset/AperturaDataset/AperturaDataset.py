import numpy as np

    #Se calcula el promedio al sumar todos los valores de array y despues se dividio entre la cantidad de valores
def promedio(lista):
    tot = 0
    for x in range(len(lista)):
        tot = tot + float(lista[x])
    return (str(tot/len(lista)))


    #Se abre y cierra el archivo para poder obtener su informacion
with open("bezdekIris.data", "r", encoding='utf-8-sig') as f:
    stringF = f.read()
    #print(stringF)
f.close()

    #se divide el archivo en filas
fila = stringF.split("\n")

    #Se generan los arrays donde se guardaran cada tipo de dato
dato = []
dato0 = []
dato1 = []
dato2 = []
dato3 = []
dato4 = []

    #Se recorre linea por linea y se separa por tipo de dato ya que estan separados por comas
for x in fila:
    dato = dato + x.split(",")

    #Para que se elija en que array va cada dato
i = 0

    #Se recorre cada dato y se guarda en su array corespondiente
for x in range(len(dato)-2):
    if i == 0:
        dato0.append(float(dato[x]))
        i = i+1
    else:
        if i == 1:
            dato1.append(float(dato[x]))
            i = i+1
        else:
            if i == 2:
                dato2.append(float(dato[x]))
                i = i+1
            else:
                if i == 3:
                    dato3.append(float(dato[x]))
                    i = i+1
                else:
                    if i == 4:
                        dato4.append(str(dato[x]))
                        i = 0
        

    #Primer se imprimen los arrays de cada datos, despues se calculan el promedio, varianza y la desviacion, para despues ser impresos 
print("Datos 1: " + dato0)
resul_prom = promedio(dato0)
varianza = np.var(dato0, ddof = 1)
desv_estandar = np.sqrt(varianza)
print("\n\tPromedio: "+ resul_prom +"\tVarianza: "+ str(varianza) +"\tDesviacion estandar: "+ str(desv_estandar) +"\n\n")


print("Datos 2: " + dato1)
resul_prom = promedio(dato1)
varianza = np.var(dato1, ddof = 1)
desv_estandar = np.sqrt(varianza)
print("\n\tPromedio: "+ resul_prom +"\tVarianza: "+ str(varianza) +"\tDesviacion estandar: "+ str(desv_estandar) +"\n\n")


print("Datos 3: " + dato2)
resul_prom = promedio(dato2)
varianza = np.var(dato2, ddof = 1)
desv_estandar = np.sqrt(varianza)
print("\n\tPromedio: "+ resul_prom +"\tVarianza: "+ str(varianza) +"\tDesviacion estandar: "+ str(desv_estandar) +"\n\n")


print("Datos 4: " + dato3)
resul_prom = promedio(dato3)
varianza = np.var(dato3, ddof = 1)
desv_estandar = np.sqrt(varianza)
print("\n\tPromedio: "+ resul_prom +"\tVarianza: "+ str(varianza) +"\tDesviacion estandar: "+ str(desv_estandar) +"\n\n")


    #Solo se imprime el array ya que son strings y no se le puede sacar los datos pedidos
print(dato4)
print("\n\n")