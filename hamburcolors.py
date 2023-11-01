import random

hamburguesas = {"Hamburguesa Roja": 3400.00, 
                "Hamburguesa Verde": 3000.00, 
                "Hamburguesa Blanca": 3000.00, 
                "Hamburguesa Amarilla": 3450.00, 
                "Hamburguesa Azul": 2950.00, 
                "Hamburguesa Naranja": 3500.00, 
                "Hamburguesa Violeta": 3100.00, 
                "Hamburguesa Celeste": 3050.00, 
                "Hamburguesa Rosada": 3450.00, 
                "Hamburguesa Negra": 3350.00
                }

hamburguesa_roja = {'Pan de hamburguesa': 450, '200 gramos de carne': 900, 'Tomate': 200, 'Lechuga': 200, 'Queso Cheddar': 550, 'Bacon': 500, 'Cebolla': 200, 'Mostaza': 200, 'Mayonesa': 200}
hamburguesa_verde = {'Pan de hamburguesa': 450, '200 gramos de carne': 900, 'Huevo': 250, 'Queso Mozzarella': 500, 'Champiñones': 250, 'Perejil': 100, 'Salsa Barbacoa': 200, 'Pepinillos': 150, 'Mayonesa': 200}
hamburguesa_blanca = {'Pan de hamburguesa': 450, '200 gramos de carne': 900, 'Queso Azul': 650, 'Tomate': 200, 'Lechuga': 200, 'Ketchup': 200, 'Cebolla': 200, 'Mayonesa': 200}
hamburguesa_amarilla = {'Pan de hamburguesa': 450, '200 gramos de carne': 900, 'Mostaza': 200, 'Queso Cheddar': 550, 'Bacon': 500, 'Pepinillos': 150, 'Huevo': 250, 'Champiñones': 250, 'Mayonesa': 200}
hamburguesa_azul = {'Pan de hamburguesa': 450, '200 gramos de carne': 900, 'Salsa Barbacoa': 200, 'Lechuga': 200, 'Queso Mozzarella': 500, 'Tomate': 200, 'Cebolla': 200, 'Perejil': 100, 'Mayonesa': 200}
hamburguesa_naranja = {'Pan de hamburguesa': 450, '200 gramos de carne': 900, 'Mostaza': 200, 'Queso Azul': 650, 'Cebolla': 200, 'Bacon': 500, 'Champiñones': 250, 'Pepinillos': 150, 'Mayonesa': 200}
hamburguesa_violeta = {'Pan de hamburguesa': 450, '200 gramos de carne': 900, 'Ketchup': 200, 'Lechuga': 200, 'Huevo': 250, 'Queso Mozzarella': 500, 'Tomate': 200, 'Salsa Barbacoa': 200, 'Mayonesa': 200}
hamburguesa_celeste = {'Pan de hamburguesa': 450, '200 gramos de carne': 900, 'Cebolla': 200, 'Queso Cheddar': 550, 'Perejil': 150, 'Bacon': 500, 'Tomate': 200, 'Mayonesa': 200}
hamburguesa_rosada = {'Pan de hamburguesa': 450, '200 gramos de carne': 900, 'Pepinillos': 150, 'Lechuga': 200, 'Champiñones': 250, 'Queso Mozzarella': 500, 'Mostaza': 200, 'Cebolla': 200, 'Mayonesa': 200}
hamburguesa_negra = {'Pan de hamburguesa': 450, '200 gramos de carne': 900, 'Salsa Barbacoa': 200, 'Queso Azul': 650, 'Tomate': 200, 'Bacon': 500, 'Huevo': 250, 'Mayonesa': 200}

ingredientes = {'Pan de hamburguesa': 450.00, 
                '200 gramos de carne': 900.00, 
                'Mayonesa': 200.00, 'Tomate': 200.00, 
                'Lechuga': 200.00, 
                'Queso Cheddar': 550.00, 
                'Queso Mozzarella': 500.00, 
                'Bacon': 500.00, 
                'Huevo': 250.00, 
                'Cebolla': 200.00, 
                'Perejil': 100.00, 
                'Ketchup': 200.00, 
                'Pepinillos': 150.00, 
                'Mostaza': 200.00, 
                'Queso Azul': 650.00, 
                'Salsa Barbacoa': 200.00, 
                'Champiñones': 250.00
                }

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

