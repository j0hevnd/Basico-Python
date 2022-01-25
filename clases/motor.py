class Motor:
    def __init__(self, tipo_motor, cilindros):
        self.tipo_motor = tipo_motor
        self.cilindros = cilindros
        
    def get_tipo_motor(self):
        return self.tipo_motor
        
    def get_cilindros(self):
        return self.cilindros
    
    def __str__(self):
        return f"-  Tipo motor: {self.tipo_motor}\n-  Cilindros: {self.cilindros}"