import matrizAdjacencias
import busca
import time
import sys

# cria um grafo a partir de um arquivo de labirinto:
def lerLabirinto(nomeArquivo):
    # Lê o arquivo do labirinto
    with open(nomeArquivo, 'r') as arquivo:
        labirinto = [linha.rstrip('\n') for linha in arquivo.readlines()]
    
    linhas = len(labirinto)
    colunas = max(len(linha) for linha in labirinto)
    mapa_vertices = {}
    contador_id = 0
    
    for i in range(linhas):
        for j in range(len(labirinto[i])):
            if labirinto[i][j] in [' ', 'S', 'E']:
                mapa_vertices[(i, j)] = contador_id
                contador_id += 1
    
    # Criar grafo com o número de vértices 
    grafo = matrizAdjacencias.MatrizAdjacencias(contador_id)
    
    posicao_inicio = None
    posicao_fim = None
    
    # Adicionar arestas entre células transitáveis adjacentes
    movimentos = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # direita, baixo, esquerda, cima
    
    for (i, j), id_vertice in mapa_vertices.items():
        if labirinto[i][j] == 'S':
            posicao_inicio = (i, j)
        elif labirinto[i][j] == 'E':
            posicao_fim = (i, j)
        
        # Explorar vizinhos
        for di, dj in movimentos:
            ni, nj = i + di, j + dj
            
            # Verificar se a célula adjacente é transitável
            if (ni, nj) in mapa_vertices:
                id_vizinho = mapa_vertices[(ni, nj)]
                grafo.addAresta(id_vertice, id_vizinho)
    
    if posicao_inicio is None or posicao_fim is None:
        raise ValueError("Labirinto deve conter pontos de início (S) e fim (E)")
    
    return grafo, mapa_vertices, posicao_inicio, posicao_fim

# Função para encontrar o caminho BFS
def encontrarCaminho(grafo, inicio_coord, fim_coord, mapa_vertices):
    if inicio_coord not in mapa_vertices or fim_coord not in mapa_vertices:
        return None
    
    inicio_id = mapa_vertices[inicio_coord]
    fim_id = mapa_vertices[fim_coord]
    
    # Usar a função bfs de busca.py
    caminho_ids = busca.bfs(grafo, inicio_id, fim_id)
    
    if caminho_ids:
        # Converter IDs
        mapa_inverso = {v: k for k, v in mapa_vertices.items()}
        caminho_coords = [mapa_inverso[id] for id in caminho_ids]
        return caminho_coords
    
    return None

if __name__ == "__main__":
    start = time.time()
    
    try:
        grafo, mapa_vertices, inicio, fim = lerLabirinto(sys.argv[1])
        caminho_coords = encontrarCaminho(grafo, inicio, fim, mapa_vertices)
        
        if caminho_coords:
            # Imprimir caminho no formato desejado
            caminho_str = " -> ".join([f"({i},{j})" for i, j in caminho_coords])
            print(caminho_str)
        else:
            print("Não foi possível encontrar um caminho.")
        
    except Exception as e:
        print(f"Erro: {e}")
        sys.exit(1)
    
    end = time.time()
    tempo_exe = end - start
    
    print(f"Tempo de execução: {tempo_exe:.10f} segundos")