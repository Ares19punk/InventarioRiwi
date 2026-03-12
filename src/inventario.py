
#Captura de datos en consola
#Este bloque solicita la informacion basica del producto: nombre, precio unitario y cantidad

print("-"*35)
print("REGISTRO DE PRODUCTO: ")
print("-"*35)
# ---------------------------------------------------
# Parte 1: Captura del nombre del producto
# La función input() permite leer datos desde la consola
# ---------------------------------------------------
name_producto = input("Por favor digite el nombre del producto: ")
print("")
precio = 0
cantidad = 0
# ---------------------------------------------------
# Parte 2: Validación del precio del producto
# Se utiliza un ciclo while para asegurar que el usuario
# ingrese un valor numérico mayor que cero. 
# Se utiliza Try-except para evitar entradas no numericas
# ---------------------------------------------------

while precio <= 0:
    try:
        precio = float(input("Digite el valor unitario del producto: "))    
        if precio > 0:
            print("")
            print("Precio digidato correctamente. $",precio)
            print("")
        else:
            print("")
            print("Por favor vuelva a digitar el precio. Valor incorrecto")
            print("")
    except:
        print("Error de datos: solo se permite valores numericos")
# ---------------------------------------------------
# Parte 3: Validación de la cantidad del producto
# El ciclo while garantiza que la cantidad ingresada
# sea un número entero mayor que cero.
# Se utiliza Try-except para evitar entradas no numericas
# ---------------------------------------------------

while cantidad <= 0:
    try:
        cantidad = int(input("Por favor digite la cantidad del producto: "))
        if cantidad > 0:
            print("")
            print("Cantidad digidata correctamente. $",cantidad)
            print("")
        else:
            print("")
            print("Por favor vuelva a digitar la cantidad. Valor incorrecto")
            print("")
    except:
        print("Error de datos: solo se permite valores numericos")
# ---------------------------------------------------
# Parte 4: Calcular el valor total del prodcuto 
# multiplicando la cantidad por el precio unitario
# ---------------------------------------------------
costo_total = precio*cantidad

# ---------------------------------------------------
# Parte 5: Resumen de la información capturada y con
# su respectivo valor total del prodcuto
# ---------------------------------------------------

print("-"*35)
print("Resumen de información")
print("-"*35)
print("")
print(f"Nombre del producto: {name_producto} | Precio: {precio} | Cantidad: {cantidad} | Total: {costo_total}")

# ---------------------------------------------------
#Explicación del programa: 
# El programa permite registrar la información básica 
# de un producto desde la consola. Finalmente, el programa 
# calcula el costo total del producto multiplicando el 
# precio por la cantidad y muestra en pantalla un resumen con 
# toda la información


  
