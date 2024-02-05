##Secuencia fibonacci

def fibonacci_con_limite_usuario():
    limite = int(input("Ingrese el límite para la secuencia de Fibonacci: "))
    fib_sequence = [0, 1]
    
    while fib_sequence[-1] + fib_sequence[-2] <= limite:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    
    print(f"Secuencia de Fibonacci hasta el límite {limite}: {fib_sequence}")

##numero random
import random

def juego_adivinanza():
    secreto = random.randint(1, 100)
    numeroIntentos = 0

    while numeroIntentos < 10:
        try:
            numero = int(input("Ingresa un número entero: "))
            print(" ")
        except ValueError:
            print("")
            print("Debes ingresar un número entero.")
            print("")
            continue

        numeroIntentos += 1

        if numero == secreto:
            print("¡Felicitaciones, elegiste el número correcto!")
            print("")
            print("Hasta luego, espero que la pases bien.")
            print("")
            break

        elif numero < secreto:
            print("El número secreto es mayor.")
            print("")

        else:
            print("El número secreto es menor.")
            print("")

        if numeroIntentos == 10:
            print("Se te acabaron los intentos. Hasta luego.")

##money change 
def proceso(cantidad):
    monedas_10 = cantidad // 10
    print('number of coins of 10 = ',monedas_10)
    cantidad %= 10
    monedas_5 = cantidad // 5
    print('number of coins of 5 = ',monedas_5)
    cantidad %= 5
    monedas_1 = cantidad // 1
    print('number of coins of 1 = ',monedas_1)
    print('total amount of coins = ', monedas_10 + monedas_5 + monedas_1)
    print(monedas_10,'+',monedas_5,'+',monedas_1)
    return monedas_10, monedas_5, monedas_1
##funciones correctas

def negate(num):
   return -num
b= int(input())
neg_b= negate(b)
print ("b: ", b, "negate_b: ", negate)

def large_num(num):
   res = (num>10000)
   return res 
xde = large_num(b)
print ("b is big",xde)