conjunto_hamburguesas = {'1': set_roja, 
                         '2': set_verde, 
                         '3': set_blanca, 
                         '4': set_amarilla, 
                         '5': set_azul, 
                         '6': set_naranja, 
                         '7': set_violate, 
                         '8': set_celeste, 
                         '9': set_rosada, 
                         '10': set_negra
                         }

lista_hamburguesas = {'1': lista_roja, 
                      '2': lista_verde, 
                      '3': lista_blanca, 
                      '4': lista_amarilla, 
                      '5': lista_azul, 
                      '6': lista_naranja, 
                      '7': lista_violeta, 
                      '8': lista_celeste, 
                      '9': lista_rosada, 
                      '10': lista_negra
                      }

lista_hamburguesas_random = {'1': "Hamburguesa Roja", 
                             '2': "Hamburguesa Verde", 
                             '3': "Hamburguesa Blanca", 
                             '4': "Hamburguesa Amarilla", 
                             '5': "Hamburguesa Azul", 
                             '6': "Hamburguesa Naranja", 
                             '7': "Hamburguesa Violeta", 
                             '8': "Hamburguesa Celeste", 
                             '9': "Hamburguesa Rosada", 
                             '10': "Hamburguesa Negra"
                             }

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
carrito_visible = {}
carrito = {}

def mostrar_menu(menu):
    for i, comida in enumerate(menu, start = 1):
        print(f'{i}. {comida}')

def mostrar_menu_carrito(carrito):
    print("Contenido del carrito:")
    for comida, precio in carrito.items():
        print(f"{comida}: {precio}")

def agregar_carrito(opcion, eleccion_menu, cantidad, carrito, carrito_visible):
    menu_comida = list(eleccion_menu.keys())
    eleccion_comida = menu_comida[opcion - 1]
    
    if eleccion_comida in carrito:
        carrito[eleccion_comida] += eleccion_menu[eleccion_comida] * cantidad
    else:
        carrito[eleccion_comida] = eleccion_menu[eleccion_comida] * cantidad
        

    if eleccion_comida in carrito_visible:
        carrito_visible[cantidad] += 'Unid.'
        carrito_visible[eleccion_comida] += eleccion_menu[eleccion_comida] * cantidad
    else:
        carrito_visible[cantidad] = 'Unid.'
        carrito_visible[eleccion_comida] = eleccion_menu[eleccion_comida] * cantidad

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
    
