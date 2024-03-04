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

