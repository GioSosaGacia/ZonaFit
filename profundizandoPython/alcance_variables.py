'''alcance de variables tambien conocido como (scope)'''
#variables definidas fuera de cualquier bloque de codigo son conocidas como variable-s globales

variable_global = 'Variable global'

def imprimir():
    #al utilizar una variable global dentro de una funcion o bloque de codigo se habilita solo para modo lectura
    #si, se desea modificar su valor la debemos de declarar con global  + nombre de la variable para que active el modo escritura
    global variable_global

    #acceder a una variable global
    print(f'Variable global desde mi función: {variable_global}')

    #definicion de una variable local dentro de cualquier bloque de codigo local a la funcion
    #el alcance solo será dentro del mismo bloque o dentro de una funcion anidada
    var_local = 'Variables locales'
    print(f'Variable local desde la funcion: {var_local}')

#cambio de valor de la variable global por el uso de global dentro de nuestro bloque de codigo def imprimir()
    variable_global = 'Nuevo valor variable global'

    def funcion_anidada():
        print(f'Dentro de la funcion anidada con variable local: {var_local}')

    funcion_anidada()

imprimir()
print(variable_global)
#print(var_local) marca error variable no definida

