from math import inf as infinity
from random import choice
import platform
import time
from os import system

"""
Se definen tanto a los humanos como a la computadora, ademas se usa una matriz para representar el tablero de juego
"""
HUMANO = -1
COMP = +1
tabla = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
]


def evaluar(EstadoTabla): 
    """
    :return: +1 si la compu gana; -1 si el humano gana; 0 empate
    esto es para ser usado en el minmax y no para revisar si se ha ganado el juego
    """
    if victoria(EstadoTabla, COMP):
        puntos = +1
    elif victoria(EstadoTabla, HUMANO):
        puntos = -1
    else:
        puntos = 0

    return puntos


def victoria(EstadoTabla, jugador):
    """
    Se comprueba si alguien gano al completar un conjunto de tres en fila, columna o diagonal
    jugador se refiere tanto al humano como a la computadora
    """
    win_state = [
        [EstadoTabla[0][0], EstadoTabla[0][1], EstadoTabla[0][2]],
        [EstadoTabla[1][0], EstadoTabla[1][1], EstadoTabla[1][2]],
        [EstadoTabla[2][0], EstadoTabla[2][1], EstadoTabla[2][2]],
        [EstadoTabla[0][0], EstadoTabla[1][0], EstadoTabla[2][0]],
        [EstadoTabla[0][1], EstadoTabla[1][1], EstadoTabla[2][1]],
        [EstadoTabla[0][2], EstadoTabla[1][2], EstadoTabla[2][2]],
        [EstadoTabla[0][0], EstadoTabla[1][1], EstadoTabla[2][2]],
        [EstadoTabla[2][0], EstadoTabla[1][1], EstadoTabla[0][2]],
    ]
    if [jugador, jugador, jugador] in win_state:
        return True
    else:
        return False


def game_over(state):
    """
    llama a la funcion victoria para ver si alguien gano
    """
    return victoria(state, HUMANO) or victoria(state, COMP)


def posicionesVacias(state):
    """
    para saber cuales posiciones estan vacias y pueden ser ocupadas por el jugador o la compu
    """
    posiciones = []

    for x, row in enumerate(state):
        for y, posicion in enumerate(row):
            if posicion == 0:
                posiciones.append([x, y])

    return posiciones


def validarPosicion(x, y):
    """
    para saber que la posicion elegida es valida
    """
    if [x, y] in posicionesVacias(tabla):
        return True
    else:
        return False


def setMovimineto(x, y, player):
    """
    llenar la posicion en el tablero despues de validar que es una eleccion aceptable porque aun no esta ocupado dicho lugar
    """
    if validarPosicion(x, y):
        tabla[x][y] = player
        return True
    else:
        return False


def minimax(EstadoTabla, profundidad, jugador):
    """
    (0 <= profundidad <= 9),
    retorna una lista con [mejor fila, mejor columna, mejor puntiacion]
    Primero se revisa si se trata de la computadora o el jugador para saber que movimientos son mejores
    Despues se revisa si se ha acabado la partida.
    Si ese no es el caso entonces se va explorando el arbol de forma recursiva para encontrar la mejor opcion
    """
    if jugador == COMP:
        mejorOpcion = [-1, -1, -infinity]
    else:
        mejorOpcion = [-1, -1, +infinity]

    if profundidad == 0 or game_over(EstadoTabla):
        puntuacion = evaluar(EstadoTabla)
        return [-1, -1, puntuacion]

    for posicion in posicionesVacias(EstadoTabla):
        x, y = posicion[0], posicion[1]
        EstadoTabla[x][y] = jugador
        puntuacion = minimax(EstadoTabla, profundidad - 1, -jugador)
        EstadoTabla[x][y] = 0
        puntuacion[0], puntuacion[1] = x, y

        if jugador == COMP:
            if puntuacion[2] > mejorOpcion[2]:
                mejorOpcion = puntuacion  # max
        else:
            if puntuacion[2] < mejorOpcion[2]:
                mejorOpcion = puntuacion  # min

    return mejorOpcion

def dibujarTabla(EstadoTabla, eleccionComputadora, eleccionHumano):
    """
    eleccionHumano y eleccionComputadora, son para poner X y O, lo demas solo es para hacer la tablita y se vea bonito
    """
    simboloEleccion = {
        -1: eleccionHumano,
        +1: eleccionComputadora,
        0: ' '
    }
    linea = '---------------'

    print('\n' + linea)
    for fila in EstadoTabla:
        for posicion in fila:
            simbolo = simboloEleccion[posicion]
            print(f'| {simbolo} |', end='')
        print('\n' + linea)


