#Bonilla Jalomo Daniel
#Castillo Sanchez Emilio
#Sistema de ecuaciones, el ultimo valor es el valor de la igualdad de su correspondiente acuacion
ec1 = [3,2,1,1]
ec2 = [5,3,4,2]
ec3 = [1,1,-1,1]
#Variables para facilitar algunas cosas
espacio = ", "
rangoNum = 100
#resulN es para guardar el resultado de cada ecuacion en cada iteracion
resul1 = resul2 = resul3 = 0

#Cada ciclo for para cada variable, primero itera Z, cuando termina con Z entonces "Y" aunmenta en 1 y Z regresa a -100
#esto se repite hasta terminar las iteraciones de X
for x in range (-rangoNum, rangoNum):
    for y in range (-rangoNum, rangoNum):
        for z in range (-rangoNum, rangoNum):
            #Se hace la multiplicacion de X,Y,Z para cada ecuacion y se guarda el resultado
            resul1 = ec1[0]*x + ec1[1]*y + ec1[2]*z
            resul2 = ec2[0]*x + ec2[1]*y + ec2[2]*z
            resul3 = ec3[0]*x + ec3[1]*y + ec3[2]*z
            #Comprueba si los tres resultados son los correctos
            if resul1 == ec1[3] and ec2[3] == resul2 and ec3[3] == resul3:
                print("\nX = ", x,"\nY = ", y, "\nZ = ", z, "\n")    
                
print("\nFin del programa")