def calcular_precio_hamburguesa(ingredientes_hamburguesa):
    # Calcular el precio total de los ingredientes de la hamburguesa
    precio_total = sum(ingredientes.get(ingrediente, 0) for ingrediente in ingredientes_hamburguesa)
    return precio_total

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

            repetir1 = input('¿Desea ver otra hamburguesa? (Si/No): ').strip().lower()
            print()
            if repetir1 != 'si':
                salir_ver_menu = True

    elif opcion == '2':
        salir_eleccion = False
        while not salir_eleccion:
            print()
            print('Elección de hamburguesa\n')
            mostrar_menu(hamburguesas)
            agregar_al_carrito = input('¿Desea agregar una hamburguesa al carrito? (Si/No): ').strip().lower()
            if agregar_al_carrito == 'si':
                opcion_compra2 = int(input('Elige la hamburguesa: '))
                cantidad2 = int(input('Cuantas desea agregar a su carrito: '))
                print()
                agregar_carrito(opcion_compra2, hamburguesas, cantidad2, carrito, carrito_visible)
                print('Su elección se ha agregado correctamente\n')
                mostrar_menu_carrito(carrito_visible)
                print()
                seguir_agregando2 = input('¿Desea salir? (Si/No): ').strip().lower()
                
                if seguir_agregando2 != 'no':
                    salir_eleccion = True
                    print()
                else:
                    salir_eleccion = True
                    print()
            else:
                salir_eleccion = True
                print()

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
                desea_agregar3 = input('¿Desea agregar esta hamburguesa al carrito? (Si/No): ').strip().lower()
                if desea_agregar3 == 'si':
                    cantidad3 = int(input('Cuantas desea agregar a su carrito: '))
                    print()
                    nombre_hamburguesa = f'Combinación nro {contador_combinaciones}'
                    precio_hamburguesa = calcular_precio_hamburguesa(union)
                    carrito[nombre_hamburguesa] = precio_hamburguesa * cantidad3
                    carrito_visible[cantidad3] = 'Unid.'
                    carrito_visible[nombre_hamburguesa] = precio_hamburguesa * cantidad3 #Quede aca, hay que seguir modificando
                    print('Su combinación de hamburguesas se ha agregado al carrito.\n')
                    mostrar_menu_carrito(carrito_visible)
                    print()
                else:
                    print('La hamburguesa no se ha agregado al carrito.\n')
                    salir_union = True
                    break
            else:
                print('Las opciones elegidas no son válidas.')

            seguir_agregando3 = input('¿Desea unir dos hamburguesas más? (Si/No): ').strip().lower()
            print()
            if seguir_agregando3 != 'si':
                salir_union = True  
            
    elif opcion == '4':
        salir_interseccion = False
        while not salir_interseccion:
            print('*** Ingredientes en Común ***\n')
            print('Puedes conocer los ingredientes que tienen en común dos hamburguesas.\n')
            mostrar_menu(hamburguesas)
            hamburguesa3 = input('Seleccione una opcion: ')
            hamburguesa4 = input('Seleccione una segunda opcion: ')
            print()
            interseccion = interseccion_hamburguesas(hamburguesa3, hamburguesa4, conjunto_hamburguesas)
            if interseccion is not None:
                print(f'Los ingredientes en común de sus dos elecciones son: \n')
                mostrar_menu(interseccion)
            else:
                print('Las opciones elegidas no son válidas.')

            repetir4 = input('¿Desea ver otra opcion? (Si/No): ').strip().lower()
            print()
            if repetir4 != 'si':
                salir_interseccion = True

    elif opcion == '5':
        salir_diferencia = False
        while not salir_diferencia:
            print('*** Ingredientes Exclusivos ***\n')
            print('Puedes conocer los ingredientes exclusivos que tiene una hamburguesa respecto a la otra.\n')
            mostrar_menu(hamburguesas)
            hamburguesa5 = input('Seleccione su hamburguesa: ')
            hamburguesa6 = input('Seleccione la otra hamburguesa: ')
            print()
            diferencia = interseccion_hamburguesas(hamburguesa1, hamburguesa2, conjunto_hamburguesas)
            if diferencia is not None:
                print(f'Los ingredientes exclusivos de su hamburguesa son: \n')
                mostrar_menu(diferencia)
            else:
                print('Las opciones elegidas no son válidas.')

            repetir5 = input('¿Desea ver otra opcion? (Si/No): ').strip().lower()
            print()
            if repetir5 != 'si':
                salir_diferencia = True
        
    elif opcion == '6':
        salir_comparacion = False
        while not salir_comparacion:
            print('*** Comparar Hamburguesas ***\n')
            print('Puedes comparar dos hamburguesas.')
            mostrar_menu(hamburguesas)
            hamburguesa7 = input('Seleccione una opcion: ')
            hamburguesa8 = input('Seleccione una segunda opcion: ')
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

            repetir6 = input('¿Desea ver otra opcion? (Si/No): ').strip().lower()
            print()
            if repetir6 != 'si':
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
            
            repetir7 = input('¿Desea ver otra opcion? (Si/No): ').strip().lower()
            print()
            if repetir7 != 'si':
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
                eleccion_random = lista_hamburguesas_random[eleccion]
                precio_random = hamburguesas[eleccion_random]
                print()
                print(f'Ha salido seleccionada la {eleccion_random}\n')
                print(f'Y sus ingredientes son:\n')
                if eleccion in lista_hamburguesas:
                    mostrar_menu(lista_hamburguesas[eleccion])

                desea_agregar = input('¿Desea agregar esta hamburguesa al carrito? (Si/No): ').strip().lower()
                if desea_agregar == 'si':
                    cantidad8 = int(input('¿Cuantas desea agregar?: '))
                    carrito[eleccion_random] = precio_random * cantidad8
                    carrito_visible[cantidad8] = 'Unid.'
                    carrito_visible[eleccion_random] = precio_random * cantidad8
                    print('Su hamburguesa aleatoria ha sido agregado al carrito.\n')
                    mostrar_menu_carrito(carrito_visible)
                    print()

                repetir8 = input('¿Desea ver otra hamburguesa aleatoria? (Si/No): ').strip().lower()
                print()
                if repetir8 != 'si':
                    salir_aleatoriamente = True
            else:
                salir_aleatoriamente = True
                    
    elif opcion == '9':
        for comida, precio in carrito_visible.items():
            print(f'- {comida}: {precio}')
            suma_precios = 0
            for precio in carrito.values():
                suma_precios += precio

        print()
        print(f'- Total: {suma_precios}\n')
        print('¡Muchas gracias por su compra! Que la disfrute')
        break

    else: 
        print('¡Muchas gracias por su visita!')
        break
