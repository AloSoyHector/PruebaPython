import os
os.system("cls")
vesionprograma = 1.0

class Producto:
    def __init__(self, codigo, nombre, precio, categoria, stock):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria
        self.stock = stock

def mostrar_menu():
    print("==== Bienvenido a CaracolExpress ====")
    print("1. Registrar Productos")
    print("2. Buscar Producto")
    print("3. Listar Productos")
    print("4. Salir")

productos = []
def registrar_producto():
    codigo = (input)("Ingrese el codigo del producto: ")
    nombre = input("Ingrese el nombre del producto: ")
    categoria = input("Ingrese la categoria del producto: ")
    precio = int(input("Ingrese el precio del producto: "))
    stock = int(input("Ingrese la cantidad de stock del producto: "))
    if len(codigo) != 6:
        print("Error, ingrese el codigo correctamente [Debe tener exactamente 6 digitos]")
        return
    if len(nombre) <= 2 and len(nombre) <= 50:
        print("El nombre debe ser minimo de 2 a 50 caracteres")
        return
    if len(categoria) < 1:
        print("Ingrese una categoria valida [Paquete o Sobre]")
        return
    if precio < 0:
        print("Error, el precio debe ser mayor a cero")
        return
    if stock < 0:
        print("Debe ingresar un numero entero positivo")
        productos.append(Producto(codigo, nombre, categoria, precio, stock))
    print("Producto guardado correctamente.")

def buscar_producto():
    codigo = input("Ingrese el producto a buscar: ")
    for producto in productos:
        if producto == codigo:
            print(producto)
            return
    print("No se encontró ningun producto ingresado.")


def listar_producto():
    codigo = input("Ingrese el codigo del producto: ")

    
nombre_apellido = input("Ingrese su Nombre y Apellido: ")
while True:
    try:
        mostrar_menu()
        opcion = input("Ingrese una opción: ")
        if opcion == "1":
            registrar_producto()
        elif opcion == "2":
            buscar_producto()
        elif opcion == "3":
            listar_producto()
        elif opcion == "4":
            print(f"Don {nombre_apellido}, ha salido exitosamente del programa version {vesionprograma}")
            break
        else:
            print("Opción inválida. Intente nuevamente.")
    except:
        print("Ha ocurrido una excepcion del menu")