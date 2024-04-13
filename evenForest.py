import math
import os
import random
import re
import sys

# Complete the evenForest function below.
#  https://www.hackerrank.com/challenges/even-tree/problem
#  ralizado por Jairo Cogollo
#  mickt681@gmail.com
#
#
def even_forest(tNodes, tEdges, tFrom, tTo):
    
    graph = [[] for _ in range(tNodes + 1)]
    '''Construir el grafo como una lista de adyacencia'''
    for i in range(tEdges):
        graph[tTo[i]].append(tFrom[i])
        '''Agregar arista de tTo a tFrom'''
        graph[tFrom[i]].append(tTo[i])
        ''' Agregar arista de tFrom a tTo'''
    
    def count_nodes(node, parent):
        '''Función para contar el número de nodos en un subárbol'''
        count = 1 
        '''Incluir el nodo actual'''
        for child in graph[node]:
            if child != parent: 
                count += count_nodes(child, node)
        return count

    def count_removed_edges(node, parent):
        '''Función para contar el número de aristas que se pueden eliminar para obtener
        un bosque con subárboles de nodos pares'''
        count = 0
        for child in graph[node]:
            if child != parent:
                subtree_nodes = count_nodes(child, node)
                if subtree_nodes % 2 == 0:  # => Si el subárbol tiene nodos pares
                    count += 1 
                count += count_removed_edges(child, node)
        return count
    
    result = count_removed_edges(1, 0)  # Comenzar desde el nodo raíz (1) con padre 0
    
    return result

if __name__ == '__main__':
    tNodes, tEdges = map(int, input().rstrip().split())

    tFrom = []
    tTo = []

    for _ in range(tEdges):
        fromToPair = list(map(int, input().rstrip().split()))
        tFrom.append(fromToPair[0])
        tTo.append(fromToPair[1])

    res = even_forest(tNodes, tEdges, tFrom, tTo)

    print(res)

    # fptr.write(str(res) + '\n')

   
# input de ejemplo
#10 9
#2 1
#3 1    
#4 3
#5 2
#6 1
#7 2
#8 6
#9 8
#10 8
