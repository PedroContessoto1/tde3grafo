import math
class GRAFO:
    def __init__(self):
        self.grafo = {}

    def adiciona_vertice(self, nome_vertice):
        if nome_vertice in self.grafo:
            print(f"Vertice {nome_vertice} ja existe")
        else:
            self.grafo[nome_vertice] = []

    def adiciona_aresta(self, vertice1, vertice2, peso):
        if self.tem_aresta(vertice1, vertice2):
            peso_ = self.peso(vertice1, vertice2)
            self.remove_aresta(vertice1, vertice2)
            self.grafo[vertice1].append([vertice2, peso_+1])
        else:
            self.grafo[vertice1].append([vertice2, peso])

    def remove_aresta(self, vertice1, vertice2):
        nova_lista = []
        if self.tem_aresta(vertice1, vertice2):
            for i in self.grafo[vertice1]:
                if i[0] != vertice2:
                    nova_lista.append(i)
            self.grafo[vertice1] = nova_lista
        else:
            print(f"Aresta entre {vertice1} -> {vertice2} não existe")

    def remove_vertice(self, vertice):
        if vertice not in self.grafo:
            print(f"Vertice {vertice} não existe")
        else:
            del self.grafo[vertice]

    def tem_aresta(self, vertice1, vertice2):
        if vertice1 not in self.grafo or vertice1 not in self.grafo:
            return False
        for i in self.grafo[vertice1]:
            if i[0] == vertice2:
                return True
        return False

    def peso(self, vertice1, vertice2):
        if self.tem_aresta(vertice1, vertice2):
            for i in self.grafo[vertice1]:
                if i[0] == vertice2:
                    return i[1]
        return f"Aresta entre {vertice1} -> {vertice2} não existe"

    def grau(self, vertice):
        if vertice in self.grafo:
            return len(self.grafo[vertice])
        return f"Vertice {vertice} não existe"

    def verificador_euleriano(self):
        eulerian = True
        for ver in self.grafo:
            if not self.grau(ver) % 2:
                eulerian = False
        return eulerian

    def imprime_lista_adjacencias(self):
        aresta = ""
        for key, value in self.grafo.items():
            for i in value:
                aresta += str(i) + " ->"
            print(f"{key} : {aresta}")
            aresta = ""

    def numero_vertices(self):
        return len(self.grafo.keys())

    def numero_arrestas(self):
        acc = 0
        for value in self.grafo.values():
            for i in value:
                acc += 1
        return acc

    def Dijkstra(self, start, end):
        dic_ = {key: math.inf for key in self.grafo if key != start}
        dic_[start] = 0
        visited = [start]
        acc = 0
        direcion = []
        best_direcion = [end]
        while end not in visited:
            for key, value in self.grafo[visited[acc]]:
                if key in visited:
                    continue
                new_distance = value + dic_[visited[acc]]
                if dic_[key] > new_distance:
                    direcion.append([visited[acc], key])
                    dic_[key] = new_distance
                visited.append(key)
            acc += 1
        end_word = end
        for i in direcion[::-1]:
            if end_word == i[1]:
                best_direcion.append(i[0])
                end_word = i[0]
        return dic_[end], best_direcion[::-1]
