import random

idioma = input('1 - ESP.\n2 - ENG\n').lower()

if idioma == '1':
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
    carrito_cantidad = []
    carrito = {}

    def mostrar_menu(menu):
        for i, comida in enumerate(menu, start = 1):
            print(f'{i}. {comida}')

    def mostrar_menu_carrito(carrito, cantidad, carrito_cantidad):
        print("Contenido del carrito:")
        iter_cantidad = iter(carrito_cantidad)
        for comida, precio in carrito.items():
            print(f"{comida}: ${precio}")
            print(f'Cant: {next(iter_cantidad)}')

    def agregar_carrito(opcion, eleccion_menu, cantidad, carrito, carrito_visible):
        menu_comida = list(eleccion_menu.keys())
        eleccion_comida = menu_comida[opcion - 1]
        
        if eleccion_comida in carrito:
            carrito[eleccion_comida] += eleccion_menu[eleccion_comida] * cantidad
        else:
            carrito[eleccion_comida] = eleccion_menu[eleccion_comida] * cantidad
            

        if eleccion_comida in carrito_visible:
            carrito_cantidad.append(cantidad)
            carrito_visible[eleccion_comida] += eleccion_menu[eleccion_comida] * cantidad
        else:
            carrito_cantidad.append(cantidad)
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

        print('*** Menú principal ***\n')

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
                    mostrar_menu_carrito(carrito_visible, cantidad2, carrito_cantidad)
                    print()
                    seguir_agregando2 = input('¿Desea salir? (Si/No): ').strip().lower()
                    
                    if seguir_agregando2 != 'no':
                        salir_eleccion = True
                        print()
                    else:
                        continue
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
                        carrito_cantidad.append(cantidad3)
                        carrito_visible[nombre_hamburguesa] = precio_hamburguesa * cantidad3 #Quede aca, hay que seguir modificando
                        print('Su combinación de hamburguesas se ha agregado al carrito.\n')
                        mostrar_menu_carrito(carrito_visible, cantidad3, carrito_cantidad)
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
                        carrito_cantidad.append(cantidad8)
                        carrito_visible[eleccion_random] = precio_random * cantidad8
                        print('Su hamburguesa aleatoria ha sido agregado al carrito.\n')
                        mostrar_menu_carrito(carrito_visible, cantidad8, carrito_cantidad)
                        print()

                    repetir8 = input('¿Desea ver otra hamburguesa aleatoria? (Si/No): ').strip().lower()
                    print()
                    if repetir8 != 'si':
                        salir_aleatoriamente = True
                else:
                    salir_aleatoriamente = True
                        
        elif opcion == '9':
            mostrar_menu_carrito(carrito_visible, cantidad2, carrito_cantidad)
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

