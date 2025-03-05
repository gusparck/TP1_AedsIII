import listaAdjacencias
import matrizAdjacencias

# versao recursiva do DFS:
def dfs(grafo, s):
    R = []
    visitado = [False] * grafo.numVertices
    dfsRecursivo(grafo, R, visitado, s)
    return R
    
def dfsRecursivo(grafo, R, visitado, u):
    visitado[u] = True
    R.append(u)
    for v, _ in grafo.vizinhos(u):
        if not visitado[v]:
            dfsRecursivo(grafo, R, visitado, v)

# versao iterativa do DFS:
def dfsIterativo(grafo, s):
    R = []
    pilha = []
    visitado = [False] * grafo.numVertices
    pilha.append(s)
    visitado[s] = True
    while pilha:
        u = pilha.pop()
        R.append(u)
        for v, _ in grafo.vizinhos(u):
            if not visitado[v]:
                pilha.append(v)
                visitado[v] = True
    return R


# BFS:
def bfs(grafo, inicio, fim):
    visitados = [False] * grafo.numVertices
    fila = [(inicio, [])]  # (vértice, caminho até ele)
    visitados[inicio] = True
    
    while fila:
        vertice, caminho = fila.pop(0)
        caminho_atual = caminho + [vertice]
        
        if vertice == fim:
            return caminho_atual
        
        for vizinho, _ in grafo.vizinhos(vertice):
            if not visitados[vizinho]:
                visitados[vizinho] = True
                fila.append((vizinho, caminho_atual))
    
    return None