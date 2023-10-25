import random

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

ingredientes = {'Pan de hamburguesa': 1, '200 gramos de carne': 1, 'Mayonesa': 1, 'Tomate': 1, 'Lechuga': 1, 'Queso Cheddar': 1, 'Queso Mozzarella': 1, 'Bacon': 1, 'Huevo': 1, 'Cebolla': 1, 'Perejil': 1, 'Ketchup': 1, 'Pepinillos': 1, 'Mostaza': 1, 'Queso Azul': 1, 'Salsa Barbacoa': 1, 'Champiñones': 1}

set_roja = set(hamburguesa_roja.keys())
set_verde = set(hamburguesa_verde.keys())
set_blanca = set(hamburguesa_blanca.keys())
set_amarilla = set(hamburguesa_amarilla.keys())
set_azul = set(hamburguesa_azul.keys())
set_naranja = set(hamburguesa_naranja.keys())
set_violate = set(hamburguesa_violeta.keys())
set_celeste = set(hamburguesa_celeste.keys())
set_rosada = set(hamburguesa_rosada.keys())
set_negra = set(hamburguesa_negra.keys())
set_ingredientes = set(ingredientes.keys())

lista_roja = list(hamburguesa_roja.keys())
lista_verde = list(hamburguesa_verde.keys())
lista_blanca = list(hamburguesa_blanca.keys())
lista_amarilla = list(hamburguesa_amarilla.keys())
lista_azul = list(hamburguesa_azul.keys())
lista_naranja = list(hamburguesa_naranja.keys())
lista_violeta = list(hamburguesa_violeta.keys())
lista_celeste = list(hamburguesa_celeste.keys())
lista_rosada = list(hamburguesa_rosada.keys())
lista_negra = list(hamburguesa_negra.keys())

conjunto_hamburguesas = {'1': set_roja, '2': set_verde, '3': set_blanca, '4': set_amarilla, '5': set_azul, '6': set_naranja, '7': set_violate, '8': set_celeste, '9': set_rosada, '10': set_negra}
lista_hamburguesas = {'1': lista_roja, '2': lista_verde, '3': lista_blanca, '4': lista_amarilla, '5': lista_azul, '6': lista_naranja, '7': lista_violeta, '8': lista_celeste, '9': lista_rosada, '10': lista_negra}

menu_principal = ['Ver el menú de la casa', 
                  'Elección de una hamburguesa',
                  'Unir hamburguesas', 
                  'Ingredientes que tienen en común las hamburguesas', 
                  'Ingredientes exclusivos de cada hamburguesa', 
                  'Comparar hamburguesas', 
                  'Ingredientes Faltantes en su Hamburguesa', 
                  'Elegir una hamburguesa aleatoriamente', 
                  'Terminar la compra',
                  'Salir']

eleccion_cliente = []
carrito = {}

def mostrar_menu(menu):
    for i, comida in enumerate(menu, start = 1):
        print(f'{i}. {comida}')

def mostrar_menu_hamburguesa(menu):
    for i, (comida, precio) in enumerate(menu.items(), start = 1):
        print(f'{i}. {comida}: {precio}')

def agregar_carrito(opcion, eleccion_menu, cantidad, carrito):
    menu_comida = list(eleccion_menu.keys())
    eleccion_comida = menu_comida[opcion - 1]
    
    if eleccion_comida in carrito:
        carrito[eleccion_comida] += eleccion_menu[eleccion_comida] * cantidad
    else:
        carrito[eleccion_comida] = eleccion_menu[eleccion_comida] * cantidad

def union_hamburguesas(opcion1, opcion2, hamburguesa):
    if opcion1 in hamburguesa and opcion2 in hamburguesa:
        union = hamburguesa[opcion1].union(hamburguesa[opcion2])
        return union
    else:
        return None
    
def interseccion_hamburguesas(opcion1, opcion2, hamburguesa):
    if opcion1 in hamburguesa and opcion2 in hamburguesa:
        union = hamburguesa[opcion1].intersection(hamburguesa[opcion2])
        return union
    else:
        return None
    
def interseccion_hamburguesas(opcion1, opcion2, hamburguesa):
    if opcion1 in hamburguesa and opcion2 in hamburguesa:
        union = hamburguesa[opcion1].difference(hamburguesa[opcion2])
        return union
    else:
        return None
    
def comparacion(opcion1, opcion2, lista_hamburguesas):
    lista1 = lista_hamburguesas.get(opcion1)
    lista2 = lista_hamburguesas.get(opcion2)
    return lista1, lista2

