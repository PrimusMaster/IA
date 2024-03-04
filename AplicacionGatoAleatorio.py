import random

#Se establecen estas 5 variables auxiliares que ayudan a generar la interfaz de juego
aux1 = "   "
aux2 = " X "
aux3 = " O "
aux4 = "|"
aux5 = "----"

#Esta variable es la que se usa para representar el juego, el juego se representa el 0 como espacio vacio, el 1 como la x del jugador y el 2 como el O de la computadora
Estadodejuego = [0 , 0 , 0 , 
                 0 , 0 , 0 ,
                 0 , 0 , 0]

#Esta variable marca el numero de espacios disponibles en el juego para saber cuando se llego a un empate
Espaciosdisponibles = 9

#La funcion imprimir es la que se encarga de darle formato al arreglo del juego para poder ser visible por el jugador
def Imprimir(EJ):
    for i in range(0,9): #Este primer ciclo for se encarga de atravesar cada elemento en el arreglo y ver que valor contiene para mostrar una señal    
        if EJ[i] == 0:
            print(aux1, end = "")
            if (i+1) % 3 != 0: #Estos if se encargan de hacer saber a la funcion cuando llego a un elemento 3 y debe de hacer salto de linea, si no, solamente imprimen el objeto
                print(aux4, end = "")
            else:
                print("\n")
                for j in range(0,3):
                    print(aux5, end = "")
                print("\n")
        elif EJ[i] == 1:
            print(aux2, end = "")
            if (i+1) % 3 != 0:
                print(aux4, end = "")
            else:
                print("\n")
                for j in range(0,3):
                    print(aux5, end = "")
                print("\n")
        elif EJ[i] == 2:
            print(aux3, end = "")
            if (i+1) % 3 != 0:
                print(aux4, end = "")
            else:
                print("\n")
                for j in range(0,3):
                    print(aux5, end = "")
                print("\n")
