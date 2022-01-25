#### Resumen de lo visto en funciones

A medida que los programas se vuelven más largos y complejos, necesitamos organizarlos adecuadamente.

Las funciones son muy útiles para agrupar código relevante, o código que cumple tareas repetitivas, por lo tanto es código reutilizable.

Por ello, cuando hablamos de una función, estamos hablando de una secuencia de comandos encapsulados que podemos usar donde queramos.


#### Crear de una función

    - def <nombreFuncion>(): si los necesitamos, pasar argumentos (argumento_1, argumento_2, ...)


```
    def saludar(nombre):
        print("Hola ", nombre)

    # Llamados a una función

    saludar("Jhon") 
    ## Hola Jhon
```
**Tenemos que tener cuidado que siempre que llamemos una función le agreguemos los paréntesis**

------------

Podemos crear una funcion con paso de argumentos opcionales, quiere decir que le definimos un valor por defecto al momento de crear el argumento

```
def argumentos_opcionales(nombre, edad, segundo_nombre=None, area_trabajo=None):
    pass
```

**Los argumentos opcionales siempre los dejamos para despues de aquellos que no serán tratados como opcionales**

* Es muy importante que sepamos que las funciones no reciben copias en los parámetros que le pasamos sino que reciben los propios argumentos.
Por ello tenemos que tener mucho cuidado cuando pasamos datos que son mutables podríamos estar sobreescribiendo una variable de fuera de la función y resulta que ello no era lo que buscabamos hacer.


## Paso de argumentos indeterminados
#### *args, **kwargs 

Está es una técnica de la que podemos dar uso para pasar una cantidad de argumentos indeterminados (tendrémos que administrarlas bien dentro de nuestra función).

Los *args dentro de la función los tratamos como tuplas, ya que así es como son tomados
```
    def llamar_a_lista(*args):
        print("Llamando a lista....")
        for nombre in args:
            print("-", nombre)

    llamar_a_lista("Juan", "Ana", "Benito", "Arturo" , "Melissa", "Julieta")
```

Los **kwargs dentro de la función los tratamos como diccionarios, ya que así es como son tomados.

Podemos pasarte tanto un diccionario de datos como argumento (**diccionario) ó, pasar los argumentos asignandoles valores al momento de pasarlos

```
    lista_de_datos_de_personas = []

    datos = {
        "nombre": "Arturo",
        "apellidos": "Pendragon",
        "identificacion": None
    }

    def guardar_datos_personas(**kwargs):
        lista_de_datos_de_personas.append(kwargs)

    guardar_datos_personas(**datos) # pasamos nuestro diccionario de datos
    datos = guardar_datos_personas(nombre="Gilgamesh", apellido="de Uruk", identificacion=None) # pasamos los datos como argumentos de clave=valor  

    print(lista_de_datos_de_personas)

```


Espero este resumen te ayude un poco... :)