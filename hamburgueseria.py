hamburguesas = {"Hamburguesa Roja": 1, "Hamburguesa Verde": 1, "Hamburguesa Blanca": 1, "Hamburguesa Amarilla": 1, "Hamburguesa Azul": 1, "Hamburguesa Naranja": 1, "Hamburguesa Violeta": 1, "Hamburguesa Celeste": 1, "Hamburguesa Rosada": 1, "Hamburguesa Negra": 1}

hamburguesa_roja = {'Pan de hamburguesa': 1, '200 gramos de carne': 1, 'Tomate': 1, 'Lechuga': 1, 'Queso Cheddar': 1, 'Bacon': 1, 'Cebolla': 1, 'Mostaza': 1, 'Mayonesa': 1}
hamburguesa_verde = {'Pan de hamburguesa': 1, '200 gramos de carne': 1, 'Huevo': 1, 'Queso Mozzarella': 1, 'Champiñones': 1, 'Perejil': 1, 'Salsa Barbacoa': 1, 'Pepinillos': 1, 'Mayonesa': 1}
hamburguesa_blanca = {'Pan de hamburguesa': 1, '200 gramos de carne': 1, 'Queso Azul': 1, 'Tomate': 1, 'Lechuga': 1, 'Ketchup': 1, 'Cebolla': 1, 'Mayonesa': 1}
hamburguesa_amarilla = {'Pan de hamburguesa': 1, '200 gramos de carne': 1, 'Mostaza': 1, 'Queso Cheddar': 1, 'Bacon': 1, 'Pepinillos': 1, 'Huevo': 1, 'Champiñones': 1, 'Mayonesa': 1}
hamburguesa_azul = {'Pan de hamburguesa': 1, '200 gramos de carne': 1, 'Salsa Barbacoa': 1, 'Lechuga': 1, 'Queso Mozzarella': 1, 'Tomate': 1, 'Cebolla': 1, 'Perejil': 1, 'Mayonesa': 1}
hamburguesa_naranja = {'Pan de hamburguesa': 1, '200 gramos de carne': 1, 'Mostaza': 1, 'Queso Azul': 1, 'Cebolla': 1, 'Bacon': 1, 'Champiñones': 1, 'Pepinillos': 1, 'Mayonesa': 1}
hamburguesa_violeta = {'Pan de hamburguesa': 1, '200 gramos de carne': 1, 'Ketchup': 1, 'Lechuga': 1, 'Huevo': 1, 'Queso Mozzarella': 1, 'Tomate': 1, 'Salsa Barbacoa': 1, 'Mayonesa': 1}
hamburguesa_celeste = {'Pan de hamburguesa': 1, '200 gramos de carne': 1, 'Cebolla': 1, 'Queso Cheddar': 1, 'Perejil': 1, 'Bacon': 1, 'Tomate': 1, 'Mayonesa': 1}
hamburguesa_rosada = {'Pan de hamburguesa': 1, '200 gramos de carne': 1, 'Pepinillos': 1, 'Lechuga': 1, 'Champiñones': 1, 'Queso Mozzarella': 1, 'Mostaza': 1, 'Cebolla': 1, 'Mayonesa': 1}
hamburguesa_negra = {'Pan de hamburguesa': 1, '200 gramos de carne': 1, 'Salsa Barbacoa': 1, 'Queso Azul': 1, 'Tomate': 1, 'Bacon': 1, 'Huevo': 1, 'Mayonesa': 1}

set_Roja = set(hamburguesa_roja.keys())
set_verde = set(hamburguesa_verde.keys())
set_blanca = set(hamburguesa_blanca.keys())
set_amarilla = set(hamburguesa_amarilla.keys())
set_azul = set(hamburguesa_azul.keys())
set_naranja = set(hamburguesa_naranja.keys())
set_violate = set(hamburguesa_violeta.keys())
set_celeste = set(hamburguesa_celeste.keys())
set_rosada = set(hamburguesa_rosada.keys())
set_negra = set(hamburguesa_negra.keys())

menu_principal = ['Ver el menú de la casa', 
                  'Elección de una hamburguesa',
                  'Unir hamburguesas', 
                  'Ingredientes que tienen en común las hamburguesas', 
                  'Ingredientes exclusivos de cada hamburguesa', 
                  'Comparar hamburguesas', 
                  'Buscar una hamburguesa por ingrediente', 
                  'Eliminar ingredientes', 
                  'Elegir una hamburguesa aleatoriamente', 
                  'Salir']

eleccion_cliente = []
carrito = {}

def mostrar_menu(menu):
    for i, comida in enumerate(menu, start = 1):
        print(f'{i}. {comida}')

def mostrar_menu_hamburguesa(menu):
    for i, (comida, precio) in enumerate(menu.items(), start = 1):
        print(f'{i}. {comida}: {precio}')

