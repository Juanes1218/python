##Secuencia fibonacci

def fibonacci_con_limite_usuario():
    limite = int(input("Ingrese el límite para la secuencia de Fibonacci: "))
    fib_sequence = [0, 1]
    
    while fib_sequence[-1] + fib_sequence[-2] <= limite:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    
    print(f"Secuencia de Fibonacci hasta el límite {limite}: {fib_sequence}")

    