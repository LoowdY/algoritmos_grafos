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

# Definição de função para busca em largura
def busca_em_largura(grafo, inicio, fim):
    #inicializa lista
    visitados = set()
    fila = [[inicio]]
    # Trabalhando-se em cima da estrutura de dados de fila
    while fila:
        caminho = fila.pop(0)
        no = caminho[-1]
        # Criando lógica por trás do algoritmo BFS
        # Busca em largura (filhos - filhos)
        if no not in visitados:
            vizinhos = grafo[no]
            #logica que ira visitar todos os visinhos andes de ir p/ prox. nivel
            for vizinho in vizinhos:
                novo_caminho = list(caminho)
                novo_caminho.append(vizinho)
                fila.append(novo_caminho)
                #fim: variavel que sera passada na utilização da funcao 
                if vizinho == fim:
                    return novo_caminho
            # Adiciona nó
            visitados.add(no)
    return None

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

# Definindo variável que será passada no parâmetro da função "busca_em_largura" como início
inicio = 'London'

# Definindo variável que será passada no parâmetro da função "busca_em_largura" como fim
fim = 'Edinburgh'

caminho = busca_em_largura(grafo, inicio, fim)

# Printando caminho como (nó inicial + nós + caminho +...+ nó final)
print("Caminho BFS:", caminho)
