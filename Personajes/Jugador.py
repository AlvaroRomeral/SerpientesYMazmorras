class Jugador:
    def __init__(self, nombre, vida):
        self.nombre = nombre
        self.vida = vida

    def saludar(self):
        print(self.nombre+": Listo para luchar!")
