class zona:
    def __init__(self, nombre, nivel) -> None:
        self.nombre = nombre
        self.nivel = nivel
        
    def __str__(self) -> str:
        return f'zona: {self.nombre} nivel: {self.nivel}'
    
    def __repr__(self) -> str:
        return f'zona: {self.nombre} nivel: {self.nivel}'
    
    def __lt__(self, o: object) -> bool:
        return self.nivel < o.nivel
    
    def __le__(self, o: object) -> bool:
        return self.nivel <= o.nivel
    
    def __gt__(self, o: object) -> bool:
        return self.nivel > o.nivel
    
    def __ge__(self, o: object) -> bool:
        return self.nivel >= o.nivel
    