#Bonilla Jalomo Daniel
#Castillo Sanchez Emilio
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
                

#la funcion checar se encarga de saber si el juego llego a un punto final verificando las 8 posiciones de victoria
def Checar(EJ):
    #este if es para las posiciones de victoria del jugador
    if (EJ[0] == 1 and EJ[1] == 1 and EJ[2] == 1) or (EJ[3] == 1 and EJ[4] == 1 and EJ[5] == 1) or (EJ[6] == 1 and EJ[7] == 1 and EJ[8] == 1) or (EJ[0] == 1 and EJ[3] == 1 and EJ[6] == 1) or (EJ[1] == 1 and EJ[4] == 1 and EJ[7] == 1) or (EJ[2] == 1 and EJ[5] == 1 and EJ[8] == 1) or (EJ[0] == 1 and EJ[4] == 1 and EJ[8] == 1) or (EJ[2] == 1 and EJ[4] == 1 and EJ[6] == 1):
        print("El ganador es el jugador")
        return True
    #este elif es para las posiciones de victoria de la computadora
    elif (EJ[0] == 2 and EJ[1] == 2 and EJ[2] == 2) or (EJ[3] == 2 and EJ[4] == 2 and EJ[5] == 2 ) or (EJ[6] == 2 and EJ[7] == 2 and EJ[8] == 2) or (EJ[0] == 2 and EJ[3] == 2 and EJ[6] == 2) or (EJ[1] == 2 and EJ[4] == 2 and EJ[7] == 2) or (EJ[2] == 2 and EJ[5] == 2 and EJ[8] == 2) or (EJ[0] == 2 and EJ[4] == 2 and EJ[8] == 2) or (EJ[2] == 2 and EJ[4] == 2 and EJ[6] == 2):
        print("El ganador es la computadora")
        return True
    #Este else es por si no se llego a la victoria de ninguno de los 2
    else:
        #este ultimo if de la funcion checa si todavia hay espacio para una jugada, si no lo hay lo marca como empate porque no hay otro movimiento disponible
        if Espaciosdisponibles == 0:
            print("Empate")
            return True
        else:
            return False
    #La funcion devuelve un True si detecta que acabo el juego, de lo contraria devuelve un False y el juego continua
   

#La funcion jugada se encarga de realizar la jugada del computador, checa cuales espacios hay en blanco en el tablero y escoge uno al azar para realizar su tirada
def Jugada(EJ):
    auxiliar = [] #lista donde se guardan las posibles jugadas
    for i in range(0,9):
        if EJ[i] == 0 : #se busca y agrega a la lista el espacio
            auxiliar.append(i)
    try: 
        EJ[random.choice(auxiliar)] = 2 #escoge la jugada al azar haciendo uso de la funcion random.choice()
    except:
        pass
    

#Este es el esqueleto principal del programa
print("El jugador es representado con X y la computadora con O") #da un mensaje inicial el cual indica la representacion de cada uno       
while True: #El while se encarga de mantener en ciclo el programa para el juego
    Imprimir(Estadodejuego) #Imprime un primer tablero vacio o el tablero con la ultima jugada en un ciclo posterior
    
    movimiento = int(input("\n Selecciona una casilla para hacer un movimento(numerada del 1 al 9):")) #da al jugador el primer movimiento y castea la respuesta a un int
    if movimiento >= 1 and movimiento <= 9: #Checa que sea una jugada legal
        if Estadodejuego[movimiento-1] == 0: #Verifica que la jugada es en un espacio vacio, de lo contrario marca error
            Estadodejuego[movimiento-1] = 1 #guarda la jugada 
            Espaciosdisponibles = Estadodejuego.count(0) #Verifica el numero de espacios disponibles
            resultado = Checar(Estadodejuego) #Checa si  no se llego a un final en el juego
            if resultado == True:  #Si detecta un final rompe el ciclo while para acabar el programa
                Imprimir(Estadodejuego) #Antes de acabar imprime el resultado final
                break
            Jugada(Estadodejuego) #Aqui es donde la computadora hace su jugada
            Espaciosdisponibles = Estadodejuego.count(0) 
            resultado = Checar(Estadodejuego)
            if resultado == True:
                Imprimir(Estadodejuego)
                break
        else:
            print("Casilla ya seleccionada")
    else:
        print("Movimiento invalido")
