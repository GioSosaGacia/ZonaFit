from Zona_fit_app.ClienteDao import ClienteDAO
from Zona_fit_app.cliente import Cliente

print('***Clientes de Zona Fit (GYM)***')
opcion = None
while opcion != 5:
    print('''Menu:
        1. Listar clientes
        2. Agregar cliente
        3. Modificar cliente
        4. Eliminar cliente
        5. Salir
    ''')
    opcion = int(input('Escribe tu opcion: '))
    if opcion == 1: #Listar cliente
        clientes = ClienteDAO.seleccionar()
        print('\n*** Listado de clientes ***')
        for cliente in clientes:
            print(cliente)
        print()
    elif opcion == 2:
        nombre_var = input('Escribe el nombre del cliente: ')
        apellido_var = input('Escribe el apellido del cliente: ')
        membresia_var = input('Escribe el numero de la membresia: ')
        cliente = Cliente(nombre=nombre_var, apellido=apellido_var, membresia=membresia_var)
        clientes_insertados = ClienteDAO.insertar(cliente)
        print(f'Clientes insertados: {clientes_insertados}\n')
    elif opcion == 3: #modificar cliente
        id_cliente_var = int(input('Escribe el id del cliente a modificar: '))
        nombre_var = input('Escribe el nombre del cliente: ')
        apellido_var = input('Escribe el apellido del cliente: ')
        membresia_var = input('Escribe el membresia del cliente: ')
        cliente = Cliente(id_cliente_var,nombre_var,apellido_var,membresia_var)
        clientes_actualizazdos = ClienteDAO.actualizar(cliente)
        print(f'Clientes modificados: {clientes_actualizazdos}\n')
    elif opcion == 4:
        id_cliente_var = int(input('Escribe el id del cliente a eliminar: '))
        cliente = Cliente(id=id_cliente_var)
        clientes_eliminados = ClienteDAO.eliminar(cliente)
        print(f'Clientes eliminados: {clientes_eliminados}\n')
    else:
        print('Salimos de la aplicacion....')
