## Herencia

A veces tendremos clases que se relacionarán mucho, nos daremos cuenta que tiene varios atributos y métodos en común. Cuando algo como esto nos pasa, entonces podemos definir una clase que sea más generica y en esta clase agregamos estos métodos y atributos que comparten otras clases. Generalmente cuando esto pasa es porque las clases tienen algún tipo de relación, por ello la clase que tienen los métodos y atributos generales le llamamos clase Padre, y a las que heredan de esta clase les llamamos clases Hijas.

#### ¿Cómo se ve la herencia en Python?

Definimos nuestra clase y le al terminar, colocamo parentesís y dentro de estos la clase de la que haremos uso de sus métodos y/o atributos

Ejemplo:

```
class Animal: # clase padre
    pass

class Perro(Animal): # Esta clase hereda los atributos y comportamientos de la clase animal.
    pass
```