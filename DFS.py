'''
Alunos:
João Renan Santanna Lopes
Jefferson Dantas
João Matheus Severino
Rodrigo Cardoso
Data: 16/11/2023
Professor: Daniel Leal
Matéria: Teoria dos Grafos
'''
#algoritmo DFS (depth - produnfidade).
def busca_em_profundidade(grafo, inicio, visitados=None):
    if visitados is None:
        #função set() vai randomizar so elementos, mas não os altera. Pode-se adicionar elementos caso queira.
        visitados = set()
    visitados.add(inicio)

    for vizinho in grafo[inicio]:
        if vizinho not in visitados:
            busca_em_profundidade(grafo, vizinho, visitados)
    return visitados




'''
Explicação do grafo. O Grafo a seguir foi implementado da seguinte maneira:
1 - Utilizou-se o farmto de dicionário. Cada nó pai é uma cahve do dicionário. Seus filhos, na mesma linha
estão representados como elementos de uma lista (estrutura de dados do python). Os filhos
e seus respectivos nós filhos são especificados nas linhas subsequentes como chaves do dicionário.
Por fim, vale citar que as chaves que não possuem filho, ou seja, possuem uma lista vazia como valor crrespondete,
são as folhas da árvore binária.



'''
grafo = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['H'],
    'E': ['I', 'J'],
    'F': ['K'],
    'G': ['L'],
    'H': ['M'],
    'I': [],
    'J': ['N'],
    'K': ['O'],
    'L': [],
    'M': [],
    'N': [],
    'O': []
}


#a partir do grafo acima, o usuário deve escolher qual nó buscar/visitar
visitados = busca_em_profundidade(grafo, 'A')

#impimindo na tela caminhos (busca)
print("Nós visitados em DFS:", visitados)
