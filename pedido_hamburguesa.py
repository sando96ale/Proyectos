from menu_completo import menu, hamburguesa, sandwich_pollo, papas_complementos, bebidas, postres, ensaladas, mc_café, cajita_feliz

def mostrar_menu(menu):
    for i, (comida, precio) in enumerate(menu.items(), start = 1):
        print(f'{i}. {comida}: {precio}')
        
def agregar_carrito(opcion, eleccion_menu):
    menu_comida = list(eleccion_menu.keys())
    eleccion_comida = menu_comida[opcion - 1]
    carrito_de_compras.update({eleccion_comida: eleccion_menu[eleccion_comida]})

carrito_de_compras = {}

print('Bienvenido a nuestro servicio de comida rápida')
print('Ofrecemos una amplia variedad de opciones deliciosas y rápidas para satisfacer tu apetito.')
print('¡Esperamos que disfrutes de tu comida con nosotros!')
print('Aquí puedes ver todo lo que tenemos para ofrecerte')

while True:
    
    mostrar_menu(menu)
    opcion = input('Seleccione una opcion: ')
    
    if opcion == '1':
        print('A elegido hamburguesas')
        mostrar_menu(hamburguesa)
        opcion1 = int(input('Seleccione una opcion: '))
        agregar_carrito(opcion1, hamburguesa)
        print('Su pedido se ha agregado al carrito')
        
    elif opcion == '2':
        print('A elegido Sandwich de pollo')
        mostrar_menu(sandwich_pollo)
        opcion1 = int(input('Seleccione una opcion: '))
        agregar_carrito(opcion1, sandwich_pollo)
        print('Su pedido se ha agregado al carrito')
        
    elif opcion == '3':
        print('A elegido Papas y complementos')
        mostrar_menu(papas_complementos)
        opcion1 = int(input('Seleccione una opcion: '))
        agregar_carrito(opcion1, papas_complementos)
        print('Su pedido se ha agregado al carrito')
        
    elif opcion == '4':
        print('A elegido Bebidas')
        mostrar_menu(bebidas)
        opcion1 = int(input('Seleccione una opcion: '))
        agregar_carrito(opcion1, bebidas)
        print('Su pedido se ha agregado al carrito')
        
    elif opcion == '5':
        print('A elegido Postres')
        mostrar_menu(postres)
        opcion1 = int(input('Seleccione una opcion: '))
        agregar_carrito(opcion1, postres)
        print('Su pedido se ha agregado al carrito')
        
    elif opcion == '6':
        print('A elegido Ensaladas')
        mostrar_menu(ensaladas)
        opcion1 = int(input('Seleccione una opcion: '))
        agregar_carrito(opcion1, ensaladas)
        print('Su pedido se ha agregado al carrito')
        
    elif opcion == '7':
        print('A elegido Mc Café')
        mostrar_menu(mc_café)
        opcion1 = int(input('Seleccione una opcion: '))
        agregar_carrito(opcion1, mc_café)
        print('Su pedido se ha agregado al carrito')
        
    elif opcion == '8':
        print('A elegido Cajita Feliz')
        mostrar_menu(cajita_feliz)
        opcion1 = int(input('Seleccione una opcion: '))
        agregar_carrito(opcion1, cajita_feliz)
        print('Su pedido se ha agregado al carrito')
        
    elif opcion == '9':
        print('A elegido Armar tu combo personalizado')
        mostrar_menu()
        
    elif opcion == '10':
        print('Muchas gracias por su visita!')
        break
    else: 
        print('Por favor, ingrese un número de opción valido.')
        continue

    repetir = input('¿Desea agregar algo mas al carrito? (SI/NO): ').lower()
    if repetir != 'si':
        break

print('Su pedido es; ')
print(carrito_de_compras)

# Cambios3