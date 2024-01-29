import random

print ("bienvenido a mi juego de adivinanza ")
print ("escoge un numero del 1 al 100, tienes 10 intentos para adivinar")
print ("te dare algunas pistas si vas mal")
print (" ")


secreto = random.randint(1,100)

numeroIntentos = 0

while numeroIntentos < 10: 
    try: 
        numero = int(input("ingresa un numero entero  ")) 
        print (" ") 
    except ValueError:
        print ("")
        print ("tienes que ingresar un numero entero")
        print ("")
        continue
    numeroIntentos += 1  
    
    if numero == secreto:
        print ("Felicitaciones, escogiste el numero correcto")
        print ("")
        print ("hasta luego, espero la pases bien")
        print ("")
    
    
    elif numero < secreto:
        print ("el numero es secreto es mayor")
        print ("")
    
    else:
        print ("el numero secreto es menor ")
        print ("")   
        
    if numeroIntentos == 10:
        print ("se te acabaron los intentos, hasta luego")
