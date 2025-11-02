
#---------------------------------------------------------
#-------------MENU----------------------------------------

def mostrar_menu():
    print("\n--- MENU DE PRODUCTOS ---")
    print("1. Buscar producto")
    print("2. Agregar producto")
    print("3. Modificar producto")
    print("4. Eliminar producto")
    print("5. Mostrar productos")
    print("6. Salir")

#---------------------------------------------------------

#cargar productos desde archivo para su LECTURA y ESCRITURA
def cargar_productos(Productos):
    productos = [] # lista vacia para almacenar productos
    try:
        with open(Productos, "r", encoding="utf-8") as f:
            for linea in f:
                partes = linea.strip().split(",") # quita espacios y divide por comas
                if len(partes) == 3:
                    productos.append({ 
                        "nombre": partes[0],
                        "precio": float(partes[1]),
                        "cantidad": partes[2]
                    })
    except FileNotFoundError:
        # Si el archivo no existe, se crea vacio
        with open(Productos, "w", encoding="utf-8"):
            pass
    return productos

def guardar_productos(Productos, productos):
    with open(Productos, "w", encoding="utf-8") as f:
        for p in productos:
            f.write(f"{p['nombre']};{p['precio']};{p['cantidad']}\n")


#---------------------------------------------------------

def buscar_producto(productos):
    nombre_buscar = input("Ingrese el nombre del producto a buscar: ").strip().lower()

    encontrado = False
    for p in productos:
        
        if p["nombre"].lower() == nombre_buscar:
            print("\n--- Producto encontrado ---")
            print(f"Nombre: {p['nombre']}")
            print(f"Precio: ${p['precio']:.2f}")
            print(f"Cantidad: {p['cantidad']}")
            encontrado = True
            break

    if not encontrado:
        print("\n No se encontro ningun producto con ese nombre.")

 #---------------------------------------------------------

 #AGREGAR PRODUCTO

def agregar_producto(productos, archivo):
    nombre = input("Ingrese el nombre del nuevo producto: ").strip()
    precio = float(input("Ingrese el precio: "))
    cantidad = input("Ingrese la cantidad: ")

    # Verificar si ya existe
    for p in productos:
        if p["nombre"].lower() == nombre.lower():
            print(" El producto ya existe.")
            return

    # Crear nuevo producto
    nuevo = {"nombre": nombre, "precio": precio, "cantidad": cantidad}
    productos.append(nuevo)

    # Guardar todo nuevamente en el archivo
    with open(archivo, "w", encoding="utf-8") as f:
        for p in productos:
            f.write(f"{p['nombre']},{p['precio']},{p['cantidad']}\n")

    print(f"Producto '{nombre}' agregado correctamente.")

    #---------------------------------------------------------
def modificar_producto(productos, archivo):
    nombre = input("Ingrese el nombre del producto a modificar: ").strip()

    for p in productos:
        if p["nombre"].lower() == nombre.lower():
            print(f"\nProducto encontrado: {p['nombre']}")
            print(f"Precio actual: {p['precio']}")
            print(f"Cantidad actual: {p['cantidad']}")

            nuevo_precio = input("Ingrese el nuevo precio (Enter para mantener): ").strip()
            nueva_cantidad = input("Ingrese la nueva cantidad (Enter para mantener): ").strip()

            # Actualiza solo si el usuario ingreso algo
            if nuevo_precio:
                try:
                    p["precio"] = float(nuevo_precio)
                except ValueError:
                    print(" Precio no valido, se mantiene el anterior.")

            if nueva_cantidad:
                p["cantidad"] = nueva_cantidad

            # Guardar todos los productos actualizados en el archivo
            with open(archivo, "w", encoding="utf-8") as f:
                for prod in productos:
                    f.write(f"{prod['nombre']},{prod['precio']},{prod['cantidad']}\n")

            print(f"\n Producto '{p['nombre']}' actualizado correctamente.")
            return  # Sale de la función

    # Si no encontró el producto
    print(f" No se encontro ningun producto con el nombre '{nombre}'.")

    #---------------------------------------------------------
#ELIMINAR PRODUCTO

def eliminar_producto(productos, archivo):
    nombre = input("Ingrese el nombre del producto a eliminar: ").strip()

    for p in productos:
        if p["nombre"].lower() == nombre.lower():
            print(f"\nProducto encontrado: {p['nombre']} (Precio: {p['precio']}, Cantidad: {p['cantidad']})")
            confirmar = input("Esta seguro que desea eliminarlo? (s/n): ").strip().lower()

            if confirmar == "s":
                productos.remove(p)

                # Guardar los cambios en el archivo
                with open(archivo, "w", encoding="utf-8") as f:
                    for prod in productos:
                        f.write(f"{prod['nombre']},{prod['precio']},{prod['cantidad']}\n")

                print(f"\n Producto '{nombre}' eliminado correctamente.")
            else:
                print("\n Operacion cancelada.")
            return  # Salir despues de encontrar el producto

    print(f"No se encontro ningun producto con el nombre '{nombre}'.")

#--------------------------------------
# MOSTRAR LISTADO COMPLETO DE PRODUCTOS
def mostrar_productos(productos):
    if not productos:
        print("\n No hay productos cargados.")
        return

    print("\n--- LISTADO DE PRODUCTOS ---") #los :<20 es para alinear a la izquierda con 20 espacios
    print(f"{'NOMBRE':<20}{'PRECIO':<10}{'CANTIDAD':<10}")
    print("-" * 40)
    for p in productos:
        print(f"{p['nombre']:<20}{p['precio']:<10.2f}{p['cantidad']:<10}")

    #-------------------------------------------------------
 #main siempre al final para que reconozca todas las funciones
def main():
    archivo = "Productos.txt"
    productos = cargar_productos(archivo)

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
             buscar_producto(productos)
        elif opcion == "2":
            agregar_producto(productos, archivo)
        elif opcion == "3":
            modificar_producto(productos, archivo)
        elif opcion == "4":
            eliminar_producto(productos, archivo)
        elif opcion == "5":
            mostrar_productos(productos)
        elif opcion == "6":
            print("Saliendo del programa...")
            break
        else:
            print("Opcion invalida, intente nuevamente.")

if __name__ == "__main__":
    main()