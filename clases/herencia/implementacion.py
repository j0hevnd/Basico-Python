#%% importaciones

from perro import Perro
from gato import Gato

perro = Perro("Hachiko", 5, True, 6, 3)

print(f"¿Es amistoso {perro.nombre}? {perro.amistoso}" )
perro.correr()
perro.jugar()
perro.tiene_hambre()
perro.comunicarse()
perro.tiene_hambre()
perro.tiene_hambre()
perro.jugar()
perro.correr()
perro.correr()
perro.tiene_hambre()
print(f"¿Es amistoso {perro.nombre}? {perro.amistoso}" )
perro.dormir()
print()
print(perro)

print("=========================\n")
gato = Gato("Tom", 5, True, 5, 2)

gato.tiene_hambre()
gato.jugar()
gato.jugar()
gato.cazar()
gato.tiene_hambre()
gato.tiene_hambre()
gato.dormir()
print()
print(gato)
print("=========================")