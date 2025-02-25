import matrizAdjacencias
import listaAdjacencias
import info
import busca
import sys

# cria um grafo a partir de um arquivo:
def lerLabirinto(nomeArquivo):
    # Lê o arquivo do labirinto
    with open(nomeArquivo, 'r') as arquivo:
        labirinto = [linha.strip() for linha in arquivo.readlines()]
    
    linhas = len(labirinto)
    colunas = len(labirinto[0])
    
    # Mapeia células transitáveis para IDs de vértices
    mapa_vertices = {}
    contador_id = 0
    posicao_inicio = None
    posicao_fim = None
    
    for i in range(linhas):
        for j in range(colunas):
            if labirinto[i][j] != '#':  # Se não for parede
                mapa_vertices[(i, j)] = contador_id
                contador_id += 1
                
                if labirinto[i][j] == 'S':
                    posicao_inicio = (i, j)
                elif labirinto[i][j] == 'E':
                    posicao_fim = (i, j)
    
    # Cria o grafo
    grafo = matrizAdjacencias.MatrizAdjacencias(contador_id)
    
    # Adiciona arestas entre células adjacentes transitáveis
    movimentos = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # direita, baixo, esquerda, cima
    
    for (i, j), id_vertice in mapa_vertices.items():
        for di, dj in movimentos:
            ni, nj = i + di, j + dj
            
            # Verifica se a célula adjacente é válida e transitável
            if (0 <= ni < linhas and 0 <= nj < colunas and 
                labirinto[ni][nj] != '#' and 
                (ni, nj) in mapa_vertices):
                
                id_vizinho = mapa_vertices[(ni, nj)]
                grafo.addAresta(id_vertice, id_vizinho)
    
    return grafo, mapa_vertices, posicao_inicio, posicao_fim

# Adicione esta função ao arquivo main.py
def encontrarCaminho(grafo, inicio_id, fim_id):
    # Busca em largura para encontrar o caminho mais curto
    visitados = [False] * grafo.numVertices
    fila = [(inicio_id, [])]  # (vértice, caminho até ele)
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
    
    return None  # Não existe caminho

# Modifique o trecho final do main.py para:
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Número inválido de parâmetros! Argumentos esperados: main.py labirinto.txt")
        sys.exit(1)
    
    grafo, mapa_vertices, inicio, fim = lerLabirinto(sys.argv[1])
    
    # Encontrar IDs dos vértices inicial e final
    inicio_id = mapa_vertices[inicio]
    fim_id = mapa_vertices[fim]
    
    # Encontrar o caminho do início ao fim
    caminho_ids = encontrarCaminho(grafo, inicio_id, fim_id)
    
    if caminho_ids:
        # Converter IDs de volta para coordenadas
        mapa_inverso = {v: k for k, v in mapa_vertices.items()}
        caminho_coords = [mapa_inverso[id] for id in caminho_ids]
        
        # Imprimir caminho no formato desejado
        caminho_str = " ".join([f"({i},{j})" for i, j in caminho_coords])
        print(caminho_str)
    else:
        print("Não foi possível encontrar um caminho.")
    
    # Aqui você poderia usar o grafo para encontrar caminhos no labirinto
    # Por exemplo, usando BFS ou DFS para encontrar um caminho do início ao fim
    
    # grafo.printGrafo()

    '''print(f"Existe aresta entre 3 e 4? {grafo.possuiAresta(3,4)}")
    print(f"Existe aresta entre 3 e 1? {grafo.possuiAresta(3,1)}")

    print(f"Vizinhos de 3: {grafo.vizinhos(3)}")

    for i in range(grafo.numVertices):
        print(f"Vertice {i}: grau = {grafo.grau(i)}")

    print(f"Densidade = {info.densidade(grafo)}")

    print("Complemento do grafo:")
    complemento = info.complemento(grafo)
    complemento.printGrafo()

    print(f"Grafo completo? {info.completo(grafo)}")

    print(f"Grafo regular? {info.regular(grafo)}")

    vertices = [0, 2, 3]
    subgrafo = info.subgrafo(grafo, vertices)
    for i in range(subgrafo.numVertices):
        print(f"{vertices[i]} -> ", end=" ")
        for (j, p) in subgrafo.vizinhos(i):
            print(vertices[j], end=" ")
        print()
    
    busca.dfs(grafo, 2)
    busca.dfsIterativo(grafo, 3)
    busca.bfs(grafo, 1)'''