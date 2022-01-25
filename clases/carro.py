import time
from motor import Motor

class Carro:
    def __init__(self, motor, marca, modelo, color, cant_puertas):
        self.motor = motor
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.cantidad_puertas = cant_puertas
        
        
    def encender_motor(self):
        print("Motor encendido...")
        time.sleep(1)
    
    def acelerar(self):
        print("El coche esta acelerando...")
        time.sleep(2)
        
    def frenar(self):
        print("El coche esta frenando...")
        time.sleep(1)
        print("El coche se detuvo por completo")
        time.sleep(2)
    
    def __str__(self):
        return \
f"""
Marca: {self.marca}
Modelo: {self.modelo}
Color: {self.color}
Puertas: {self.cantidad_puertas}
Características de motor:
{self.motor.__str__()}
"""

#- Creamos objetos de tipo motor   
motor_1 = Motor("Diesel", 3.0)        
motor_2 = Motor("Eléctrico", 4.0)        

#- Creamos objetos de tipo carro
carro_1 = Carro(motor_1, "Nissan", "Juke Kiiro", "Negro", 4, 40)
carro_2 = Carro(motor_2, "Ford", "Bronco Raptor", "Gris", 4, 45)

print(carro_1)
time.sleep(1)
carro_1.encender_motor()
carro_1.acelerar()
carro_1.frenar()

print(carro_2)    