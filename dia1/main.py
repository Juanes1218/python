##----------------------------
##---- EJERCICIO1 ----
##----------------------------
## IMPRESIÓN EN CONSOLA 
print("hola mundo") 

# ----DATOS PRIMITIVOS ----
# 1. String
Texto = "campus"
print(Texto)
# 2. Int
NumeroEntero = 3
print(NumeroEntero)
# 3. Double 
NumeroDecimalLargo = 3.123124313
print(NumeroDecimalLargo) 
# 4. Float 
Numerodecimal = 3.1
print(Numerodecimal) 
# 5. Boolean
booleano = True
print(booleano) 

# ----entradas parte del usuario -----
EntradaUsuario = input ("ingrese tu nombre")
numeroFinal = (EntradaUsuario)
print ("tu nombre es: ", numeroFinal)

# ----entradas partes del usuario con definicion de tipo de dato primitivo ----
EntradaUsuarioNumero = input ("ingrese tu edad")
numeroFinal = int(EntradaUsuarioNumero)
print ("tu edad es: ", EntradaUsuarioNumero) 

# ----ciclos -----

# ----ciclo for -----

for i in range (5,10,2): #for contador in range (desde, hasta, pasos)
    print(i)
    
# ----ciclo while ----

booleanito = False
while booleanito == True: #while condicion_a_cumplir:
    print("sigo vivo")
    booleanito = False 
    
# ----condicionales-----#

puntuacion=input("ingrese un numero")
masato = int (puntuacion) 

if masato > 100: 
    print ("puntuacion es mayor")

else:
    print ("no es mayor")



##----FUNCIONES----##

##----Con parametros y con retorno----##

def suma(a, b):
    return a + b

resultado_suma = suma(3, 5)
print(resultado_suma)


##----sin parametros y sin retorno----##

def saludar():
    print("¡Hola!")

saludar()


##----con parametros y sin retorno----##

def imprimir_multiplicacion(x, y):
    resultado = x * y
    print(f"El resultado es: {resultado}")

imprimir_multiplicacion(4, 6)

#----sin parametros y con retorno----##

def obtener_numero():
    return 42

resultado_numero = obtener_numero()
print(resultado_numero)

##----arreglos----##
numeros = [1, 2, 3, 4, 5]
primer_elemento = numeros[0]
ultimo_elemento = numeros[-1]
numeros[2] = 10
numeros.append(6)
print("Lista completa:", numeros)
print("Primer elemento:", primer_elemento)
print("Último elemento:", ultimo_elemento)


## DESAROLLADO POR JUAN ESTEBAN OCHOA CORTES - 1091358460