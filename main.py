import matrizAdjacencias
import listaAdjacencias
import info
import busca
import time
import sys
import caminho_minimo

def ler_grafo(nomeArquivo):
    with open(nomeArquivo, 'r') as arquivo:
        num_vertices, num_arestas = map(int, arquivo.readline().split())
        grafo = matrizAdjacencias.MatrizAdjacencias(num_vertices)
        
        for _ in range(num_arestas):
            origem, destino, peso = map(int, arquivo.readline().split())
            grafo.addAresta(origem, destino, peso)  
        
    return grafo

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
    
    return None 

if __name__ == "__main__":
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

    elif len(sys.argv) == 4:  # Execução para Caminho Mínimo em Grafo Ponderado
        nomeArquivo = sys.argv[1]
        origem = int(sys.argv[2])
        destino = int(sys.argv[3])

    grafo = ler_grafo(nomeArquivo)
    print("\nProcessando...\n")

    for nome, algoritmo in [("Dijkstra", caminho_minimo.dijkstra), 
                            ("Bellman-Ford", caminho_minimo.bellman_ford),
                            ("Floyd-Warshall", caminho_minimo.floyd_warshall)]:

        if nome == "Floyd-Warshall":
            distancias, predecessores, tempo_execucao = algoritmo(grafo)
            caminho = caminho_minimo.reconstruir_caminho_floyd(predecessores, origem, destino)
            custo = distancias[origem][destino]
        else:
            caminho, custo, tempo_execucao = algoritmo(grafo, origem, destino)

        print(f"----- {nome} -----")
        print(f"Caminho mínimo: {caminho}")
        print(f"Custo: {custo}")
        print(f"Tempo: {tempo_execucao:.6f} s")
        print("-------------------")
