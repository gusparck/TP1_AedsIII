import listaAdjacencias
import matrizAdjacencias

# versao recursiva do DFS (Aula 07 - slide 7):
def dfs(self, s):
        R = []
        for v in range(self.numVertices):
            visitado[v] = False
        dfsRecursivo(self, R, visitado, s)
        return R
    
def dfsRecursivo(self, R, visitado, u):
        visitado[u] = True
        R.append(u)
        for v in range(u):
            if visitado[v] == False:
                dfsRecursivo(self, R, visitado, v)
        


# versao iterativa do DFS (Aula 07 - slide 8):
def dfsIterativo(self, s):
    R = []
    pilha = []
    for v in range(self.numVertices):
        visitado[v] = False
    pilha.append(s)
    visitado[s] = True
    while pilha:
        u = pilha.pop()
        R.append(u)
        for v in range(u):
            if visitado[v] == False:
                pilha.append(v)
                visitado[v] = True
    return R

# BFS (Aula 07 - slide 15):
def bfs(self, s):
    R = []
    fila = []
    for v in range(self.numVertices):
        visitado[v] = False
    fila.append(s)
    visitado[s] = True
    while fila:
        u = fila.pop()
        R.append(u)
        for v in range(u):
            if visitado[v] == False:
                fila.append(v)
                visitado[v] = True
    return R