print("Hola, bienvenido a mi software acerca de la secuencia de finobacci")

repetirCodigo = True

while repetirCodigo == True:
    numeron = input("Escribe un numero entero para establecer el fin de la secuencia ") 
numeroFinal = int(numeron)

print("Vale, a continuaciòn te pedire dos numeros enteros para poder comenzar con la secuencia ")

numeroxde = input("numero1 # ")
numero1 = int(numeroxde)

numeroxdee = input("numero2 # ")
numero2 = int(numeroxdee)

numerosuma = numero1+numero2
numero3 = int(numerosuma)

while numero2<numeroFinal:
    numero3 = numero1+numero2
    numero1 = numero2
    numero2 = numero3
    print (numero2)
    
respuesta = input ("¿deseas repetir el programa? si/1, no/0 ")

