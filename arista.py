from nodo import Nodo

class Arista:
    def __init__(self, origen:Nodo, destino:Nodo) -> None:
        self.__par = [origen, destino]

    def getPair(self) -> list:
        return self.__par
    
    def __str__(self) -> str:
        return f"(Nodo: {self.getPair()[0]} ?-----Arista------(Nodo: {self.getPair()[1]})"

    def __eq__(self, o:Nodo) -> bool:
        return self.getPair()[0] == o.getPair()[0] and self.getPair()[1] == o.getPair()[1]
    
    def isDirected(self) -> bool:
        return False
    
    def isPonderated(self) -> bool:
        return True

#Arista no dirigida y no ponderada.
class AristaNoDirigida(Arista):
    def __init__(self, origen: Nodo, destino: Nodo) -> None:
        super().__init__(origen, destino)
    
    def isDirected(self) -> bool:
        return False
    
    def isPonderated(self) -> bool:
        return False
    
    def getOrigen(self) -> Nodo:
        return self.getPair()[0]
    
    def getDestino(self) -> Nodo:
        return self.getPair()[1]
    
    def __str__(self) -> str:
        return f"(Nodo: {self.getPair()[0]} <-----Arista------>(Nodo: {self.getPair()[1]})"

class Ponderada:
    def __init__(self, peso:int) -> None:
        self.__peso = peso
    
    @property
    def peso(self) -> int:
        return self.__peso

class AristaNoDirigidaPonderada(AristaNoDirigida, Ponderada):
    def __init__(self, origen: Nodo, destino: Nodo, peso:int) -> None:
        AristaNoDirigida.__init__(self, origen, destino)
        Ponderada.__init__(self, peso)
    
    def isPonderated(self) -> bool:
        return True
    
    def __str__(self) -> str:
        return f"(Nodo: {self.getPair()[0]} <-----{self.peso}------>(Nodo: {self.getPair()[1]})"
    
class AristaDirigidaPonderada(Arista, Ponderada):
    def __init__(self, origen: Nodo, destino: Nodo, peso:int) -> None:
        Arista.__init__(self, origen, destino)
        Ponderada.__init__(self, peso)
    
    def isPonderated(self) -> bool:
        return True
    
    def isDirected(self) -> bool:
        return True
    
    def getOrigen(self) -> Nodo:
        return self.getPair()[0]
    
    def getDestino(self) -> Nodo:
        return self.getPair()[1]
    
    def __str__(self) -> str:
        return f"(Nodo: {self.getPair()[0]} -----Arista {self.peso}------>(Nodo: {self.getPair()[1]})"
