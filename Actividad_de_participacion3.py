from math import sqrt, pi
# Cree una clase Vehículo que contenga los atributos de instancia velocidad_maxima y kilometraje.

class Vehiculo:
    def __init__(self, velocidad_maxima, kilometraje):
        self.velocidad_maxima = velocidad_maxima
        self.kilometraje = kilometraje

# Cree una clase Punto que represente un punto en el plano cartesiano.

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def mostrar_coordenadas(self):

        print(f"({self.x}, {self.y})")

    def mover_coordenadas(self):

        x = int(input("Introduzca la nueva coordenada de x: "))
        y = int(input("Introduzca la nueva coordenada de y: "))

        self.x = x
        self.y = y

    def calcular_distancia(self):

        punto2_x = float(input("Ingrese la coordenada x del otro punto: "))
        punto2_y = float(input("Ingrese la coordenada y del otro punto: "))

        print(round(sqrt((punto2_x - self.x)**2 + (punto2_y - self.y)**2), 2))
    
# Cree una clase Rectángulo la cual contiene dos atributos de instancia que representan los puntos que definen sus esquinas. 
    
class Rectangulo:
    def __init__(self, punto1, punto2):
        self.esquina_superior_izquierda = punto1
        self.esquina_inferior_derecha = punto2

    def calcular_perimetro(self):
        base = abs(self.esquina_inferior_derecha[0] - self.esquina_superior_izquierda[0])
        altura = abs(self.esquina_inferior_derecha[1] - self.esquina_superior_izquierda[1])
        return 2 * (base + altura)

    def calcular_area(self):
        base = abs(self.esquina_inferior_derecha[0] - self.esquina_superior_izquierda[0])
        altura = abs(self.esquina_inferior_derecha[1] - self.esquina_superior_izquierda[1])
        return base * altura

    def es_cuadrado(self):
        base = abs(self.esquina_inferior_derecha[0] - self.esquina_superior_izquierda[0])
        altura = abs(self.esquina_inferior_derecha[1] - self.esquina_superior_izquierda[1])
        return base == altura

punto1 = (0, 0)
punto2 = (4, 3)
rectangulo = Rectangulo(punto1, punto2)

if rectangulo.es_cuadrado():
    print("El rectángulo es un cuadrado.")
else:
    print("El rectángulo no es un cuadrado.")

# Cree una clase Circulo que tenga las propiedades centro y radio

class Circulo:
    def __init__(self, centro : tuple, radio : float):
        self.centro = (0, 0)
        self.radio = 3

    def calcular_area(self):

        return (self.radio)**2 * pi

    def calcular_perimetro(self):

        return pi*(self.radio*2)
    
    def esta_en_circulo(self):

        x = float(input("Introduzca la coordenada del punto en x: "))
        y = float(input("Introduzca la coordenada del punto en y: "))

        if sqrt((x - self.centro[0])**2 + (y - self.centro[1])**2) <= self.radio:

            print("Las coordenadas introducidas están contenidas en el círculo.")

        else:
            print("Las coordenadas introducidas no están contenidas en el círculo.")

#Cree una clase Carta que contenga dos propiedades valor y pinta

class Carta:
    PINTAS = ('Corazones', 'Diamantes', 'Tréboles', 'Picas')

    def __init__(self, valor, pinta):
        self.valor = valor
        self.pinta = pinta

carta1 = Carta(10, 'Corazones')
carta2 = Carta(4, 'Picas')
carta3 = Carta(11, 'Diamantes')
