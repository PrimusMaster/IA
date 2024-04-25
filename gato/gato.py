from math import inf as infinity
from random import choice
import platform
import time
from os import system

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
    Se comprueba si alguien gano
    jugador: es el humano o la computadora
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
    para saber cuales posiciones estan vacias
    """
    posiciones = []

    for x, row in enumerate(state):
        for y, posicion in enumerate(row):
            if posicion == 0:
                posiciones.append([x, y])

    return posiciones


def validarPosicion(x, y):
    """
    para saber que eleccion es valida
    """
    if [x, y] in posicionesVacias(tabla):
        return True
    else:
        return False


def setMovimineto(x, y, player):
    """
    llenar la posicion en el tablero
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
    Print the board on console
    :param state: current state of the board
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
    It calls the minimax function if the depth < 9,
    else it choices a random coordinate.
    :param c_choice: computer's choice X or O
    :param h_choice: human's choice X or O
    :return:
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
    The Human plays choosing a valid move.
    :param c_choice: computer's choice X or O
    :param h_choice: human's choice X or O
    :return:
    """
    profundidad = len(posicionesVacias(tabla))
    if profundidad == 0 or game_over(tabla):
        return

    # Dictionary of valid moves
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
    """
    Main function that calls all functions
    """
    system('cls')
    eleccionHumano = ''  # X or O
    eleccionComputadora = ''  # X or O
    quienVaPrimero = ''  # if human is the first

    # Human chooses X or O to play
    while eleccionHumano != 'O' and eleccionHumano != 'X':
        try:
            print('')
            eleccionHumano = input('Choose X or O\nChosen: ').upper()
        except (EOFError, KeyboardInterrupt):
            print('Bye')
            exit()
        except (KeyError, ValueError):
            print('Bad choice')

    # Setting computer's choice
    if eleccionHumano == 'X':
        eleccionComputadora = 'O'
    else:
        eleccionComputadora = 'X'

    # Human may starts first
    system('cls')
    while quienVaPrimero != 'Y' and quienVaPrimero != 'N':
        try:
            quienVaPrimero = input('First to start?[y/n]: ').upper()
        except (EOFError, KeyboardInterrupt):
            print('Bye')
            exit()
        except (KeyError, ValueError):
            print('Bad choice')

    # Main loop of this game
    while len(posicionesVacias(tabla)) > 0 and not game_over(tabla):
        if quienVaPrimero == 'N':
            turnoTerminator(eleccionComputadora, eleccionHumano)
            quienVaPrimero = ''

        turnoHumano(eleccionComputadora, eleccionHumano)
        turnoTerminator(eleccionComputadora, eleccionHumano)

    # Game over message
    if victoria(tabla, HUMANO):
        system('cls')
        print(f'Human turn [{eleccionHumano}]')
        dibujarTabla(tabla, eleccionComputadora, eleccionHumano)
        print('YOU WIN!')
    elif victoria(tabla, COMP):
        system('cls')
        print(f'Computer turn [{eleccionComputadora}]')
        dibujarTabla(tabla, eleccionComputadora, eleccionHumano)
        print('YOU LOSE!')
    else:
        system('cls')
        dibujarTabla(tabla, eleccionComputadora, eleccionHumano)
        print('DRAW!')

    exit()


if __name__ == '__main__':
    main()
