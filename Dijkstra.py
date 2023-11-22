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
def dijkstra(grafo, inicio, fim):
#inicialização
    #armazena caminho mais curto ente dois nos (none porque nao tem no anterior)
    caminhos_mais_curtos = {inicio: (None, 0)}
    
    #criacao da variavel de no atual 
    no_atual = inicio

    #cria-se uma lista pra implemntação de uma lista aletoria (set())
    #usando para controle dos nós visitados
    visitados = set()
#processamento
    #entra em loop até o no atual ser o no final (fim)
    while no_atual != fim:
        
        #quando visitado, e adicionado "marcado como visitado"
        visitados.add(no_atual
                      
        #pra cada nós vizinho o algorimto vai calcular o custo (soma dos pesos) do caminho de menor custo, passando pelo nó atual. 
        destinos = grafo[no_atual]
        
        #atribuindo peso ao nó atual
        peso_ao_no_atual = caminhos_mais_curtos[no_atual][1]

        #aqui deve-se escolher o nó de menor distância a ser visitado (vai mapear todos os caminhos e ao final esoclher o mais rápido - menor custo)
        for proximo_no in destinos:
            
            #incrementa-se o peso 
            peso = grafo[no_atual][proximo_no] + peso_ao_no_atual
            
            #criando logica de selecionar menor caminho
            if proximo_no not in caminhos_mais_curtos:
            
                caminhos_mais_curtos[proximo_no] = (no_atual, peso)
            
            else:
                
                peso_mais_curto_atual = caminhos_mais_curtos[proximo_no][1]
            
                if peso_mais_curto_atual > peso:
                    caminhos_mais_curtos[proximo_no] = (no_atual, peso)
        
        proximos_destinos = {no: caminhos_mais_curtos[no] for no in caminhos_mais_curtos if no not in visitados}
        
        if not proximos_destinos:
            return None
    '''
        função IMPORTANTE
        a função min() é chamada com a função lambda (função anônima). Basicamente,
        key-lambda k: proximos_destinos[k][1] tem o objetivo de se utilizar da min() p/ escolher
        nó com menor distância acumulada entre aqueles que ainda não foram visitados.
        
    '''   
        no_atual = min(proximos_destinos, key=lambda k: proximos_destinos[k][1])

    caminho = []
'''
alcança o no fim no loop anteiror.
aqui inicia uma listagem do no final ao no inifical e depois a variavel caminho vai inverter a logica, ja que se iniciou
no final e se quer printar o processos desde o inicio para o fim, e não do fim ao inicio.
'''
while no_atual is not None:
        caminho.append(no_atual)
        proximo_no = caminhos_mais_curtos[no_atual][0]
        no_atual = proximo_no
    caminho = caminho[::-1]
    return caminho

# Criando uso (aplicação/abstração) do algoritmo Dijkstra

'''
O grafo abaixo representa estações ferroviárias do Reino Unido. Os números representam o peso associado com cada
conexão, não sendo considerados como nós.
'''
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
