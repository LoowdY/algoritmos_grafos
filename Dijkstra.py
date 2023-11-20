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



#implementando funcao principal do algorimto djikstra
def dijkstra(grafo, inicio, fim):
    caminhos_mais_curtos = {inicio: (None, 0)}
    no_atual = inicio
    #lista com itens que não se repetem. Se dermos Type(visitados), ele retorna
    visitados = set()

    while no_atual != fim:
        visitados.add(no_atual)
        destinos = grafo[no_atual]
        peso_ao_no_atual = caminhos_mais_curtos[no_atual][1]

        for proximo_no in destinos:
            peso = grafo[no_atual][proximo_no] + peso_ao_no_atual
            if proximo_no not in caminhos_mais_curtos:
                caminhos_mais_curtos[proximo_no] = (no_atual, peso)
            else:
                peso_mais_curto_atual = caminhos_mais_curtos[proximo_no][1]
                if peso_mais_curto_atual > peso:
                    caminhos_mais_curtos[proximo_no] = (no_atual, peso)
        
        proximos_destinos = {no: caminhos_mais_curtos[no] for no in caminhos_mais_curtos if no not in visitados}
        if not proximos_destinos:
            return None
        no_atual = min(proximos_destinos, key=lambda k: proximos_destinos[k][1])

    caminho = []
    while no_atual is not None:
        caminho.append(no_atual)
        proximo_no = caminhos_mais_curtos[no_atual][0]
        no_atual = proximo_no
    caminho = caminho[::-1]
    return caminho

#criando uso do algormtio djikstra


'''

O grafo abaixo é o grafo em formato de dicionário abaixo. Observe que os numeros representam o peso associado com cada
conexão, não sendo cosiderados como nós.

'''
grafo = {
    'A': {'B': 1, 'C': 4},
    'B': {'E': 2, 'G': 5},
    'C': {'D': 2, 'H': 7},
    'D': {'E': 3, 'I': 6},
    'E': {'F': 2, 'J': 4},
    'F': {'K': 3},
    'G': {'H': 1},
    'H': {'I': 4},
    'I': {'J': 2},
    'J': {'K': 1, 'L': 3},
    'K': {'L': 2},
    'L': {'M': 3},
    'M': {'N': 4},
    'N': {'O': 2},
    'O': {}
}
inicio = 'A'
fim = 'O'
caminho = dijkstra(grafo, inicio, fim)
print("Caminho Dijkstra:", caminho)
