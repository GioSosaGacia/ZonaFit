
'''
    La función raise se usa para indicar que se ha producido un error o una condición excepcional.
    La información sobre el error se captura en un objeto de excepción.
    La función reraise se usa para propagar una excepción controlada por la cadena de llamadas.
'''

class ConvertidorTemperatura:
#SI ESTA EN MAYUSCULA QUIERE DECIR QUE ES UNA CONSTANTE, YA QUE NO SE VA A MODIFICAR/CAMBIARA EL VALOR
    MAX_CELCIUS = 100
    MAX_FAHRENHEIT = 213

    @classmethod
    def c_f(cla,celcius):
        if celcius > cla.MAX_CELCIUS:
            raise ValueError(f'Temperatura en grados celcius demaciado alta: {celcius}')
        return celcius * 9/5 + 32

    @classmethod
    def f_c(cls,fahrenheit):
        if fahrenheit > cls.MAX_FAHRENHEIT:
            raise  ValueError(f'Temperatura en grados fahrenheit demaciado alta: {fahrenheit}')
        return (fahrenheit-32) * 5/9

if __name__ == '__main__':
    resultado = ConvertidorTemperatura.c_f(95)
    print(f'15  C a F: {resultado:.2f}')
    resultado = ConvertidorTemperatura.f_c(59)
    print(f'F a C: {resultado:.2f}')



