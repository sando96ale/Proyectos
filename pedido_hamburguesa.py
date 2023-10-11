from menu_completo import menu, hamburguesa, sandwich_pollo, papas_complementos, bebidas, postres, ensaladas, mc_café, cajita_feliz

def mostrar_menu(menu):
    for i, (comida, precio) in enumerate(menu.items(), start = 1):
        print(f'{i}. {comida}: {precio}')
        
def agregar_carrito(opcion, eleccion_menu):
    if opcion == len(eleccion_menu):
        return
    
    menu_comida = list(eleccion_menu.keys())
    eleccion_comida = menu_comida[opcion - 1]
    carrito_de_compras.update({eleccion_comida: eleccion_menu[eleccion_comida]})

carrito_de_compras = {}

print('Bienvenido a nuestro servicio de comida rápida')
print('Ofrecemos una amplia variedad de opciones deliciosas y rápidas para satisfacer tu apetito.')
print('¡Esperamos que disfrutes de tu comida con nosotros!')
print('Aquí puedes ver todo lo que tenemos para ofrecerte')
print()

eleccion = True
while eleccion:
    mostrar_menu(menu)
    print()
    opcion = input('Seleccione una opcion: ')
    print()
    
    if opcion == '1':
        print('Ha elegido la sección de Hamburguesas')
        print('A continuación, nuestras opciones disponibles:')
        print()
        mostrar_menu(hamburguesa)
        print()
        opcion1 = int(input('Seleccione una opcion: '))
        print()
        agregar_carrito(opcion1, hamburguesa)
        print('Su pedido se ha agregado al carrito')
        
    elif opcion == '2':
        print('Ha elegido la sección de Sandwich de pollo')
        print('A continuación, nuestras opciones disponibles:')
        print()
        mostrar_menu(sandwich_pollo)
        print()
        opcion1 = int(input('Seleccione una opcion: '))
        print()
        agregar_carrito(opcion1, sandwich_pollo)
        print('Su pedido se ha agregado al carrito')
        
    elif opcion == '3':
        print('Ha elegido la sección de Papas y complementos')
        print('A continuación, nuestras opciones disponibles:')
        print()
        mostrar_menu(papas_complementos)
        print()
        opcion1 = int(input('Seleccione una opcion: '))
        print()
        agregar_carrito(opcion1, papas_complementos)
        print('Su pedido se ha agregado al carrito')
        
    elif opcion == '4':
        print('Ha elegido la sección de Bebidas')
        print('A continuación, nuestras opciones disponibles:')
        print()
        mostrar_menu(bebidas)
        print()
        opcion1 = int(input('Seleccione una opcion: '))
        print()
        agregar_carrito(opcion1, bebidas)
        print('Su pedido se ha agregado al carrito')
        
    elif opcion == '5':
        print('Ha elegido la sección de Postres')
        print('A continuación, nuestras opciones disponibles:')
        print()
        mostrar_menu(postres)
        print()
        opcion1 = int(input('Seleccione una opcion: '))
        print()
        agregar_carrito(opcion1, postres)
        print('Su pedido se ha agregado al carrito')
        
    elif opcion == '6':
        print('Ha elegido la sección de Ensaladas')
        print('A continuación, nuestras opciones disponibles:')
        print()
        mostrar_menu(ensaladas)
        print()
        opcion1 = int(input('Seleccione una opcion: '))
        print()
        agregar_carrito(opcion1, ensaladas)
        print('Su pedido se ha agregado al carrito')
        
    elif opcion == '7':
        print('Ha elegido la sección de Mc Café')
        print('A continuación, nuestras opciones disponibles:')
        print()
        mostrar_menu(mc_café)
        print()
        opcion1 = int(input('Seleccione una opcion: '))
        print()
        agregar_carrito(opcion1, mc_café)
        print('Su pedido se ha agregado al carrito')
        
    elif opcion == '8':
        print('Ha elegido la sección de Cajita Feliz')
        print('A continuación, nuestras opciones disponibles:')
        print()
        mostrar_menu(cajita_feliz)
        print()
        opcion1 = int(input('Seleccione una opcion: '))
        print()
        agregar_carrito(opcion1, cajita_feliz)
        print('Su pedido se ha agregado al carrito')
        
    elif opcion == '9':
        print('Ha elegido Armar tu combo personalizado')
        mostrar_menu()
        
    elif opcion == '10':
        print('Muchas gracias por su visita!')
        eleccion = False
    else: 
        print('Por favor, ingrese un número de opción valido.')
        continue
    
    if eleccion:
        while True:
            repetir = input('¿Desea agregar algo mas al carrito? (SI/NO): ').lower()
            print()
            if repetir == 'si':
                break
            elif repetir == 'no':
                eleccion = False
                break
            else:
                print('Ingrese una opcion valida')
    
print('Estamos preparando su pedido.')
print('Incluye los siguientes elementos:')
for comida, precio in carrito_de_compras.items():
    print(f'{comida}: {precio}')
print()

carrito = list(carrito_de_compras.values())
monto_total = sum(carrito)
print(f'Monto total de su pedido: {monto_total}')
print()
print('¡Gracias por elegirnos y disfrute de su comida!')