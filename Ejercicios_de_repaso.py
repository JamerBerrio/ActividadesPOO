from math import pi
import random
# 1. Crear un programa que pida al usuario ingresar su nombre y edad y los imprima en pantalla.

def programa1(nombre, edad):

    print(f"Tu nombre es {nombre} y tienes {edad} años.")

programa1(nombre="Andrés", edad=17) 

# 2. Escribir una función que calcule el área de un círculo dado su radio.

def area(radio):

    print(f"El área del circulo de radio {radio} es {round(pi * radio**2, 2)}")

area(radio=10)

# 3. Crear un programa que genere una lista de números aleatorios y los imprima en pantalla.

def numeros_aleatorios():
    numeros = list()
    for i in range(10):
        numero = random.randint(1, 100)
        numeros.append(numero)

    print(numeros)

numeros_aleatorios()

# 4. Escribir un programa que determine si un número dado es par o impar.

def par_o_impar(numero):

    if numero % 2 == 0:
        print("El número dado es par.")

    else:
        print("El número dado es impar.")

par_o_impar(8)

# 5. Crear una función que convierta grados Fahrenheit a grados Celsius.

def fahrenheit_a_celcius(temp_fahrenheit):

    celcius = (temp_fahrenheit - 32) / 1.8

    print(f"{temp_fahrenheit} ºF es igual a {round(celcius, 2)} ºC")

fahrenheit_a_celcius(120)

# 6. Crear un programa que calcule la suma de los números en una lista dada.

def suma_lista():
    resultado = 0
    lista = [1, 8, 88, 91, 14, 17, 21]
    
    for i in range(len(lista)):
        resultado += lista[i]

    print(resultado)

suma_lista()

# 7. Escribir un programa que encuentre el número más grande y el más pequeño en una lista dada.

def mayor_y_menor():
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    print(f"El menor número de la lista es {min(lista)} y el mayor número es {max(lista)}.")

mayor_y_menor() 

# 8. Crear una función que invierta el orden de los elementos en una lista dada

def invertir_listas():
    lista = ["Hola", "cómo", "estás"]
    lista_invertida = []
    iterador = 1
    for i in range(len(lista)):
        lista_invertida.append(lista[len(lista) - iterador])
        iterador += 1

    print(lista_invertida)    

invertir_listas()

# 9. Crear un programa que genere una matriz de números y la imprima en pantalla.

def matrices(filas, columnas):

    matriz = [[0 for i in range(columnas)] for i in range(filas)]

    for i in range(filas):
        for j in range(columnas):
            matriz[i][j] = random.randint(1, 100)

    for fila in matriz:
        print(fila)


matrices(3, 3)

# 10. Escribir una función que calcule el factorial de un número dado.

def factorial (y):
    x = int(y)
    resultado = x
    if x == 0:
        resultado = 1
    elif x>1:
        for iterador in range (x-1,1,-1):
            resultado = resultado * iterador
    return resultado    

print(factorial(5))

# 11. Crear un programa que genere una lista de números pares entre 1 y 100.

def lista_pares():
    pares = list()

    for i in range(0, 101, 2):
        pares.append(i)

    print(pares)

lista_pares()   

# 12. Crear un programa que imprima los números del 1 al 10 utilizando un ciclo for.

def numeros1Al10():
    for i in range(1, 11):
        print(i)

numeros1Al10()

# 13. Crear un programa que pida al usuario ingresar dos números y calcule su suma, resta, multiplicación y división.

def operaciones(n1, n2):
    print(f"{n1} + {n2} = {n1+n2}")
    print(f"{n1} - {n2} = {n1-n2}")
    print(f"{n1} x {n2} = {n1*n2}")
    print(f"{n1} / {n2} = {n1/n2}")

operaciones(5, 4)   

# 14. Escribir una función que calcule la media aritmética de una lista de números.

def media_aritmetica():

    lista_nums = [5, 7, 89, 44, 33, 22, 69]
    media = (sum(lista_nums)) / len(lista_nums)

    print(round(media, 2))

media_aritmetica()

# 15. Crear un programa que pida al usuario ingresar una cadena de texto y determine si es un palíndromo o no.

def palindromo(texto):

    reverso = "".join(reversed(texto))
    if texto == reverso:
        print("Es palíndromo.")

    else:
        print("No es palíndromo.")

palindromo("reconocer")