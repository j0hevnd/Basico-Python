# CLASES EN PYTHON

Hablar de un resumen de clases en Python, es pasar varias cosas por ensima.

Este resumen solo toca algo de lo fundamental de la Programación Orientada a Objetos en Python (POO)

Un paradigma de programación en Python es la POO, esta nos permite hacer 'moldes' de 'objetos' que consideramos reales y realizar 'copias' con sus propias carácteristicas, un ejemplo común es el de un molde de torta, todas las tortas hechas en este molde tienen las mismas caracteristicas, sin embargo cada una puede implementar sabores diferentes, colores diferentes, etc que lleve una torta...

Pues la POO hace esto, creamos una clase, le damos atributos y métodos propios que sean generales para quienes la usan, y ya con esto ¡¡¡tenemos nuestro molde (clase)!!!!....

Parece fácil :')

Python es un lenguaje orientado a objetos, si hacemos un type(variable) notamos que esta variable es de un tipo de dato que esta ligado a una clase. Es por este motivo que tenemos tantos métodos que podemos usar con nuestros datos, por ejemplo, con el tipo de dato 'str' tenemos los métodos .upper(), .lower(), .strip(), por nombrar algunos....
Es como si nuestras variables fueran objetos de estas clases, así es que pueden usar sus métodos

#### ¿Como estan estructuradas las clases?

*   <<\class>> es la palabra reservada para crear clases
*   el nombre de nuestra clase inicia con mayúscula, cuando es compuesta la siguiente tambien lleva mayúscula y no la separamos con guión bajo.
*   Las clases pueden 'tener atributos de clase' y 'metodos de clase que son los que se crean a un solo nivel de identación, y pueden tener variables de la instancia que son las que se crean al momento de crear un objeto de la clase o instancia (variable_instancia = Clase()), y estás estan definidas dentro de un método especial de la clase llamado __init__()

    - __init__() es el método que usamos para inicializar los atributos que son de la instancia.

Algo que necesitan nuestros métodos de clase (funciones) es el parámetro <<\self>>, este ayuda a nuestras instancias a acceder a los métodos y atributos de la clase, por ello debemos pasar este atributo a nuestros métodos de clase (este se puede llamar como queramos, pero por convención se le llama self).

Tambien podemos tener método y atributos 'privados' y 'protegidos' nos damos cuenta por ello gracias a los guiones bajos al inicio de la variable

    - _variable_protegida
    - __variable_privada

Tienen usos prácticos, pero no los cubriremos en este resumen :(

Veamos un ejemplo con la clase molde:

class MoldeTorta:
    
    def __init__(self, sabor, color, cant_azucar, tiempo_coccion):
        # Aquí dentro las variables que inician con el nombre self
        # son creadas como instancias de clase

        self.sabor = sabor
        self.color = color
        self.cant_azucar = cant_azucar
        self.tiempo_coccion = tiempo_coccion
        self.torta_cocinada = False


    # Hay mejores maneras de implementar los setter y getter dentro 
    # de Python, ero lo haremos así para el ejemplo
    def set_agregar_azucar(self, cant_azucar):
        """Añande azucar a la torta"""
        self.cant_azucar += cant_azucar
    
    def get_azucar(self):
        """ Envia la cantidad de azucar que tiene la torta"""
        return self.cant_azucar

    def get_torta_cocinada(self):
        return self.torta_cocinada
    
    
    # Caracteristicas de nuestra clase
    def cocinar_a(self, cant_grados):
        print(f"La torta esta a {cant_grados}° de cocción")
    
    def __tiempo_coccion(self):
        """
        Va disminullendo el tiempo de cocción
        Devulve el valor que tiempo que falte para la cocción
        """
        self.tiempo_coccion -= 1
        return self.tiempo_coccion

    def concinar_torta(self):
        """
        Va disminullendo el tiempo de coccion de la torta
        hasta que este lista, si se deja seguir, se quema la torta
        """
        tiempo = self.__tiempo_coccion()
        if tiempo == 0:
            print("La torta ya se quemo....")
            return False
        elif tiempo == 1:
            self.torta_cocinada = True
            print("La torta ya está")
        
        print("Torta cocinada: ", self.get_torta_cocinada())
    

### Creamos nuestro objeto o instancia de clase
 - torta = MoldeTorta("Vainilla", "Blanca", 4, 5)

### Invocamos los métodos de la clase
```
torta.cocinar_a(180)
torta.concinar_torta()
torta.concinar_torta()
torta.concinar_torta()
torta.concinar_torta()
torta.concinar_torta()
```