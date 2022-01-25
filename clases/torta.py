class MoldeTorta:
    
    def __init__(self, sabor, color, cant_azucar, tiempo_coccion):
        self.sabor = sabor
        self.color = color
        self.cant_azucar = cant_azucar
        self.tiempo_coccion = tiempo_coccion
        self.torta_cocinada = False

    # Hay mejores maneras de implementar los setter y getter dentro de Python
    # Pero lo haremos así para el ejemplo
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
    
    
torta = MoldeTorta("Vainilla", "Blanca", 4, 5)
torta.cocinar_a(180)
torta.concinar_torta()
torta.concinar_torta()
torta.concinar_torta()
torta.concinar_torta()
torta.concinar_torta()