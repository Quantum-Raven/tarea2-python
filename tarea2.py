productos = []

def añadir_producto():
    nombre = input('Introduce el nombre del producto: ')

    while True:
        try:
            precio = float(input('Introduce el precio del producto: '))
            break
        except ValueError:
            print('Por favor, introduce un número válido para el precio.')

    while True:
        try:
            cantidad = int(input('Introduce la cantidad del producto: '))
            break
        except ValueError:
            print('Por favor, introduce un número válido para el precio.')

    productos.append({'nombre': nombre, 'precio': precio, 'cantidad': cantidad})
    print(f'Producto "{nombre}" añadido correctamente')

    pass

def ver_productos():
    if productos:
        print('\nLista de productos:')
        for producto in productos:
            print(f'Nombre: {producto['nombre']}, Precio: {producto['precio']}, Cantidad: {producto['cantidad']} ')
    else:
        print('No hay productos guardados aún')

    pass

def actualizar_producto():
    nombre = input('Introduce el nombre del producto a actualizar: ')
    
    for producto in productos:
        if producto['nombre'].lower() == nombre.lower():
            print(f'Producto encontrado: {producto['nombre']}')
            nuevo_nombre = input(f'Nuevo nombre (deja vacío para no cambiar "{producto['nombre']}"): ')
            if nuevo_nombre:
                producto['nombre'] = nuevo_nombre

            while True:
                try:
                    nuevo_precio = input(f'Nuevo precio (deja vacío para no cambiar "{producto['precio']}"): ')
                    if nuevo_precio:
                        producto['precio'] = nuevo_precio
                        break
                except ValueError:
                    print('Por favor, introduce un número válido para el precio.')

            while True:
                try:
                    nueva_cantidad = input(f'Nueva cantidad (deja vacío para no cambiar "{producto['cantidad']}"): ')
                    if nueva_cantidad:
                        producto['cantidad'] = nueva_cantidad
                        break
                except ValueError:
                    print('Por favor, introduce un número válido para la cantidad.')

            print(f'Producto "{producto['nombre']}" actualizado correctamente.')
            return
        
    print('Producto no encontrado.')

    pass

def eliminar_producto():
    nombre = input('Introduce el nombre del producto a eliminar: ')
    
    for producto in productos:
        if producto['nombre'].lower() == nombre.lower():
            productos.remove(producto)
            print(f'Producto "{producto['nombre']}" eliminado correctamente')
            return
    
    print('Producto no encontrado.')

    pass

def guardar_datos():
    try:
        with open('productos.txt', 'a') as archivo:
            for producto in productos:
                archivo.write(f'{producto['nombre']}, {producto['precio']}, {producto['cantidad']}')
                
        print('Datos guardados correctamente.')

    except Exception as e:
        print(f'Ocurrió un error al guardar los datos: {e}')

    pass

def cargar_datos():
    try:
        with open('productos.txt', 'r') as archivo:
            for linea in archivo:
                nombre, precio, cantidad = linea.strip().split(', ')
                productos.append({'nombre': nombre, 'precio': float(precio), 'cantidad': int(cantidad)})

        print('Datos cargados correctamente.')

    except FileNotFoundError:
        print('No se ha encontrado el archivo')
    
    except Exception as e:
        print('Ocurrió un error al cargar los datos: {e}')

    pass

def menu():
    while True:
        print("1: Añadir producto")
        print("2: Ver productos")
        print("3: Actualizar producto")
        print("4: Eliminar producto")
        print("5: Guardar datos y salir")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            añadir_producto()
        elif opcion == '2':
            ver_productos()
        elif opcion == '3':
            actualizar_producto()
        elif opcion == '4':
            eliminar_producto()
        elif opcion == '5':
            guardar_datos()
            break
        else:
            print("Por favor, selecciona una opción válida.")

menu()