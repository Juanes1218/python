#REALIZAR UN PROGRAMA QUE USE UN DICCIONARIO PARA GESTIONAR LOS PRODUCTOS
#Y PRECIOS DE LA TABLA, DONDE SE LE PREGUNTE AL USUARIO POR UN PRODUCTO
#Y LA CANTIDAD. AL FINALIZAR MOSTRAR EN LA CONSOLA EL PRECIO TOTAL. SI
#EL PRODUCTO NO ESTA DEBE MOSTRAR UN MENSAJE INFORMANDO SOBRE ELLO

diccionario = {"portatiles": ("portatil1", "portatil2", "portatil3"),
               "Precios": (700000, 2500000, 8000000)}

print("Lista de portatiles")

print(diccionario)

producto = str (input("Ingrese el producto que desea de la lista anterior: "))
cantidad = int (input("Ingrese la cantidad que desea de este producto: "))
producto = producto.capitalize()
precioTotal = int


if producto in diccionario["portatiles"] :

    IndiceProducto = diccionario["portatiles"].index(producto)

    precioTotal = diccionario["Precios"][IndiceProducto]

    precioTotal = precioTotal * cantidad

    print(f"El precio total es de $",precioTotal,)

else:
    print("El producto no se encuentra.")
    