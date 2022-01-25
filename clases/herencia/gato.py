from animal import Animal

class Gato(Animal):
    
    _tipo = __name__.lower() # Obtenemos el nombre de la clase
    
    def __init__(self, nombre, edad, amistoso:bool, max_energia, min_energia):
        super().__init__(nombre, edad, amistoso, max_energia, min_energia)
        self.energia = self._max_energia
        
    def alimentarse(self):
        return super().alimentarse(self.nombre)
    
    def tiene_hambre(self, cazar=None):
        if super().tiene_hambre():
            print(f"{self.nombre} tiene hambre...")
            if not cazar:
                print(self.alimentarse())
                return
            return self.alimentarse()
        
        print(f"{self.nombre} no tiene hambre")    
    
    def comunicarse(self):
        print(f"{self.nombre} esta ñarriando")
    
    def jugar(self):
        super().jugar()
        print(f"{self.nombre} esta jugando con una bolita de plástico")
    
    def cazar(self):
        self.energia -= 1
        print(f"{self.nombre} está cazando...")
        comiendo = self.tiene_hambre("cazar")
        if comiendo:
            print(comiendo, "lo que cazo")
    
    def dormir(self):
        return super().dormir(self._tipo)
    
    def __str__(self):
        return super().__str__(self._tipo, self.nombre, self.edad)