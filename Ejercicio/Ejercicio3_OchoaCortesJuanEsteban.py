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

def verificar_y_procesar():
    nombre = int(input("Ingrese un número entre 1 y 1000: "))
    
    if nombre >= 1 and nombre <= 1000:
        proceso(nombre)

