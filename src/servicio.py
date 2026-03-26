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
    print("| 4. Eliminar producto              |")
    print("| 5. Salir                          |")
    print("|                                   |")
    print("-"*37)

#------------------------------------------------------------------------------------
#2. Se implemento funcion agregar producto para solicitar al usuario nombre, precio 
#   y cantidad. Almacena los 3 datos dentro de una lista con diccionarios de clave y 
#   valor y devuelve (return) un diccionario con las claves "nombre", "precio", "cantidad"
#------------------------------------------------------------------------------------
def agregar_producto(lista):
    valido = False
    producto = None
    print()
    print("|>--------1. Agregar producto------<|")
    print("|                                   |")
    nombre = input("| a. Digite el nombre de producto  \n| >  ").capitalize()
    for i, list in enumerate(lista):
        if list["nombre"] == nombre:
            print("|                                   |")
            print("| > El prodcuto se encuentra        |")
            print("|   registrado                      |")
            print("|                                   |")
            valido = True
    if valido == False:

        precio = float(input("| b. Digite el precio del producto\n| >  "))
        cantidad = float(input("| c. Digite la cantidad del producto\n| >  "))
        print("|                                   |")
        producto = {"nombre" : nombre, 
                "precio" : precio,
                "cantidad": cantidad}
    else:
        pass
    return producto

#------------------------------------------------------------------------------------
#3. Se implemento funcion mostrar inventario usando bucle for para recorrer cada
#   posicion de la lista. Organiza las clave valor de los diccionarios en columnas
#------------------------------------------------------------------------------------
def mostrar_inventario(lista):
    print("|>--------2. Mostrar inventario----<|")
    print()
    for i, nombre in enumerate(lista):
        print(f" {i+1:<3}. Producto : {nombre["nombre"]:<12} | Precio : {nombre["precio"]:<8} | Cantidad : {nombre["cantidad"]:<5} | Total : {nombre["cantidad"]*nombre["precio"]}")
    print()

#------------------------------------------------------------------------------------
#4. Se implemento funcion calcular estadistica usando bucle for para recorrer la lista
#   y suma el costo de cada prodcuto. Se usa len(lista) para saber la cantidad de
#   referencia de prodcutos
#------------------------------------------------------------------------------------
def calcular_estadistica(lista):
    suma = 0
    cant = 0
    mayor_precio = 0
    nombre_precio_mayor = ''
    mayor_cantidad = 0
    name_cantidad_mayor = ''
    print("|>------3. Calcular estadistica----<|")
    num_producto = len(lista)
    for i, dic in enumerate(lista):
        suma = (dic["precio"]*dic["cantidad"]) + suma
        cant = (dic["cantidad"]) + cant

        if dic["precio"] > mayor_precio:
            mayor_precio = dic["precio"]
            nombre_precio_mayor = dic["nombre"]
        
        if dic["cantidad"] > mayor_cantidad:
            mayor_cantidad = dic["cantidad"]
            name_cantidad_mayor = dic["nombre"]
    
    print("|                                   |")
    print("| a. Valor total del inventario:    |")
    print(f"|   > $ {suma:<10}                  |")
    print("| b. Referencias total de productos:|")
    print(f"|   > {num_producto:<3}                           |")
    print("| c. Unidades totales en inv:       |")
    print(f"|   > {cant:<4}                          |")
    print("| b. Producto con mayor precio:     |")
    print(f"|   > Producto:   {nombre_precio_mayor:<10}        |")
    print(f"|   > Precio  : $ {mayor_precio:<10}        |")
    print("|                                   |")
    print("| c. Producto con mayor sotck:      |")
    print(f"|   > Producto:   {name_cantidad_mayor:<10}        |")
    print(f"|   > Cantidad:   {mayor_cantidad:<10}        |")
    print("-"*35)

#------------------------------------------------------------------------------------
#5. Se implemento funcion para eliminar posicion del inventario, usando bucle for para
#   encontrar el parametro digitado y eliminarlo con remove(posicion a eliminar)
#------------------------------------------------------------------------------------
def eliminar_producto(lista):
    print("-------------------------------------")
    print("|>-------5. Eliminar producto------<|")
    print("|                                   |")
    name = input("| a. Digite el nombre de producto  \n| >  ").capitalize()
    for i, nombre in enumerate(lista):
        if name == nombre["nombre"]:
            print("|                                   |")
            print("| > Prodcuto encontrado             |")
            print("|                                   |")
            print("|  ¿Está seguto de eliminar         |")
            print("|        el producto?               |")
            print("|       (SI)      (NO)              |")
            si_no = input("| > ").upper()
            print("                               |")
            if si_no == "SI":
                lista.remove(nombre)
            else:
                print("| > Producto no encontrado          |")
                print("|                                   |")
        else:
            pass
    print("| > Volviendo al menú               |")
    return lista

