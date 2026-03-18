def agregar_producto():
    print("|>--------1. Agregar producto------<|")
    print("|                                   |")
    nombre = input("| a. Digite el nombre de producto  \n| >  ")
    precio = float(input("| b. Digite el precio del producto\n| >  "))
    cantidad = input("| c. Digite la cantidad del producto\n| >  ")
    print("|                      m             |")
    lista = {"nombre" : nombre, 
              "precio" : precio,
              "cantidad": cantidad}
    return lista


print("-"*37)
print("|     Sistema de Inventarios Riwi   |")
print("-"*37)
print("|>--------------MENÚ---------------<|")
print("|                                   |")
print("| Opciones de sistema:              |")
print("|                                   |")
print("| 1. Agregar producto               |")
print("| 2. Mostrar inventario             |")
print("| 3. Calcular estadistica           |")
print("| 4. Salir                          |")
print("|                                   |")
print("-"*37)

lista_inv = []

option = 0
while option < 4:
    option = int(input("Digite la opción > "))
    if option > 0 and option < 4:
        match option:
            case 1:
                diccionario = agregar_producto()
                lista_inv.append(diccionario)
                pass
            case 2:
                pass
            case 3:
                pass
            case 4:
                pass
    else:
        print("OPCIÓN INVALIDA. Vuelva a digitar la opción")