import random
import string
from tkinter import Y

def create_maze(m_high, m_witdh, m_possible, start, end):
     
    sx, sy, px, py = start
    ex, ey = end
    b = '0'
    xc = sx
    yc = sy
    List = [0,1] #Para elegir las paredes con probabilidad ponderada
    #print("\n(", sx,",", sy ,") ", end)

    t_maze = []
    for x in range(m_high):    
        a = []
        for y in range(m_witdh):   
            
            if x == sx and y == sy:
                b = 'S'
            else: 
                if x == ex and y == ey:
                    b = 'E'
                else:
                    b = '0'
                
            a.append(b)
        t_maze.append(a)
    
    while xc != ex or yc != ey:
        if t_maze[xc][yc] != 'S' and t_maze[xc][yc] != 'E':
            t_maze[xc][yc] = str(3)
        if xc < ex:
            xc += 1
        else:
            if xc > ex:
                xc -= 1
            else:
                if yc < ey:
                    yc += 1
                else:
                    if yc > ey:
                        yc -= 1

    for x in range(m_high):
       for y in range(m_witdh):
            if t_maze[x][y] == 'S':
                t_maze[x][y] = 'S'
            else:
                if t_maze[x][y] == 'E':
                    t_maze[x][y] = 'E'
                else:
                    if t_maze[x][y] == '3':
                        t_maze[x][y] = '0'
                    else:  
                        temp = random.choices(List, weights=(20, 80), k=1)
                        t_maze[x][y] = "".join(map(str, temp))

    for row in t_maze:
        print("".join(row))

    if m_possible == 0: #Hace que el laberinto sea imposible de resolver
        if sx-1 > 0:
                #print("\nTop")
                t_maze[sx-1][sy] = '1'
        if sy-1 > 0:
                #print("\nLeft")
                t_maze[sx][sy-1] = '1'
        if sy+1 < m_witdh:
                #print("\nRight")
                t_maze[sx][sy+1] = '1'
        if sx+1 < m_high:
                #print("\nBottom")
                t_maze[sx+1][sy] = '1'

    return t_maze

def solve_maze(maze, start, end):
    frontera = [start] #se mete el primer nodo a la forntera
    visitados = []
    while frontera:
        x, y, px, py = frontera[0] #Revisa el nodo mas antiguo por eso agarra el 0

        # If reached the end point
        if (x, y) == end:
            visitados.append((x, y, px, py))
            return True, visitados

        # Mark as visited
        if maze[x][y] != 'S':
            maze[x][y] = '2'
        
#Comprueba las 4 direcciones del nodo actual, si son validos y no han sido visitados los guarda en frontera
        if x-1 > 0:
            if  (maze[x-1][y] == '0' or maze[x-1][y] == 'E') and maze[x-1][y] != '2':
                #print("\nTop")
                frontera.append((x-1, y, x, y))

        if y-1 > 0:
            if  (maze[x][y-1] == '0' or maze[x][y-1] == 'E') and maze[x][y-1] != '2':
                #print("\nLeft")
                frontera.append((x, y-1, x, y))
            
        if y+1 < m_witdh:
            if  (maze[x][y+1] == '0' or maze[x][y+1] == 'E') and maze[x][y+1] != '2':
                #print("\nRight")
                frontera.append((x, y+1, x, y))
            
        if x+1 < m_high:
            if  (maze[x+1][y] == '0' or maze[x+1][y] == 'E') and maze[x+1][y] != '2':
                #print("\nBottom")
                frontera.append((x+1, y, x, y))
            
        visitados.append((x, y, px, py)) #Agrega el nodo visitado
        frontera.pop(0) #quita nodo frontera

    return False, [] #Si no se llega a un nodo con la solucion entonces no hay respuesta


if __name__ == "__main__":
    # 0 = open path, 1 = wall, S = start, E = end
    '''
    maze = [
        ['S', '1', '1', '1', '1'],
        ['0', '0', '1', 'E', '1'],
        ['1', '0', '1', '0', '1'],
        ['1', '0', '0', '0', '0'],
        ['1', '1', '1', '1', '1']
    ]
    start = (0, 0, 0, 0)
    end = (1, 3)
    '''

    m_high = 5
    m_witdh = 5
    m_possible = 0
    
#Creando la posicion del inicio y la salida
    eh = (-1,-1)
    ew = (-1,-1)
    sh = random.randint(0, m_high-1)
    sw = random.randint(0, m_witdh-1)
    
    eh = random.randint(0, m_high-1)
    if eh == sh:
        while eh == sh:
            eh = random.randint(0, m_high-1)
            
    ew = random.randint(0, m_witdh-1)
    if eh == sh:
        while eh == sh:
            eh = random.randint(0, m_high-1)
            
    r_start = (sh, sw, sh, sw) #Primer par nodo actual, segundo par nodo padre
    r_end = (eh, eh)
    
    r_maze = create_maze(m_high, m_witdh, m_possible, r_start, r_end)
    solved, path = solve_maze(r_maze, r_start, r_end)

    print("\n")
    if solved:
        print("Maze Solved!")
        for x, y, px, py in path:
            if r_maze[x][y] != 'S' and r_maze[px][py] != 'S':
                r_maze[px][py] = '*'
            if r_maze[x][y] == '2':
                r_maze[x][y] = '0'
        for row in r_maze:
            print("".join(row))
    else:
        print("Maze cannot be Solved!")
        for row in r_maze:
            print("".join(row))
