'''
Alunos:
João Renan Santanna Lopes
Jefferson Dantas
João Matheus Severino
Rodrigo Cardoso
Data: 16/11/2023
Professor: Daniel Leal
Matéria: Teoria dos Grafos
OBS: a abstração foram as estações ferroviárias do Reino Unido.
'''

# Implementando função principal do algoritmo Dijkstra
# Implementando função principal do algoritmo Dijkstra
def dijkstra(grafo, inicio, fim):
    # Inicialização
    caminhos_mais_curtos = {inicio: (None, 0)}
    no_atual = inicio
    visitados = set()
    #faz laco ate o ultimo no do grafo
    while no_atual != fim:
        #adiciona visitados
        visitados.add(no_atual)
        
        destinos = grafo[no_atual]
        
        #adicioa caminho ao peso atual (peso para variavel)
        peso_ao_no_atual = caminhos_mais_curtos[no_atual][1]

        #indo para proximos nos
        for proximo_no in destinos:
            #adicionando peso dos nós
            peso = grafo[no_atual][proximo_no] + peso_ao_no_atual
            if proximo_no not in caminhos_mais_curtos or caminhos_mais_curtos[proximo_no][1] > peso:
                caminhos_mais_curtos[proximo_no] = (no_atual, peso)

        proximos_destinos = {no: caminhos_mais_curtos[no] for no in caminhos_mais_curtos if no not in visitados}
        if not proximos_destinos:
            return None

        no_atual = min(proximos_destinos, key=lambda k: proximos_destinos[k][1])

    caminho = []
    #parte do no final (no atual) ate o no inciial, por isso inverte-se a logica
    while no_atual is not None:
        caminho.append(no_atual)
        no_atual = caminhos_mais_curtos[no_atual][0]
    caminho = caminho[::-1]
    return caminho

# Grafo representando estações ferroviárias do Reino Unido
grafo = {
    'London': {'Birmingham': 1, 'Manchester': 4},
    'Birmingham': {'Leeds': 2, 'Liverpool': 5},
    'Manchester': {'Sheffield': 2, 'Bristol': 7},
    'Sheffield': {'Leeds': 3, 'Nottingham': 6},
    'Leeds': {'York': 2, 'Newcastle': 4},
    'York': {'Edinburgh': 3},
    'Liverpool': {'Bristol': 1},
    'Bristol': {'Nottingham': 4},
    'Nottingham': {'Newcastle': 2},
    'Newcastle': {'Edinburgh': 1, 'Glasgow': 3},
    'Edinburgh': {'Glasgow': 2},
    'Glasgow': {'Inverness': 3},
    'Inverness': {'Aberdeen': 4},
    'Aberdeen': {'Dundee': 2},
    'Dundee': {}
}

inicio = 'London'
fim = 'Dundee'
caminho = dijkstra(grafo, inicio, fim)
print("Caminho Dijkstra:", caminho)
