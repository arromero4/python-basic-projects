#adivinar un numero en un rango especifico
import random


def adivina_el_numero(x):

    print('======================')
    print('¡Bienvenido al Juego!')
    print('======================')
    print('Tu meta es adivinar el número generado por la computadora')

    numero_aleatorio = random.randint(1,x) #aleatorio entre 1 y x
    
    prediccion = 0

    while prediccion != numero_aleatorio:
        #el usuario ingresa un numero
        prediccion = int(input(f"Adivina un numero entre un numero y {x}: "))

        if prediccion <= numero_aleatorio:
            print("Intenta otra vez, este numero es muy pequeño!")
        elif prediccion > numero_aleatorio:
            print("Intenta otra vez, este numero es muy grande!")
    
    print(f"¡Felicitaciones adivinaste el numero {numero_aleatorio} correctamente.")


adivina_el_numero(10)