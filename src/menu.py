#------------------------------------------------------------------------------------
#1. Se implemento una funcion de interfaz de usuario que muestra un menu interactivo
#------------------------------------------------------------------------------------
def mostrar_menu():

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

#------------------------------------------------------------------------------------
#2. Se implemento funcion agregar producto para solicitar al usuario nombre, precio 
#   y cantidad. Almacena los 3 datos dentro de una lista con diccionarios de clave y 
#   valor y devuelve (return) un diccionario con las claves "nombre", "precio", "cantidad"
#------------------------------------------------------------------------------------
def agregar_producto():
    print()
    print("|>--------1. Agregar producto------<|")
    print("|                                   |")
    nombre = input("| a. Digite el nombre de producto  \n| >  ")
    precio = float(input("| b. Digite el precio del producto\n| >  "))
    cantidad = float(input("| c. Digite la cantidad del producto\n| >  "))
    print("|                                   |")
    producto = {"nombre" : nombre, 
              "precio" : precio,
              "cantidad": cantidad}
    return producto

#------------------------------------------------------------------------------------
#3. Se implemento funcion mostrar inventario usando bucle for para recorrer cada
#   posicion de la lista. Organiza las clave valor de los diccionarios en columnas
#------------------------------------------------------------------------------------
def mostrar_inventario(lista):
    print("|>--------2. Mostrar inventario----<|")
    print()
    for i, nombre in enumerate(lista):
        print(f" {i+1:<3}. Producto : {nombre["nombre"]:<12} | Precio : {nombre["precio"]:<8} | Cantidad : {nombre["cantidad"]:<5} | Total : 2{nombre["cantidad"]*nombre["precio"]}")
    print()

#------------------------------------------------------------------------------------
#4. Se implemento funcion calcular estadistica usando bucle for para recorrer la lista
#   y suma el costo de cada prodcuto. Se usa len(lista) para saber la cantidad de
#   referencia de prodcutos
#------------------------------------------------------------------------------------
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

#5. Se creo lista_inv para almacenar prdocutos
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

#6. Se usa bucle while para que el menu se repita hasta que el usuario decida salir
while option < 5:
    mostrar_menu()
#7. Se solicita opcion al usuario
    option = int(input("Digite la opción > "))
#8. Condicional if para validar la opcion que el usuario digite
    if option > 0 and option < 5:
        match option:
            case 1:
                #9. Se almacena en la variable "diccionario" el resultado de la funcion agregar producto
                diccionario = agregar_producto()
                #10. Se usa append para agregar a la lista el diccionario 
                lista_inv.append(diccionario)
                pass
            case 2:
                #11. Se invoca funcion mostrar_inventario y se le pasa como parametro "lista_inv" para que recorra dicha variable
                mostrar_inventario(lista_inv)
                pass
            case 3:
                #12. Se invoca funcion calcular_estadistica y se le pasa como parametro "lista_inv" para que trabaje sobre la lista
                calcular_estadistica(lista_inv)
                pass
            case 4:
                #13. Para salir del menu
                print("-"*35)
                print("Saliendo. Hasta pronto.....")
                break
    else:
        #14. caso tal el usuario digite una opción invalida le mostrara el siguiente msj
        print("OPCIÓN INVALIDA. Vuelva a digitar la opción")
    print("Volviendo al menú.....")
    print("2")