elif idioma == '2':
    hamburgers = {"Red Hamburger": 3400.00,
                "Green Hamburger": 3000.00,
                "White Hamburger": 3000.00,
                "Yellow Hamburger": 3450.00,
                "Blue Hamburger": 2950.00,
                "Orange Hamburger": 3500.00, 
                "Purple Hamburger": 3100.00,
                "Light Blue Hamburger": 3050.00,
                "Pink Hamburger": 3450.00,
                "Black Hamburger": 3350.00
                }

    red_hamburger = {'Hamburger bun': 450, '200 grams of meat': 900, 'Tomato': 200, 'Lettuce': 200, 'Cheddar cheese': 550, 'Bacon': 500, 'Onion': 200, 'Mustard': 200, 'Mayonnaise': 200}
    green_hamburger = {'Hamburger bun': 450, '200 grams of meat': 900, 'Egg': 250, 'Mozzarella cheese': 500, 'Mushrooms': 250, 'Parsley': 100, 'Barbecue sauce': 200, 'Pickles': 150, 'Mayonnaise': 200}  
    white_hamburger = {'Hamburger bun': 450, '200 grams of meat': 900, 'Blue cheese': 650, 'Tomato': 200, 'Lettuce': 200, 'Ketchup': 200, 'Onion': 200, 'Mayonnaise': 200}
    yellow_hamburger = {'Hamburger bun': 450, '200 grams of meat': 900, 'Mustard': 200, 'Cheddar cheese': 550, 'Bacon': 500, 'Pickles': 150, 'Egg': 250, 'Mushrooms': 250, 'Mayonnaise': 200}
    blue_hamburger = {'Hamburger bun': 450, '200 grams of meat': 900, 'Barbecue sauce': 200, 'Lettuce': 200, 'Mozzarella cheese': 500, 'Tomato': 200, 'Onion': 200, 'Parsley': 100, 'Mayonnaise': 200}  
    orange_hamburger = {'Hamburger bun': 450, '200 grams of meat': 900, 'Mustard': 200, 'Blue cheese': 650, 'Onion': 200, 'Bacon': 500, 'Mushrooms': 250, 'Pickles': 150, 'Mayonnaise': 200}
    purple_hamburger = {'Hamburger bun': 450, '200 grams of meat': 900, 'Ketchup': 200, 'Lettuce': 200, 'Egg': 250, 'Mozzarella cheese': 500, 'Tomato': 200, 'Barbecue sauce': 200, 'Mayonnaise': 200}
    light_blue_hamburger = {'Hamburger bun': 450, '200 grams of meat': 900, 'Onion': 200, 'Cheddar cheese': 550, 'Parsley': 150, 'Bacon': 500, 'Tomato': 200, 'Mayonnaise': 200}
    pink_hamburger = {'Hamburger bun': 450, '200 grams of meat': 900, 'Pickles': 150, 'Lettuce': 200, 'Mushrooms': 250, 'Mozzarella cheese': 500, 'Mustard': 200, 'Onion': 200, 'Mayonnaise': 200} 
    black_hamburger = {'Hamburger bun': 450, '200 grams of meat': 900, 'Barbecue sauce': 200, 'Blue cheese': 650, 'Tomato': 200, 'Bacon': 500, 'Egg': 250, 'Mayonnaise': 200}

    ingredients = {'Hamburger bun': 450.00,
                '200 grams of meat': 900.00,
                'Mayonnaise': 200.00, 'Tomato': 200.00,
                'Lettuce': 200.00,
                'Cheddar cheese': 550.00,
                'Mozzarella cheese': 500.00,
                'Bacon': 500.00,
                'Egg': 250.00,
                'Onion': 200.00,
                'Parsley': 100.00,
                'Ketchup': 200.00,
                'Pickles': 150.00,
                'Mustard': 200.00,
                'Blue cheese': 650.00,
                'Barbecue sauce': 200.00,
                'Mushrooms': 250.00
                }

    set_red = set(red_hamburger.keys())
    set_green = set(green_hamburger.keys())  
    set_white = set(white_hamburger.keys())
    set_yellow = set(yellow_hamburger.keys())
    set_blue = set(blue_hamburger.keys())
    set_orange = set(orange_hamburger.keys())
    set_purple = set(purple_hamburger.keys()) 
    set_light_blue = set(light_blue_hamburger.keys())
    set_pink = set(pink_hamburger.keys())
    set_black = set(black_hamburger.keys())
    set_ingredients = set(ingredients.keys())

    list_red = list(red_hamburger.keys())
    list_green = list(green_hamburger.keys())
    list_white = list(white_hamburger.keys())
    list_yellow = list(yellow_hamburger.keys())
    list_blue = list(blue_hamburger.keys()) 
    list_orange = list(orange_hamburger.keys())
    list_purple = list(purple_hamburger.keys())
    list_light_blue = list(light_blue_hamburger.keys())
    list_pink = list(pink_hamburger.keys())
    list_black = list(black_hamburger.keys())

    hamburgers_sets = {'1': set_red,
                    '2': set_green,
                    '3': set_white,
                    '4': set_yellow,
                    '5': set_blue,
                    '6': set_orange,
                    '7': set_purple,
                    '8': set_light_blue, 
                    '9': set_pink,
                    '10': set_black
                    }

    hamburgers_lists = {'1': list_red,
                        '2': list_green,
                        '3': list_white, 
                        '4': list_yellow,
                        '5': list_blue,
                        '6': list_orange,
                        '7': list_purple, 
                        '8': list_light_blue,
                        '9': list_pink,
                        '10': list_black
                    }
                    
    random_hamburgers_list = {'1': "Red Hamburger",
                            '2': "Green Hamburger",
                            '3': "White Hamburger",
                            '4': "Yellow Hamburger",
                            '5': "Blue Hamburger",
                            '6': "Orange Hamburger",
                            '7': "Purple Hamburger",
                            '8': "Light Blue Hamburger",
                            '9': "Pink Hamburger",
                            '10': "Black Hamburger"
                            }
                            
    main_menu = ['View the house menu',
                'Choose a burger',
                'Combine burgers',
                'Common ingredients in burgers',
                'Exclusive ingredients for each burger',
                'Compare burgers',
                'Missing ingredients in your burger',
                'Randomly select a burger',
                'Complete the purchase',
                'Exit']
                
    customer_choice = []                 
    visible_cart = {}
    cart_quantity = []
    cart = {}

    def show_menu(menu):
        for i, food in enumerate(menu, start=1):
            print(f'{i}. {food}')
            
    def show_cart_menu(cart, quantity, cart_quantity):
        print("Cart content:")
        iter_quantity = iter(cart_quantity)
        for food, price in cart.items():
            print(f"{food}: ${price}")
            print(f'Qty: {next(iter_quantity)}')
            
    def add_to_cart(option, menu_choice, quantity, cart, visible_cart):
        menu_food = list(menu_choice.keys())
        food_choice = menu_food[option - 1]
        
        if food_choice in cart:
            cart[food_choice] += menu_choice[food_choice] * quantity
        else:
            cart[food_choice] = menu_choice[food_choice] * quantity

        if food_choice in visible_cart:
            cart_quantity.append(quantity)
            visible_cart[food_choice] += menu_choice[food_choice] * quantity
        else:
            cart_quantity.append(quantity)
            visible_cart[food_choice] = menu_choice[food_choice] * quantity
            
    def join_hamburgers(option1, option2, hamburgers):
        if option1 in hamburgers and option2 in hamburgers:
            union = hamburgers[option1].union(hamburgers[option2])
            return union
        else:
            return None
            
    def intersection_hamburgers(option1, option2, hamburgers):
        if option1 in hamburgers and option2 in hamburgers:
            intersection = hamburgers[option1].intersection(hamburgers[option2])
            return intersection
        else:
            return None
            
    def difference_hamburgers(option1, option2, hamburgers):
        if option1 in hamburgers and option2 in hamburgers:
            difference = hamburgers[option1].difference(hamburgers[option2])
            return difference
        else:
            return None
            
    def compare(option1, option2, hamburgers_lists):
        list1 = hamburgers_lists.get(option1)
        list2 = hamburgers_lists.get(option2)
        return list1, list2

    def find_missing_ingredients(chosen_hamburger, hamburgers_sets, universal_set):
        if chosen_hamburger in hamburgers_sets:
            selected_hamburger = hamburgers_sets[chosen_hamburger]
            missing_ingredients = universal_set - selected_hamburger
            return missing_ingredients
        else:
            return None
            
    def calculate_hamburger_price(hamburger_ingredients):
        # Calculate total price of hamburger ingredients
        total_price = sum(ingredients.get(ingredient, 0) for ingredient in hamburger_ingredients)
        return total_price

    print()  
    print('*** HAMBURCOLORS ***\n')
    print('Welcome to our burger joint!')
    print('We offer a wide variety of delicious burgers')
    print('We offer the opportunity to customize your own burger')
    print('Enjoy your meal with us!\n')

    while True:

        print('*** Main menu ***\n')
    
        show_menu(main_menu)
        option = input('Select an option: ')
        print()
        if option == '1':
            exit_view_menu = False
            while not exit_view_menu:
                print('*** House Menu ***\n')
                show_menu(hamburgers)
                hamburger_option = int(input('Select a hamburger to view ingredients: '))
                print()
                if 1 <= hamburger_option <= len(hamburgers):
                    chosen_hamburger = list(hamburgers_lists.values())[hamburger_option - 1]
                    print('Hamburger ingredients: ')
                    show_menu(chosen_hamburger)
                else:
                    print('Invalid option.')

                repeat1 = input('View another hamburger? (Yes/No): ').strip().lower()
                print()
                if repeat1 != 'yes':
                    exit_view_menu = True

        elif option == '2':
            exit_choice = False
            while not exit_choice:
                print()
                print('Hamburger Choice\n')
                show_menu(hamburgers)
                add_to_cart2 = input('Add a hamburger to cart? (Yes/No): ').strip().lower()
                if add_to_cart2 == 'yes':
                    purchase_option2 = int(input('Choose the hamburger: '))
                    quantity2 = int(input('How many to add to your cart: '))
                    print()
                    add_to_cart(purchase_option2, hamburgers, quantity2, cart, visible_cart)
                    print('Your choice has been added successfully\n')
                    show_cart_menu(visible_cart, quantity2, cart_quantity)
                    print()
                    continue_adding2 = input('Ready to checkout? (Yes/No): ').strip().lower()
                    
                    if continue_adding2 != 'no':
                        exit_choice = True
                        print()
                    else:
                        continue
                else:
                    exit_choice = True
                    print()

        elif option == '3':
            combination_counter = 1
            exit_join = False
            while not exit_join:
                print('*** Join Hamburgers ***\n')
                print('You can choose two and join them into one.\n')
                show_menu(hamburgers)
                hamburger1 = input('Select first option: ')
                hamburger2 = input('Select second option: ')
                print()
                union = join_hamburgers(hamburger1, hamburger2, hamburgers_sets)
                if union is not None:
                    print(f'The union of your two choices is: \n') 
                    show_menu(union)
                    add_to_cart3 = input('Add this hamburger to cart? (Yes/No): ').strip().lower()
                    if add_to_cart3 == 'yes':
                        quantity3 = int(input('How many to add to your cart: '))
                        print()
                        hamburger_name = f'Combination no {combination_counter}'
                        hamburger_price = calculate_hamburger_price(union)
                        cart[hamburger_name] = hamburger_price * quantity3
                        cart_quantity.append(quantity3)
                        visible_cart[hamburger_name] = hamburger_price * quantity3
                        print('Your hamburger combination has been added to cart.\n')
                        show_cart_menu(visible_cart, quantity3, cart_quantity)
                        print()
                    else:
                        print('The hamburger was not added to cart.\n')
                        exit_join = True
                        break
                else:
                    print('Invalid options selected.')

                continue_adding3 = input('Join two more hamburgers? (Yes/No): ').strip().lower()
                print()
                if continue_adding3 != 'yes':
                    exit_join = True  
                
        elif option == '4':
            exit_intersection = False
            while not exit_intersection:
                print('*** Ingredients in Common ***\n')
                print('See ingredients two hamburgers have in common.\n') 
                show_menu(hamburgers)
                hamburger3 = input('Select first option: ')
                hamburger4 = input('Select second option: ')
                print()
                intersection = intersection_hamburgers(hamburger3, hamburger4, hamburgers_sets)
                if intersection is not None:
                    print(f'Ingredients in common between selections: \n')
                    show_menu(intersection)
                else:
                    print('Invalid options selected.')

                repeat4 = input('View another option? (Yes/No): ').strip().lower()
                print()
                if repeat4 != 'yes':
                    exit_intersection = True

        elif option == '5':
            exit_difference = False
            while not exit_difference:
                print('*** Exclusive Ingredients ***\n')
                print('See the exclusive ingredients one hamburger has compared to the other.\n')
                show_menu(hamburgers)
                hamburger5 = input('Select your hamburger: ')
                hamburger6 = input('Select the other hamburger: ')
                print()
                difference = difference_hamburgers(hamburger5, hamburger6, hamburgers_sets)
                if difference is not None:
                    print(f'Exclusive ingredients in your selection: \n')
                    show_menu(difference)
                else:
                    print('Invalid options selected.')

                repeat5 = input('View another option? (Yes/No): ').strip().lower()
                print()
                if repeat5 != 'yes':
                    exit_difference = True
            
        elif option == '6':
            exit_compare = False
            while not exit_compare:
                print('*** Compare Hamburgers ***\n')
                print('You can compare two hamburgers.')
                show_menu(hamburgers)
                hamburger7 = input('Select first option: ')
                hamburger8 = input('Select second option: ')
                print()
                list_hamburger1, list_hamburger2 = compare(hamburger7, hamburger8, hamburgers_lists)
                if list_hamburger1 is not None and list_hamburger2 is not None:
                    print('Ingredients of first hamburger:')
                    show_menu(list_hamburger1)
                    print()
                    print('Ingredients of second hamburger:')
                    show_menu(list_hamburger2)
                else:
                    print('One of the selected options is invalid.')

                repeat6 = input('View another option? (Yes/No): ').strip().lower()
                print()
                if repeat6 != 'yes':
                    exit_compare = True
                    

        elif option == '7':
            missing = False
            while not missing:
                print('*** Missing Ingredients in your Hamburger ***\n')
                print('See ingredients missing in the hamburger you choose.\n')
                show_menu(hamburgers)
                chosen_hamburger = input('Choose the hamburger: ')
                missing_ingredients = find_missing_ingredients(chosen_hamburger, hamburgers_sets, set_ingredients)
                print()
                if missing_ingredients:
                    print('Missing ingredients in selected hamburger:')
                    show_menu(missing_ingredients)
                else:
                    print('Invalid hamburger selected.')
                
                repeat7 = input('View another option? (Yes/No): ').strip().lower()
                print()
                if repeat7 != 'yes':
                    missing = True
            
        elif option == '8':
            combination_counter = 1
            exit_random = False
            while not exit_random:
                print('*** Random Hamburger ***\n')
                print('You can choose a random hamburger.')
                start = input('Begin random selection? (Yes/No): ').lower()
                if start == 'yes':
                    selection = random.choice(list(hamburgers_lists.keys()))
                    random_selection = random_hamburgers_list[selection]
                    random_price = hamburgers[random_selection]
                    print()
                    print(f'{random_selection} has been randomly selected\n')
                    print(f'The ingredients are:\n')
                    if selection in hamburgers_lists:
                        show_menu(hamburgers_lists[selection])

                    add_to_cart = input('Add this hamburger to cart? (Yes/No): ').strip().lower()
                    if add_to_cart == 'yes':
                        quantity8 = int(input('How many to add?: '))
                        cart[random_selection] = random_price * quantity8
                        cart_quantity.append(quantity8)
                        visible_cart[random_selection] = random_price * quantity8
                        print('Your random hamburger has been added to cart.\n')
                        show_cart_menu(visible_cart, quantity8, cart_quantity)
                        print()

                    repeat8 = input('View another random hamburger? (Yes/No): ').strip().lower()
                    print()
                    if repeat8 != 'yes':
                        exit_random = True
                else:
                    exit_random = True
                        
        elif option == '9':
            show_cart_menu(visible_cart, quantity3, cart_quantity)
            total_price = 0
            for price in cart.values():
                total_price += price

            print()
            print(f'- Total: {total_price}\n')
            print('Thank you for your purchase! Enjoy')
            break

        else:
            print('Thank you for visiting!') 
            break