import heapq
from collections import deque, defaultdict

class Grafo:
    def __init__(self):
        self.grafo = defaultdict(list)
    
    def adicionar_aresta(self, u, v, peso=1):
        self.grafo[u].append((v, peso))
        self.grafo[v].append((u, peso))  # para grafo não direcionado
    
    def bfs(self, inicio):
        visitado = set()
        fila = deque([inicio])
        resultado = []

        while fila:
            no = fila.popleft()
            if no not in visitado:
                visitado.add(no)
                resultado.append(no)
                for vizinho, _ in self.grafo[no]:
                    if vizinho not in visitado:
                        fila.append(vizinho)
        
        return resultado
    
    def dfs(self, inicio):
        visitado = set()
        pilha = [inicio]
        resultado = []

        while pilha:
            no = pilha.pop()
            if no not in visitado:
                visitado.add(no)
                resultado.append(no)
                for vizinho, _ in self.grafo[no]:
                    if vizinho not in visitado:
                        pilha.append(vizinho)
        
        return resultado
    
    def dijkstra(self, inicio):
        distancias = {no: float('infinity') for no in self.grafo}
        distancias[inicio] = 0
        prioridade = [(0, inicio)]
        caminho = {}

        while prioridade:
            distancia_atual, no_atual = heapq.heappop(prioridade)

            if distancia_atual > distancias[no_atual]:
                continue

            for vizinho, peso in self.grafo[no_atual]:
                distancia = distancia_atual + peso

                if distancia < distancias[vizinho]:
                    distancias[vizinho] = distancia
                    heapq.heappush(prioridade, (distancia, vizinho))
                    caminho[vizinho] = no_atual
        
        return distancias