def cantidad_comida(opcion, cantidad, menu, carrito):
    # Verificar si la opción está en el menú
    comida_elegida = None
    for comida, indice in menu.items():
        if indice == opcion:
            comida_elegida = comida
            break

    if comida_elegida:
        # Multiplicar la cantidad de la comida por la cantidad deseada
        total = {comida_elegida: cantidad}
        # Agregar al carrito
        carrito.update(total)
        print(f"{cantidad} x {comida_elegida} ha sido añadido al carrito.")
    else:
        print("Opción no válida. Por favor, elige una hamburguesa válida del menú.")

def agregar_carrito(opcion, eleccion_menu):
    menu_comida = list(eleccion_menu.keys())
    eleccion_comida = menu_comida[opcion - 1]
    carrito.update({eleccion_comida: eleccion_menu[eleccion_comida]})

print()
print('*** HAMBURCOLORS ***\n')
print('¡Bienvenido a nuestra hamburgueseria!')
print('Ofrecemos una amplia variedad de hamburguesas deliciosas')
print('Ofrecemos la oportunidad de personalizar tu propia hamburguesa')
print('¡Esperamos que disfrutes de tu comida con nosotros!\n')

print('Menú principal\n')

mostrar_menu(menu_principal)
opcion = input('Ingrese una opcion: ')
print()

if opcion == '1':
    print('*** Menú de la Casa ***\n')
    mostrar_menu(hamburguesas)
    opcion_hamburguesa = int(input('Seleccione una opcion para ver los ingredientes: '))
    if opcion_hamburguesa == 1:
        print()
        print('Los ingredientes de la Hamburguesa Roja son:\n')
        mostrar_menu(list(hamburguesa_roja))
    elif opcion_hamburguesa == 2:
        print()
        print('Los ingredientes de la Hamburguesa Verde son:\n')
        mostrar_menu(list(hamburguesa_verde))
    elif opcion_hamburguesa == 3:
        print()
        print('Los ingredientes de la Hamburguesa Blanca son:\n')
        mostrar_menu(list(hamburguesa_blanca))
    elif opcion_hamburguesa == 4:
        print()
        print('Los ingredientes de la Hamburguesa Amarilla son:\n')
        mostrar_menu(list(hamburguesa_amarilla))
    elif opcion_hamburguesa == 5:
        print()
        print('Los ingredientes de la Hamburguesa Azul son:\n')
        mostrar_menu(list(hamburguesa_azul))
    elif opcion_hamburguesa == 6:
        print()
        print('Los ingredientes de la Hamburguesa Naranja son:\n')
        mostrar_menu(list(hamburguesa_naranja))
    elif opcion_hamburguesa == 7:
        print()
        print('Los ingredientes de la Hamburguesa Violeta son:\n')
        mostrar_menu(list(hamburguesa_violeta))
    elif opcion_hamburguesa == 8:
        print()
        print('Los ingredientes de la Hamburguesa Celeste son:\n')
        mostrar_menu(list(hamburguesa_celeste))
    elif opcion_hamburguesa == 9:
        print()
        print('Los ingredientes de la Hamburguesa Rosada son:\n')
        mostrar_menu(list(hamburguesa_rosada))
    elif opcion_hamburguesa == 10:
        print()
        print('Los ingredientes de la Hamburguesa Negra son:\n')
        mostrar_menu(list(hamburguesa_negra))
    else:
        pass
elif opcion == '2':
    print()
    print('Elección de hamburguesa\n')
    mostrar_menu(hamburguesas)
    opcion_compra = int(input('Seleccione la hamburguesa que desea comprar: '))
    cantidad = int(input('Cuantas desea agregar a su carrito: '))
    cantidad_comida(opcion_compra, cantidad, hamburguesas, carrito)
    agregar_carrito(opcion_compra, hamburguesas)
    print('Se agregó a su carrito')
elif opcion == '3':
    print('*** Unir Hamburguesas ***\n')
    print('Puedes elegir dos o más hamburguesas y unirlas en una sola.')
elif opcion == '4':
    print('*** Ingredientes en Común ***\n')
    print('Puedes conocer los ingredientes que tienen en común dos hamburguesas.\n')
elif opcion == '5':
    print('*** Ingredientes Exclusivos ***\n')
    print('Puedes conocer los ingredientes exclusivos que tiene una hamburguesa respecto a la otra.\n')
elif opcion == '6':
    print('*** Comparar Hamburguesas ***\n')
    print('Puedes comparar dos hamburguesas.')
elif opcion == '7':
    print('*** Buscar por Ingrediente ***\n')
    print('Puedes buscar una hamburguesa que contenga un ingrediente específico.')
elif opcion == '8':
    print('*** Eliminar Ingredientes ***\n')
    print('Puedes eliminar ingredientes de tu hamburguesa personalizada.')
elif opcion == '9':
    print('*** Hamburguesa Aleatoria ***\n')
    print('Puedes elegir una hamburguesa de forma aleatoria.')
else: 
    print('Menú de la casa')

print(carrito)