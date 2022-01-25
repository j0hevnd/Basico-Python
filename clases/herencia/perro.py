from animal import Animal

class Perro(Animal):
    
    _tipo = __name__.lower() # Obtenemos el nombre de la clase
    
    def __init__(self, nombre, edad, amistoso:bool, max_energia, min_energia):
        super().__init__(nombre, edad, amistoso, max_energia, min_energia)
        self.energia = self._max_energia
        
    def alimentarse(self):
        return super().alimentarse(self.nombre)
    
    def tiene_hambre(self):
        if super().tiene_hambre():
            print(f"{self.nombre} tiene hambre...")
            print(self.alimentarse())
        self.amistoso = True
        print(f"{self.nombre} no tiene hambre")  
    
    def comunicarse(self):
        print(f"{self.nombre} esta ladrándo")
    
    def correr(self):
        self.energia -= 3
        self.amistoso = True
        print(f"{self.nombre} esta corriendo en el parque")

    def jugar(self):
        super().jugar()
        print(f"{self.nombre} esta trayendo la pelota")
        
    def dormir(self):
        return super().dormir(self._tipo)
        
    def __str__(self):
        return super().__str__(self._tipo, self.nombre, self.edad)