def encontrar_ingredientes_faltantes(hamburguesa_elegida, conjunto_hamburguesas, conjunto_universal):
    if hamburguesa_elegida in conjunto_hamburguesas:
        hamburguesa_seleccionada = conjunto_hamburguesas[hamburguesa_elegida]
        ingredientes_faltantes = conjunto_universal - hamburguesa_seleccionada
        return ingredientes_faltantes
    else:
        return None

print()
print('*** HAMBURCOLORS ***\n')
print('¡Bienvenido a nuestra hamburgueseria!')
print('Ofrecemos una amplia variedad de hamburguesas deliciosas')
print('Ofrecemos la oportunidad de personalizar tu propia hamburguesa')
print('¡Esperamos que disfrutes de tu comida con nosotros!\n')

while True:

    print('Menú principal\n')

    mostrar_menu(menu_principal)
    opcion = input('Ingrese una opcion: ')
    print()
    if opcion == '1':
        salir_ver_menu = False
        while not salir_ver_menu:
            print('*** Menú de la Casa ***\n')
            mostrar_menu(hamburguesas)
            opcion_hamburguesa = int(input('Seleccione una hamburguesa para ver los ingredientes: '))
            print()
            if 1 <= opcion_hamburguesa <= len(hamburguesas):
                hamburguesa_elegida = list(lista_hamburguesas.values())[opcion_hamburguesa - 1]
                print('Los ingredientes de su hamburguesa son: ')
                mostrar_menu(hamburguesa_elegida)
            else:
                print('Opción inválida.')

            repetir = input('¿Desea ver otra hamburguesa? (Si/No): ').strip().lower()
            print()
            if repetir != 'si':
                salir_ver_menu = True

    elif opcion == '2':
        salir_eleccion = False
        while not salir_eleccion:
            print()
            print('Elección de hamburguesa\n')
            mostrar_menu(hamburguesas)
            opcion_compra = int(input('Elige la hamburguesa: '))
            cantidad = int(input('Cuantas desea agregar a su carrito: '))
            agregar_carrito(opcion_compra, hamburguesas, cantidad, carrito)
            print('Su elección se ha agregado correctamente')
            print(carrito)
            seguir_agregando = input('¿Desea agregar más hamburguesas al carrito? (Si/No): ').strip().lower()
            if seguir_agregando != 'si':
                salir_eleccion = True

    elif opcion == '3':
        contador_combinaciones = 1
        salir_union = False
        while not salir_union:
            print('*** Unir Hamburguesas ***\n')
            print('Puedes elegir dos y unirlas en una sola.\n')
            mostrar_menu(hamburguesas)
            hamburguesa1 = input('Seleccione una opcion: ')
            hamburguesa2 = input('Seleccione una segunda opcion: ')
            print()
            union = union_hamburguesas(hamburguesa1, hamburguesa2, conjunto_hamburguesas)
            if union is not None:
                print(f'La unión de sus dos elecciones son: \n')
                mostrar_menu(union)
                desea_agregar = input('¿Desea agregar esta hamburguesa al carrito con un nombre específico? (Si/No): ').strip().lower()
                if desea_agregar == 'si':
                    cantidad = int(input('Cuantas desea agregar a su carrito: '))
                    nombre_hamburguesa = f'Combinación nro {contador_combinaciones}'
                    carrito[nombre_hamburguesa] = 1 * cantidad
                    print('Su combinación de hamburguesas se ha agregado al carrito.')
                    print(carrito)
                else:
                    print('La hamburguesa no se ha agregado al carrito.')
            else:
                print('Las opciones elegidas no son válidas.')

            seguir_agregando = input('¿Desea agregar más hamburguesas al carrito? (Si/No): ').strip().lower()
            if seguir_agregando != 'si':
                salir_union = True  
            
    elif opcion == '4':
        salir_interseccion = False
        while not salir_interseccion:
            print('*** Ingredientes en Común ***\n')
            print('Puedes conocer los ingredientes que tienen en común dos hamburguesas.\n')
            mostrar_menu(hamburguesas)
            hamburguesa1 = input('Seleccione una opcion: ')
            hamburguesa2 = input('Seleccione una segunda opcion: ')
            print()
            interseccion = interseccion_hamburguesas(hamburguesa1, hamburguesa2, conjunto_hamburguesas)
            if interseccion is not None:
                print(f'Los ingredientes en común de sus dos elecciones son: \n')
                mostrar_menu(interseccion)
            else:
                print('Las opciones elegidas no son válidas.')

            repetir = input('¿Desea ver otra opcion? (Si/No): ').strip().lower()
            print()
            if repetir != 'si':
                salir_interseccion = True

    elif opcion == '5':
        salir_diferencia = False
        while not salir_diferencia:
            print('*** Ingredientes Exclusivos ***\n')
            print('Puedes conocer los ingredientes exclusivos que tiene una hamburguesa respecto a la otra.\n')
            mostrar_menu(hamburguesas)
            hamburguesa1 = input('Seleccione su hamburguesa: ')
            hamburguesa2 = input('Seleccione la otra hamburguesa: ')
            print()
            diferencia = interseccion_hamburguesas(hamburguesa1, hamburguesa2, conjunto_hamburguesas)
            if diferencia is not None:
                print(f'Los ingredientes exclusivos de su hamburguesa son: \n')
                mostrar_menu(diferencia)
            else:
                print('Las opciones elegidas no son válidas.')

            repetir = input('¿Desea ver otra opcion? (Si/No): ').strip().lower()
            print()
            if repetir != 'si':
                salir_diferencia = True
        
    elif opcion == '6':
        salir_comparacion = False
        while not salir_comparacion:
            print('*** Comparar Hamburguesas ***\n')
            print('Puedes comparar dos hamburguesas.')
            mostrar_menu(hamburguesas)
            hamburguesa1 = input('Seleccione una opcion: ')
            hamburguesa2 = input('Seleccione una segunda opcion: ')
            print()
            lista_hamburguesa1, lista_hamburguesa2 = comparacion(hamburguesa1, hamburguesa2, lista_hamburguesas)
            if lista_hamburguesa1 is not None and lista_hamburguesa2 is not None:
                print('Ingredientes de la primera hamburguesa:')
                mostrar_menu(lista_hamburguesa1)
                print()
                print('Ingredientes de la segunda hamburguesa:')
                mostrar_menu(lista_hamburguesa2)
            else:
                print('Alguna de las opciones elegidas no es válida.')

            repetir = input('¿Desea ver otra opcion? (Si/No): ').strip().lower()
            print()
            if repetir != 'si':
                salir_comparacion = True
                

    elif opcion == '7':
        faltante = False
        while not faltante:
            print('*** Ingredientes Faltantes en su Hamburguesa ***\n')
            print('Puedes ver los ingredientes que no están en la hamburguesa que eliges.\n')
            mostrar_menu(hamburguesas)
            hamburguesa_elegida = input('Elige la hamburguesa: ')
            ingredientes_faltantes = encontrar_ingredientes_faltantes(hamburguesa_elegida, conjunto_hamburguesas, set_ingredientes)
            print()
            if ingredientes_faltantes:
                print('Ingredientes faltantes en la hamburguesa seleccionada:')
                mostrar_menu(ingredientes_faltantes)
            else:
                print('La hamburguesa seleccionada no es válida.')
            
            repetir = input('¿Desea ver otra opcion? (Si/No): ').strip().lower()
            print()
            if repetir != 'si':
                faltante = True
        
    elif opcion == '8':
        contador_combinaciones = 1
        salir_aleatoriamente = False
        while not salir_aleatoriamente:
            print('*** Hamburguesa Aleatoria ***\n')
            print('Puedes elegir una hamburguesa de forma aleatoria.')
            hamburguesa = input('Comenzamos con tu eleccion(SI/NO): ').lower()
            if hamburguesa == 'si':
                eleccion = random.choice(list(lista_hamburguesas.keys()))
                print()
                print(f'Ha salido seleccionada la hamburguesa número {eleccion}')
                print(f'Y sus ingredientes son:')
                if eleccion in lista_hamburguesas:
                    mostrar_menu(lista_hamburguesas[eleccion])

                desea_agregar = input('¿Desea agregar esta hamburguesa al carrito con un nombre específico? (Si/No): ').strip().lower()
                if desea_agregar == 'si':
                    cantidad = int(input('Cuantas desea agregar a su carrito: '))
                    nombre_hamburguesa = f'Hamburguesa aleatoria {contador_combinaciones}'
                    carrito[nombre_hamburguesa] = 1 * cantidad
                    print('Su hamburguesa aleatoria se ha agregado al carrito.')
                    print(carrito) 

            if desea_agregar == 'no':
                repetir = input('¿Desea agregar otra hamburguesa aleatoria? (Si/No): ').strip().lower()
                print()
                if repetir != 'si':
                    salir_aleatoriamente = True
                    
    elif opcion == '9':
        mostrar_menu(carrito)
        print('¡Muchas gracias por su compra! Que la disfrute')
        break
    else: 
        print('¡Muchas gracias por su visita!')
        break


print(carrito)