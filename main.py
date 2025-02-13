import matrizAdjacencias
import listaAdjacencias
import info
import busca
import sys

# cria um grafo a partir de um arquivo:
def leitura(nomeArquivo):
    arquivo = open(nomeArquivo)

    str = arquivo.readline()
    str = str.split(" ")
    numVertices = int(str[0])
    numArestas = int(str[1])

    grafo = listaAdjacencias.ListaAdjacencias(numVertices)
    # grafo = matrizAdjacencias.MatrizAdjacencias(numVertices)

    for i in range(numArestas):
        str = arquivo.readline()
        str = str.split(" ")
        origem = int(str[0])
        destino = int(str[1])
        peso = int(str[2])
        grafo.addAresta(origem, destino, peso)

    return grafo

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Numero invalido de parametros! Argumentos esperados: main.py grafo.txt")
        sys.exit(1)

    # sys.argv[1] contem o nome do arquivo a ser lido
    grafo = leitura(sys.argv[1])

    grafo.printGrafo()

    print(f"Existe aresta entre 3 e 4? {grafo.possuiAresta(3,4)}")
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
    busca.bfs(grafo, 1)