from arista import Arista
from nodo import Nodo
from queue import PriorityQueue

class Grafo:
    def __init__(self) -> None:
        self.__aristas = []
        self.__ady = {}
    
    def agregarArista(self, arista:Arista) -> None:
        if arista not in self.__aristas:
            self.__aristas.append(arista)
    
    def __str__(self) -> str:
        return str([str(arista) for arista in self.__aristas])
    
    def eliminarArista(self, arista:Arista) -> None:
        self.__aristas.remove(arista)
    
    def getListaAdyacencia(self) -> dict:
        self.__ady.clear()

        for arista in self.__aristas:
            if arista.isDirected():
                n1 = arista.getOrigen()
                n2 = arista.getDestino()

                self.agregarDiccionario(n1, n2, arista.peso)

            else:
                n1 = arista.getOrigen()
                n2 = arista.getDestino()

                self.agregarDiccionario(n1, n2, arista.peso)
                self.agregarDiccionario(n2, n1, arista.peso)

        return self.__ady
    
    def imprimirListaAdyacencia(self) -> None:
        self.getListaAdyacencia()

        for key in self.__ady.keys():
            print(key, "---->",  end="")

            for value in self.__ady[key]:
                nodo = value[0]
                peso = value[1]
                print(f"[{nodo}, {peso}]", end="")
            
            print("\n")
    
    def agregarDiccionario(self, n1, n2, peso):
        if n1 in self.__ady:
            self.__ady[n1].append([n2, peso])
        else:
            self.__ady[n1] = [[n2, peso]]

    def algoritmoPrim(self, inicio:Nodo):
        grafoResultante = []
        visitados = []
        pq = PriorityQueue()

        visitados.append(inicio)

        for ady in self.__ady[inicio]:
            arista =(ady[1], inicio, ady[0])
            pq.put(arista)
        
        while not pq.empty():
            aristaActual = pq.get()

            destino = aristaActual[2]

            if destino not in visitados:
                visitados.append(destino)

                for ady in self.__ady[destino]:
                    if ady[0] not in visitados:
                        adyacente =(ady[1], destino, ady[0])
                        pq.put(adyacente)

                grafoResultante.append(aristaActual)
        
        return grafoResultante

    def makeSet(self) -> list:
        ds = []

        for nodo in self.__ady:
            ds.append([nodo])
        
        return ds
    
    def findSet(self, nodo,  ds:list) -> int:
        i = 0

        while i < len(ds):
            if nodo in ds[i]:
                return i
            
            i += 1
    
    def union(self, origen:Nodo, destino:Nodo, ds:list) -> None:
        i = self.findSet(origen, ds)
        j = self.findSet(destino, ds)

        listaOrigen : list = ds[i]
        listaDestino : list = ds[j]

        listaUnion = listaOrigen + listaDestino

        ds.remove(listaOrigen)
        ds.remove(listaDestino)

        ds.append(listaUnion)

    def algoritmoKruskal(self) -> list:
        grafoResultante = []
        ds = self.makeSet()
        lista = []

        for nodo, adyacentes in self.__ady.items():
            for ady in adyacentes:
                destino = ady[0]
                peso = ady[1]
                arista =(peso, nodo, destino)

                lista.append(arista)
            
        lista.sort(key=lambda arista:arista[0], reverse=True)

        while len(lista) > 0:
            arista = lista[-1]
            lista.pop()

            peso = arista[0]
            origenB = arista[1]
            destinoB = arista[2]

            if self.findSet(origenB, ds) != self.findSet(destinoB, ds):
                grafoResultante.append(arista)
                self.union(origenB, destinoB, ds)

        return grafoResultante

    def algoritmoDijkstra(self, inicio:Nodo):
        distancias = {}
        camino = {}
        pq = PriorityQueue()

        for nodo in self.__ady:
            if nodo == inicio:
                distancias[inicio] = 0
                camino[inicio] = inicio
            else:
                distancias[nodo] = 100000
                camino[nodo] = ""

        pq.put((0, inicio))

        while not pq.empty():
            nodo = pq.get()
            n = nodo[1]

            for arista in self.__ady[n]:
                distancia = arista[1] + nodo[0]
                destino = arista[0]

                if distancia < distancias[destino]:
                    distancias[destino] = distancia
                    camino[destino] = nodo
                    pq.put((distancia, destino))
        
        return distancias, camino
            