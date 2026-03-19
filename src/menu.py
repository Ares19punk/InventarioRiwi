def agregar_producto():
    print()
    print("|>--------1. Agregar producto------<|")
    print("|                                   |")
    nombre = input("| a. Digite el nombre de producto  \n| >  ")
    precio = float(input("| b. Digite el precio del producto\n| >  "))
    cantidad = float(input("| c. Digite la cantidad del producto\n| >  "))
    print("|                                    |")
    producto = {"nombre" : nombre, 
              "precio" : precio,
              "cantidad": cantidad}
    return producto

def mostrar_inventario(lista):
    print("|>--------2. Mostrar inventario----<|")
    print()
    for i, nombre in enumerate(lista):
        print(f" {i+1:<3}. Producto : {nombre["nombre"]:<12} | Precio : {nombre["precio"]:<8} | Cantidad : {nombre["cantidad"]:<5} | Total : 2{nombre["cantidad"]*nombre["precio"]}")
    print()

def calcular_estadistica(lista):
    suma = 0
    print("|>------3. Calcular estadistica----<|")
    num_producto = len(lista)
    for i, precio in enumerate(lista):
        suma = (precio["precio"]*precio["cantidad"]) + suma
    print("|                                   |")
    print("| a. Valor total del inventario:    |")
    print(f"|   > $ {suma:<8}                    |")
    print("| b. Cantidad total de productos:   |")
    print(f"|   > {num_producto:<3}                           |")
    print("-"*35)

print("Cantidad de productos registrados")
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

lista_inv = [
    {
        "nombre" : "Manzana", 
        "precio" : 1000,
        "cantidad": 5
    },
    {
        "nombre" : "Pera", 
        "precio" : 1500,
        "cantidad": 11
    }
]

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
                mostrar_inventario(lista_inv)
                pass
            case 3:
                calcular_estadistica(lista_inv)
                pass
            case 4:
                pass
    else:
        print("OPCIÓN INVALIDA. Vuelva a digitar la opción")