from grafos import Grafo

def exibir_menu():
    print("Menu:")
    print("1. Adicionar Aresta")
    print("2. Executar BFS")
    print("3. Executar DFS")
    print("4. Executar Dijkstra")
    print("5. Sair")

def main():
    grafo = Grafo()

    while True:
        exibir_menu()
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            u = input("Digite o primeiro vértice: ")
            v = input("Digite o segundo vértice: ")
            peso = int(input("Digite o peso da aresta: "))
            grafo.adicionar_aresta(u, v, peso)
        elif escolha == '2':
            inicio = input("Digite o vértice inicial para BFS: ")
            resultado = grafo.bfs(inicio)
            print("Resultado BFS:", resultado)
        elif escolha == '3':
            inicio = input("Digite o vértice inicial para DFS: ")
            resultado = grafo.dfs(inicio)
            print("Resultado DFS:", resultado)
        elif escolha == '4':
            inicio = input("Digite o vértice inicial para Dijkstra: ")
            resultado = grafo.dijkstra(inicio)
            print("Resultado Dijkstra:", resultado)
        elif escolha == '5':
            break
        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    main()
