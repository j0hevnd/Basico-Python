class Animal:
    #- Las clases padre generalmente son clases genericas, quiere decir que la 
    #- información que contienen puede ser fácilmente adaptada por otras clases
    
    def __init__(self, nombre,  edad, amistoso:bool, max_energia, min_energia):
        self.nombre = nombre
        self.edad = edad
        self.amistoso = amistoso
        self._max_energia = max_energia
        self._min_energia = min_energia
        
    def correr(self):
        pass
    
    def alimentarse(self, nombre):
        self.amistoso = False
        self.energia = self._max_energia
        return f"{nombre} está comiendo"
    
    def tiene_hambre(self):
        return self.energia <= self._min_energia
    
    def comunicarse(self):
        self.energia -= 1
    
    def jugar(self):
        self.energia -= 2
        self.amistoso = True
    
    def dormir(self, tipo):
        print(f"El {tipo} está durmiendo")

    def __str__(self, tipo, nombre, edad):
        return f"==============\nNombre del {tipo} es: {self.nombre}\nEdad: {self.edad} años"
    
