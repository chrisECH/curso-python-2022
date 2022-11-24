class Coche:

    def __init__(self, marca, color, combustible, cilindrada):
        self.marca = marca
        self.color = color
        self.combustible = combustible
        self.cilindrada = cilindrada

    def mostrarCaracteristicas(self):
        print('Marca {}; Color: {}; Combustible: {}; Cilindrada: {}'.format(self.marca, self.color, self.combustible, self.cilindrada))

coche1 = Coche("Opel", "rojo", "gasolina", "1.6")


coche1.mostrarCaracteristicas()