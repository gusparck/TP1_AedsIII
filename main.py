import matrizAdjacencias
import sys
import time

def lerLabirinto(nomeArquivo):
    with open(nomeArquivo, 'r') as arquivo:
        labirinto = [linha.strip() for linha in arquivo.readlines()]
    
    linhas = len(labirinto)
    colunas = len(labirinto[0])
    
    mapa_vertices = {}
    contador_id = 0
    posicao_inicio = None
    posicao_fim = None
    
    for i in range(linhas):
        for j in range(colunas):
            if labirinto[i][j] != '#':
                mapa_vertices[(i, j)] = contador_id
                contador_id += 1
                if labirinto[i][j] == 'S':
                    posicao_inicio = (i, j)
                elif labirinto[i][j] == 'E':
                    posicao_fim = (i, j)
    
    grafo = matrizAdjacencias.MatrizAdjacencias(contador_id)
    
    movimentos = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    for (i, j), id_vertice in mapa_vertices.items():
        for di, dj in movimentos:
            ni, nj = i + di, j + dj
            
            if (0 <= ni < linhas and 0 <= nj < colunas and 
                labirinto[ni][nj] != '#' and 
                (ni, nj) in mapa_vertices):
                
                id_vizinho = mapa_vertices[(ni, nj)]
                grafo.addAresta(id_vertice, id_vizinho)
    
    return grafo, mapa_vertices, posicao_inicio, posicao_fim

def encontrarCaminho(grafo, inicio_id, fim_id):
    visitados = [False] * grafo.numVertices
    fila = [(inicio_id, [])]  
    visitados[inicio_id] = True
    
    while fila:
        vertice, caminho = fila.pop(0)
        caminho_atual = caminho + [vertice]
        
        if vertice == fim_id:
            return caminho_atual
        
        for vizinho, _ in grafo.vizinhos(vertice):
            if not visitados[vizinho]:
                visitados[vizinho] = True
                fila.append((vizinho, caminho_atual))
    
    return None  # Caso não haja caminho

if len(sys.argv) == 2:  # Execução para Labirinto
    nomeArquivo = sys.argv[1]
    start = time.time()

    grafo, mapa_vertices, inicio, fim = lerLabirinto(nomeArquivo)
    inicio_id = mapa_vertices[inicio]
    fim_id = mapa_vertices[fim]
    caminho_ids = encontrarCaminho(grafo, inicio_id, fim_id)

    if caminho_ids:
        mapa_inverso = {v: k for k, v in mapa_vertices.items()}
        caminho_coords = [mapa_inverso[id] for id in caminho_ids]
        caminho_str = " -> ".join([f"({i},{j})" for i, j in caminho_coords])
        print(f"Caminho encontrado: {caminho_str}")
    else:
        print("Não foi possível encontrar um caminho.")

    end = time.time()
    print(f"Tempo de execução: {end - start:.6f} s")
    