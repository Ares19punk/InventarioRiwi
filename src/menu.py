
from servicio import mostrar_inventario, mostrar_menu, agregar_producto, calcular_estadistica, eliminar_producto, buscar_prodcuto, actualizar_producto

#1. Se creo lista_inv para almacenar prdocutos
lista_inv = [
    {
        "nombre" : "Manzana", 
        "precio" : 2000,
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
while option < 9:
    mostrar_menu()
#7. Se solicita opcion al usuario
    option = int(input("Digite la opción > "))
#8. Condicional if para validar la opcion que el usuario digite
    if option > 0 and option < 9:
        match option:
            case 1:
                #9. Se almacena en la variable "diccionario" el resultado de la funcion agregar producto
                diccionario = agregar_producto(lista_inv)
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
                #13. Se invoca funcion para eliminar producto por el nombre en especifico
                lista_inv = eliminar_producto(lista_inv)
                pass
            case 5:
                #14. Se invoca funcion para buscar producto dentro de la lista de diccionarios
                buscar_prodcuto(lista_inv)
                pass
            case 6:
                lista_inv = actualizar_producto(lista_inv)
            case 7:
                pass
            case 8:
                pass
            case 9:     
             #14. Para salir del menu
                print("-"*35)
                print("Saliendo. Hasta pronto.....")
                break
    else:
        #15. caso tal el usuario digite una opción invalida le mostrara el siguiente msj
        print("OPCIÓN INVALIDA. Vuelva a digitar la opción")
    print("Volviendo al menú.....")
    print("2")