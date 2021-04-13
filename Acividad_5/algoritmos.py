import math 

def distancia_euclidiana(x_1, y_1, x_2, y_2):
    cuadrado_x=(x_2-x_1)*(x_2-x_1)
    cuadrado_y=(y_2-y_1)*(y_2-y_1)
    suma_cuadrados = cuadrado_x+cuadrado_y
    distancia = math.sqrt(suma_cuadrados)
    return (distancia)