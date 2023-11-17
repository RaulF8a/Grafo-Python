class Nodo:
    def __init__(self, dato) -> None:
        self.__dato = dato

    @property
    def dato(self):
        return self.__dato
    
    def __str__(self) -> str:
        return f"{self.dato}"
    
    def __eq__(self, o: object) -> bool:
        return self.dato == o.dato
    
    def __hash__(self) -> int:
        return hash(self.dato)
    
    def __lt__(self, o:object) -> bool:
        return self.dato < o.dato