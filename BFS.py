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

#definição de função para busca em largura
def busca_em_largura(grafo, inicio, fim):
    visitados = set()
    fila = [[inicio]]
    #trabalhando-se em cima da estrutura de dados de fila
    while fila:
        caminho = fila.pop(0)
        no = caminho[-1]
        #criando logica por tras do algoritmo BFS
        #busca em largura ( filhos - filhos)
        if no not in visitados:
            vizinhos = grafo[no]
            for vizinho in vizinhos:
                novo_caminho = list(caminho)
                novo_caminho.append(vizinho)
                fila.append(novo_caminho)
                if vizinho == fim:
                    return novo_caminho
            #adiciona nó
            visitados.add(no)
    return None



'''
Explicação do grafo. O Grafo a seguir foi implementado da seguinte maneira:
1 - Utilizou-se o formato de dicionário. Cada nó pai é uma cahve do dicionário. Seus filhos, na mesma linha
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

# Definindo variável que será passada no parâmetro da função "busca_em_largura" como início
inicio = 'A'

# Definindo variável que será passada no parâmetro da função "busca_em_largura" como fim
fim = 'O'

caminho = busca_em_largura(grafo, inicio, fim)

# Printando caminho como (nó inicial + nós + caminho +...+ nó final)
print("Caminho BFS:", caminho)
