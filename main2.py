import caminho_minimo
import matrizAdjacencias
import sys
import time  

def ler_grafo(nomeArquivo):
    with open(nomeArquivo, 'r') as arquivo:
        num_vertices, num_arestas = map(int, arquivo.readline().split())
        grafo = matrizAdjacencias.MatrizAdjacencias(num_vertices)
        
        for _ in range(num_arestas):
            origem, destino, peso = map(int, arquivo.readline().split())
            grafo.addAresta(origem, destino, peso)
        
    return grafo

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Uso correto: python main_caminho_minimo.py grafo.txt origem destino")
        sys.exit(1)
    
    nomeArquivo = sys.argv[1]
    origem = int(sys.argv[2])
    destino = int(sys.argv[3])

    # Carregar o grafo a partir do arquivo
    grafo = ler_grafo(nomeArquivo)

    print("\nProcessando...\n")
    for nome, algoritmo in [("Dijkstra", caminho_minimo.dijkstra), 
                            ("Bellman-Ford", caminho_minimo.bellman_ford),
                            ("Floyd-Warshall", caminho_minimo.floyd_warshall)]:
        
        # Medir o tempo de execução do algoritmo
        start_time = time.time()  # Tempo de início

        if nome == "Floyd-Warshall":
            distancias, predecessores, _ = algoritmo(grafo)
            caminho = caminho_minimo.reconstruir_caminho_floyd(predecessores, origem, destino)
            custo = distancias[origem][destino]
        else:
            caminho, custo, _ = algoritmo(grafo, origem, destino)

        end_time = time.time()  # Tempo de término
        tempo_execucao = end_time - start_time  # Tempo de execução

        print(f"----- {nome} -----")
        print(f"Caminho mínimo: {caminho}")
        print(f"Custo: {custo}")
        print(f"Tempo de execução: {tempo_execucao:.6f} s")  # Exibindo o tempo de execução
        print("-------------------")
