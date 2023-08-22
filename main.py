class Asiento:
    def __init__(self, color, precio, registro):
        self.color = color
        self.precio = precio
        self.registro = registro
        
    def cambiarColor(self, ncolor):
        if ncolor == "rojo" or ncolor == "amarillo" or ncolor == "verde" or ncolor == "negro" or ncolor == "blanco":
            self.color = ncolor
            
class Motor:
    def __init__(self, numeroCilindros, tipo, registro):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro
        
    def cambiarRegistro(self, nregistro):
        self.registro = nregistro
        
    def asignarTipo(self, ntipo):
        if ntipo == "electrico" or ntipo == "gasolina":
            self.tipo = ntipo
            
class Auto:
    cantidadCreados = 0
    def __init__(self, modelo, precio, asientos, marca, motor, registro,):
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos
        self.marca = marca
        self.motor = motor
        self.registro = registro
        
    def cantidadAsientos(self, asientos):
        cantidad = 0
        for i in range(len(asientos)):
            if asientos[i] != None:
                cantidad += 1
        return cantidad
            
    def verificarIntegridad(self, asientos):
        original = True
        for i in asientos:
            if asientos[i] != None and asientos[i].registro != self.registro:
                original = False
                break
        
        if self.registro != Motor.registro and self.motor != None:
            original = False
        
        if original == True:
            return "Auto original"
        else:
            return "Las piezas no son originales"