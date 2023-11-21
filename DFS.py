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

# Algoritmo DFS (Depth-First Search - Busca em Profundidade)
def busca_em_profundidade(grafo, inicio, visitados=None):
    if visitados is None:
        visitados = set()
    visitados.add(inicio)

    for vizinho in grafo[inicio]:
        if vizinho not in visitados:
            busca_em_profundidade(grafo, vizinho, visitados)
    return visitados

'''
Explicação do grafo. O Grafo a seguir foi implementado da seguinte maneira:
1 - Utilizou-se o formato de dicionário. Cada nó pai é uma chave do dicionário. Seus filhos, na mesma linha,
estão representados como elementos de uma lista (estrutura de dados do Python). Os filhos
e seus respectivos nós filhos são especificados nas linhas subsequentes como chaves do dicionário.
Por fim, vale citar que as chaves que não possuem filho, ou seja, possuem uma lista vazia como valor correspondente,
são as folhas da árvore binária.
'''

grafo = {
    'London': ['Birmingham', 'Manchester'],
    'Birmingham': ['Leeds', 'Liverpool'],
    'Manchester': ['Sheffield', 'Bristol'],
    'Leeds': ['York'],
    'Liverpool': ['Edinburgh', 'Glasgow'],
    'Sheffield': ['Nottingham'],
    'Bristol': ['Cardiff'],
    'York': ['Newcastle'],
    'Edinburgh': [],
    'Glasgow': ['Inverness'],
    'Nottingham': [],
    'Cardiff': [],
    'Newcastle': [],
    'Inverness': [],
}

# A partir do grafo acima, o usuário deve escolher qual nó buscar/visitar
visitados = busca_em_profundidade(grafo, 'London')

# Imprimindo na tela os caminhos (busca)
print("Nós visitados em DFS:", visitados)
