

while True:

#Entrada de datos

    print("-"*35)
    print("REGISTRO DE PRODUCTO: ")
    print("-"*35)
    print("")
    nombre = input("DIGITE EL NOMBRE DEL PRODUCTO  : ")     
    precio = float(input("DIGITE EL PRECIO DEL PRODUCTO  : "))
    cantidad = int(input("DIGITE LA CANTIDAD DEL PRODUCTO: "))
    print("")
# Condicionales para un valor invalido, en caso tal se cumpla vovlera a solicitar la información.

    if precio < 0: 
        print("Información no valida. Vuelva a digitar el precio")

    elif cantidad < 0:
        print("Información invalida. Vuelva a digitar la cantidad")

    else:
        break
    

