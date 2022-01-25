
# Haremos un CRUD (Create, Read, Update, Delete) de equipos tecnologicos
# usando una variable para tener allí los datos

# Variable donde guardamos la información
equipos = "" 

def listar_equipos():
    """ 
    Lista todos los equipo de equipos
    """
    global equipos
    print("Lista:\n",equipos, "\n")


def guardar_equipo(equipo=None):
    global equipos             
    """
    Agregar equipo nuevo
    Args:
        equipo (string): equipo a agregar
    """
    
    #- try, except nos ayuda para atrapar errores así 
    #- los podremos administrar correctamente
    try: 
        if equipos is None:
            return "pasaste ningún nombre de equipo a agregar"
        elif len(equipos) == 0:
            equipos += equipo
        else:
            equipos += "," + equipo
            
        print("Añadido")
        return listar_equipos()
    except Exception: # 'Exception' atrapa todas las excepciones
        print("No pasaste un argumento correcto")
        return False


def guardar_equipo_argumentos(*equipos_informaticos, **kwargs): # *tupla, **diccionario
    """
    Añadimos una tupla, lista o diccionario de equipos 
    (*El diccionario no lo estamos usando, solo fue para el ejemplo)
    """
    global equipos
    equipos = ','.join(equipos_informaticos)
    print("Añadidos")
    return listar_equipos()


def actualizar_equipo(equipo_actualizar, equipo_nuevo):
    """
    Actualiza el nombre con el que se añadio un equipo
    Args: 
        equipo_actualizar (string): equipo a actualizar
        equipo_nuevo (string): nuevo equipo
    """
    global equipos
    
    if equipo_actualizar in equipos:
        equipos = equipos.replace(equipo_actualizar, equipo_nuevo)
        print(f"**** '{equipo_actualizar}' actualizado correctamente a '{equipo_nuevo}' ****")
        
        # llamamos a nuestra función listar 
        # para ver todos los cambios realizados
        return listar_equipos()
    else:
        print("La equipo no esta en la lista")


def eliminar_equipo(equipo):
    """
    Elimina un equipo 
    Args: equipo (string): equipo a eliminar
    """
    global equipos
    
    lista_equipos = equipos.split(',')
    if equipo not in lista_equipos:
        print("El equipo no está en la lista")
        return
    
    lista_equipos.remove(equipo)
    equipos = ','.join(lista_equipos)
    print(f"**** {equipo} fue removido correctamente ****")
    return listar_equipos()


# Este es el entrypoint, así lo que se encuentra dentro de esta condición solo se ejecuta
# en caso de sea llamdado directamente este modulo, no se ejecuta si el modulo es llamado
# desde otro lugar (Como cuando importamos)
if __name__ == "__main__":
    
    guardar_equipo("Adaptador")
    guardar_equipo("HDMI")
    guardar_equipo_argumentos("Adaptador","Monitor", "Torre", "Teclado", "Mouse", equipo='Juan', apellido='Gonzales')
    actualizar_equipo("Adaptador", "Adaptador HDMI/VGA")
    eliminar_equipo("Adaptador HDMI/VGA")
    # eliminar_equipo("Adaptador")