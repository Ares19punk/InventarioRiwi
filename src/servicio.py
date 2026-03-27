import csv

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
    print("| 5. Buscar producto                |")
    print("| 6. Actualizar prodcuto            |")
    print("| 7. Cargar inventario              |")
    print("| 8. Guardar inventario             |")
    print("| 9. Salir                          |")
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

#------------------------------------------------------------------------------------
#5. Se implementa funcion para encontrar un producto determinado a partir del nombre
#   suministrado por el usuario
#------------------------------------------------------------------------------------
def buscar_prodcuto(lista):
    valide = False
    print("-------------------------------------")
    print("|>--------6. Buscar producto-------<|")
    print("|                                   |")
    name = input("| a. Digite el nombre de producto  \n| >  ").capitalize()
    for i, nombre in enumerate(lista):
        if name == nombre["nombre"]:
            print("|                                   |")
            print("| > Producto encontrado:            |")
            print("|                                   |")
            print(f"|   > Producto:   {nombre["nombre"]:<10}        |")
            print(f"|   > Precio  : $ {nombre["precio"]:<10}        |")
            print(f"|   > Cantidad:   {nombre["cantidad"]:<10}        |")
            print("|                                   |")
            valide = True
    if valide == False:
        print("|                                   |")
        print("| > Prodcuto no encontrado...       |")
        print("|                                   |")
    else:
        pass

def actualizar_producto(lista):
    new_name = ''
    new_precio = 0
    new_cantidad = 0
    valido = False
    print("-------------------------------------")
    print("|>--------6. Buscar producto-------<|")
    print("|                                   |")
    name = input("| a. Digite el nombre de producto  \n| >  ").capitalize()
    for i, nombre in enumerate(lista):
        if name == nombre["nombre"]:
            print("|                                   |")
            print("| > Producto encontrado:            |")
            print("|                                   |")
            print(f"|   > Producto:   {nombre["nombre"]:<10}        |")
            print(f"|   > Precio  : $ {nombre["precio"]:<10}        |")
            print(f"|   > Cantidad:   {nombre["cantidad"]:<10}        |")
            print("|                                   |")
            print("|     ¿Que cambio desea hacer?      |")
            print("|                                   |")
            print("|    > Nombre de producto: (1)      |")
            print("|    > Precio de prodcuto: (2)      |")
            print("|    > Cantidad prdocuto : (3)      |")
            print("|    > Salir             : (4)      |")
            print("|                                   |")
            option = input("|    Digite la opción:            \n| >  ")
            if option == '1':
                print("|  a. Digite el nuevo nombre del    |")
                new_name = input("|     producto: \n| >  ").capitalize()
                nombre["nombre"] = new_name
                print("| > Nombre actualizado...           |")
                print("|                                   |")
                valido = True
            elif option == '2':
                print("|  a. Digite el nuevo precio del    |")
                new_precio = float(input("|     producto: \n| > $ "))
                nombre["precio"] = new_precio
                print("| > Precio actualizado...           |")
                print("|                                   |")
                valido = True
            elif option == '3':
                print("|  a. Digite la nueva cantidad de   |")
                new_cantidad = int(input("|     producto: \n| > $ "))
                nombre["precio"] = new_cantidad
                print("| > Cantidad actualizada...         |")
                print("|                                   |")
                valido = True
            elif option == '4':
                print("|                                   |")
                print("| > Saliendo de la opción...        |")
    if valido == False:
        print("|                                   |")
        print("| > Producto no encontrado...       |")
        print("|                                   |")
    return lista        

def guardar_csv(lista, seguro):

    if seguro == True:
        columnas = ["nombre","precio","cantidad"]

        print("|  ¿Está seguto de guardar         |")
        print("|      la información?             |")
        print("|       (SI)      (NO)             |")
        
        si_no = input("| > ").upper()
        if si_no == 'SI':
            
            with open('data/inventario.csv', 'w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=columnas)

                writer.writeheader()

                for producto in lista:
                    writer.writerow(producto)
            print("|                                   |")
            print("| > Se guardaron los cambios.       |")
        else:
            print("|                                   |")
            print("| > No se guardaron los cambios.    |")
            print("| > Volviendo al menú               |")
    else:
        print("|                                   |")
        print("| > Aún no se a cargado el inv      |")
        print("| > Por favor cargar el inv         |")
        print("| > Volviendo al menú               |")

def cargar_csv(lista, valido):
    nombre = ''
    precio = 0
    cantidad = 0
    if not lista:
        try:
            with open('data/inventario.csv', 'r', newline='') as file:
                reader = csv.DictReader(file)

                for i, fila in enumerate(reader):
                    nombre = fila["nombre"]
                    precio = float(fila["precio"])
                    cantidad = float(fila["cantidad"])

                    producto = {"nombre" : nombre, 
                    "precio" : precio,
                    "cantidad": cantidad}

                    lista.append(producto)
                
            print("|                                   |")
            print("| > Inventario cargado              |")
            print("|                                   |")
            valido = True

        except FileNotFoundError:
            print("|                                   |")
            print("| > Archivo no encontrado...        |")
            print("|                                   |")
        return lista
        return valido
    else:
        print("|                                   |")
        print("| > Ya se realizó el cargue         |")
        print("|                                   |")
    
    