def turnoTerminator(eleccionComputadora, eleccionHumano):
    """
    Turno de la compu, se revisa si ya se acabo el juego, si este no es el caso entonces se dibuja la HUD
    Si es el primer turno se elije una posicion predefinida, si no, se hace el minmax y se pone en la posicion
    """
    profundidad = len(posicionesVacias(tabla))
    if profundidad == 0 or game_over(tabla):
        return

    system('cls')
    print(f'Computer turn [{eleccionComputadora}]')
    dibujarTabla(tabla, eleccionComputadora, eleccionHumano)

    if profundidad == 9:
        x = choice([0, 1, 2])
        y = choice([0, 1, 2])
    else:
        movimiento = minimax(tabla, profundidad, COMP)
        x, y = movimiento[0], movimiento[1]

    setMovimineto(x, y, COMP)
    time.sleep(1)


def turnoHumano(eleccionComputadora, eleccionHumano):
    """
    Se revisa si se acabo el juego, si este no es el caso entonces se le pide al usuario que ingrese una posicion, si esta ocupada debe de elejir otra.
    
    """
    profundidad = len(posicionesVacias(tabla))
    if profundidad == 0 or game_over(tabla):
        return

    movimiento = -1
    movimientos = {
        1: [0, 0], 2: [0, 1], 3: [0, 2],
        4: [1, 0], 5: [1, 1], 6: [1, 2],
        7: [2, 0], 8: [2, 1], 9: [2, 2],
    }

    system('cls')
    print(f'Human turn [{eleccionHumano}]')
    dibujarTabla(tabla, eleccionComputadora, eleccionHumano)

    while movimiento < 1 or movimiento > 9:
        try:
            movimiento = int(input('Use numpad (1..9): '))
            cordenada = movimientos[movimiento]
            movimientoValido = setMovimineto(cordenada[0], cordenada[1], HUMANO)

            if not movimientoValido:
                print('Bad move')
                movimiento = -1
        except (EOFError, KeyboardInterrupt):
            print('Adios tonoto')
            exit()
        except (KeyError, ValueError):
            print('Bad choice')


def main():
    system('cls')
    #El humano elige el simbolo que quiere usar y si va primero o no
    eleccionHumano = ''  # X o O
    eleccionComputadora = ''  # X o O
    quienVaPrimero = ''

    #Por si meten alguna opcion no valida para el simbolo y el ir primero o no
    while eleccionHumano != 'O' and eleccionHumano != 'X':
        try:
            print('')
            eleccionHumano = input('X o O\nSe eliguio: ').upper()
        except (EOFError, KeyboardInterrupt):
            print('Bye')
            exit()
        except (KeyError, ValueError):
            print('Opcion no valido')

    if eleccionHumano == 'X':
        eleccionComputadora = 'O'
    else:
        eleccionComputadora = 'X'

    system('cls')
    while quienVaPrimero != 'S' and quienVaPrimero != 'N':
        try:
            quienVaPrimero = input('Quieres ir primero?[s/n]: ').upper()
        except (EOFError, KeyboardInterrupt):
            print('Bye')
            exit()
        except (KeyError, ValueError):
            print('Opcion no valido')

    #Se continuac el juego hasta que alguien gane o no haya mas movimientos disponibles osea un empate
    while len(posicionesVacias(tabla)) > 0 and not game_over(tabla):
        if quienVaPrimero == 'N':
            turnoTerminator(eleccionComputadora, eleccionHumano)
            quienVaPrimero = ''

        turnoHumano(eleccionComputadora, eleccionHumano)
        turnoTerminator(eleccionComputadora, eleccionHumano)

    #Se imprimen los mensajes de vitoria o empate junto con la trablita
    if victoria(tabla, HUMANO):
        system('cls')
        print(f'Humano [{eleccionHumano}]')
        dibujarTabla(tabla, eleccionComputadora, eleccionHumano)
        print('YOU WIN!')
    elif victoria(tabla, COMP):
        system('cls')
        print(f'Compu [{eleccionComputadora}]')
        dibujarTabla(tabla, eleccionComputadora, eleccionHumano)
        print('YOU LOSE!')
    else:
        system('cls')
        dibujarTabla(tabla, eleccionComputadora, eleccionHumano)
        print('EMPATE!')

    exit()


if __name__ == '__main__':
    main()
