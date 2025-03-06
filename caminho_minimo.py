import time
import heapq #Disponibiliza funções para manipulação de filas de prioridade
from matrizAdjacencias import MatrizAdjacencias


INF = float('inf')

def dijkstra(grafo, origem, destino):
    inicio_tempo = time.time()
    num_vertices = grafo.ordem()  
    
    dist = [INF] * num_vertices
    predecessores = [-1] * num_vertices
    visitados = [False] * num_vertices

    dist[origem] = 0
    fila_prioridade = [(0, origem)]

    while fila_prioridade:
        custo_atual, u = heapq.heappop(fila_prioridade)
        if visitados[u]:
            continue
        visitados[u] = True

        
        for v, peso in grafo.vizinhos(u):  
            novo_custo = dist[u] + peso
            if novo_custo < dist[v]:
                dist[v] = novo_custo
                predecessores[v] = u
                heapq.heappush(fila_prioridade, (novo_custo, v))

    caminho = reconstruir_caminho(predecessores, origem, destino)
    tempo_execucao = time.time() - inicio_tempo
    return caminho, dist[destino], tempo_execucao

def reconstruir_caminho(predecessores, origem, destino):
    caminho = []
    atual = destino
    while atual != -1:
        caminho.append(atual)
        atual = predecessores[atual]
    caminho.reverse()
    return caminho if caminho[0] == origem else []

INF = float('inf')

def bellman_ford(grafo, origem, destino):
    inicio_tempo = time.time()
    num_vertices = grafo.ordem()  

    dist = [INF] * num_vertices
    predecessores = [-1] * num_vertices

    dist[origem] = 0

   
    for _ in range(num_vertices - 1):
        for u in range(num_vertices):
            
            for v, peso in grafo.vizinhos(u):  
                if dist[u] + peso < dist[v]:
                    dist[v] = dist[u] + peso
                    predecessores[v] = u

    caminho = reconstruir_caminho(predecessores, origem, destino)
    tempo_execucao = time.time() - inicio_tempo
    return caminho, dist[destino], tempo_execucao

def reconstruir_caminho(predecessores, origem, destino):
    caminho = []
    atual = destino
    while atual != -1:
        caminho.append(atual)
        atual = predecessores[atual]
    caminho.reverse()
    return caminho if caminho[0] == origem else []



def floyd_warshall(grafo):
    inicio_tempo = time.time()
    num_vertices = grafo.ordem()
    
    # Inicializando a matriz de distâncias
    dist = [[float('inf')] * num_vertices for _ in range(num_vertices)]
    predecessores = [[-1] * num_vertices for _ in range(num_vertices)]
    
    
    for u in range(num_vertices):
        dist[u][u] = 0  
        for v, peso in grafo.vizinhos(u):
            dist[u][v] = peso
            predecessores[u][v] = u
    
    # Algoritmo de Floyd-Warshall
    for k in range(num_vertices):
        for i in range(num_vertices):
            for j in range(num_vertices):
                if dist[i][k] != float('inf') and dist[k][j] != float('inf'):
                    novo_custo = dist[i][k] + dist[k][j]
                    if novo_custo < dist[i][j]:
                        dist[i][j] = novo_custo
                        predecessores[i][j] = predecessores[k][j]
    
    tempo_execucao = time.time() - inicio_tempo
    return dist, predecessores, tempo_execucao

def reconstruir_caminho_floyd(predecessores, origem, destino):
    if predecessores[origem][destino] == -1:
        return []  # Não há caminho
    caminho = []
    atual = destino
    while atual != origem:
        caminho.append(atual)
        atual = predecessores[origem][atual]
    caminho.append(origem)
    caminho.reverse()
    return caminho