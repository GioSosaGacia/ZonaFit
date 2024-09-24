'''Mas de funciones anidadas u alcance de variables'''
'''Una variable local interna anidada no se puede utilizar en una funcion no anidada, solo de afuera hacia adentro'''

def funcion_externa():
    variable_local_externa = 'Variable local externa'

    def funcion_anidada():
        variable_local_anidada = 'Variable local anidada'

        #Si queremos modificar una variable local a una funcion debemos de utilizar la palabra nonlocal
        #para poder cambiar su valor, y para lectura no se debe de usar nonlocal
        nonlocal variable_local_externa
        variable_local_externa = 'Nuevo valor variable local externo'
        print(f'Valor variable local anidada: {variable_local_anidada}')

    funcion_anidada()
    print(f'Valor variable local externa: {variable_local_externa}')
    #no es posible acceder a una variable local mas interna
    #print(f'Valor variable local anidada: {variable_local_anidada}') marca error porque esta fuera de su bloque , una vez que se manda a llamar la funcion
    #termina el bloque

funcion_externa()
