import matrizAdjacencias
import listaAdjacencias
import info
import busca

# cria um grafo a partir de um arquivo:
def leitura(nomeArquivo):
    print("Implementar metodo leitura...")

if __name__ == "__main__":
    # grafo = matrizAdjacencias.MatrizAdjacencias(5)
    grafo = listaAdjacencias.ListaAdjacencias(5)

    grafo.addAresta(0, 1, 2)
    grafo.addAresta(0, 2, 4)
    grafo.addAresta(1, 4, 7)
    grafo.addAresta(3, 2, 6)
    grafo.addAresta(3, 4, 4)
    grafo.addAresta(4, 0, 3)
    grafo.addAresta(4, 3, 1)

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