#Puzzle de 8 fichas con busqueda de coste uniforme
from arbol import Nodo

solucion = [1,2,3,4,5,6,7,8,0]

def BuscarSolucion(Posicion):
    solucionado=False
    nodos_visitados=[]
    nodoInicial = Nodo(Posicion)
    numiteraciones=0
    nodos_camino=[]
    nodos_camino.append(nodoInicial)
    nodos_camino
    while (not solucionado) and len(nodos_camino)!=0:
        if Posicion == solucion:
            break
        else:
            for i in range(0,9):
                if Posicion[i] == 0:
                   break
            movimientos = [i - 1, i + 1,i - 3,i + 3]
            for n in range(0,3):






if __name__ == "__main__":
    Problema = [0,1,2,3,4,5,6,7,8]
    BuscarSolucion(solucion)
    
    
    
    
    #estado_inicial = []
    #
    #nodo_solucion = buscar_solucion_BFS(estado_inicial, solucion)
    ##print(nodo_solucion.get_padre())
    ## mostrar resultado
    #resultado = []
    #nodo = nodo_solucion
    #while nodo.get_padre() != None:
    #    resultado.append(nodo.get_datos())
    #    #print(resultado)
    #    nodo = nodo.get_padre()
    #
    #resultado.append(estado_inicial)
    #resultado.reverse()
    