import random

def adivina_numero_computador(x):

    print('======================')
    print('¡Bienvenido al Juego!')
    print('======================')
    print(f'Selecciona un numero entre 1 y {x}')

    limite_inferior = 1 
    limite_superior = x

    respuesta = ""

    while respuesta != "c":
        #generar una prediccion
        if limite_inferior != limite_superior:
            prediccion = random.randint(limite_inferior, limite_superior)
        else:
            prediccion = limite_inferior #podria ser el limite superior porque son iguales
        
        #Obtener una respuesta del usuario
        respuesta = input(f'Mi prediccion es: {prediccion} \nSi es muy alta ingresa A. Si es muy pequeña ingresa B. Si es correcta ingresa C').lower()

        if respuesta == "a":
            limite_superior = prediccion -1 
        elif respuesta == "b":
            limite_inferior = prediccion + 1

    print(f'¡Si, la computadora adivinó tu número correctamente {prediccion}')

adivina_numero_computador(7)