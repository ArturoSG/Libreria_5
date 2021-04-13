from libro import Libro

class Libreria:
    def __init__(self):
        self.__libros = []

    def agregar_final(self, libro:Libro):
        self.__libros.append(libro)

    def agregar_inicio(self, libro:Libro):
        self.__libros.insert(0, libro)

    def mostrar(self):
        for libro in self.__libros:
            print(libro)

l01 = Libro(id=220304946, 
            origen_x=4, 
            origen_y=5, 
            destino_x=7, 
            destino_y=8, 
            velocidad=45,
            red=60,
            green=34,
            blue=75)
l02 = Libro(220508951, 6,9,8,5,4,8,60,42)
libreria = Libreria()
libreria.agregar_final(l02)
libreria.agregar_inicio(l01)
libreria.mostrar()