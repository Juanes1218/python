
##------------MUTABLES---------##
##-----------------------------##




## [LISTAS]


print("lista")
print("")
Lista = [1,"tamo bien", 47, 6.98,"con o sin"]
print (Lista)
print("")
#-se pueden eleminar los elemntos o editar#
Lista.pop(0)
print (Lista)
print("")
#-Tambien se pueden añadir elementos#
Lista.append("billetes de cien")
print(Lista)


print("")
print("")


## {DICCIONARIO}


habitantes = {"casa1":"nadie","casa2":("juanita","pedro","kenia","os"),"casa3":"juan"}
print(habitantes)
print("")
##se pueden borrar posiciones
habitantes.pop("casa2")
print(habitantes)


##----------INMUTABLES---------##
##-----------------------------##


## "CADENAS"

#mi_cadena = "Hola, mundo!"

## Intentar cambiar un carácter en la cadena generará un error

#mi_cadena[0] = 'h'

## Para poder modificarla se debe hacer de esta forma

mi_cadena = "Hola, mundo!"
nueva_cadena = "h" + mi_cadena[1:]
print(nueva_cadena)



## (TUPLAS)

mi_tupla= ("1","2","3","hola","mundo")
print (mi_tupla)

# (una tupla no se puede modificar, solo leer y desempacar, por ejemplo)

print(mi_tupla[0:3])

