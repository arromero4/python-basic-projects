import random
import string
from palabras import palabras
from ahorcado_diagrama import vidas_diccionario_visual

def obtener_palabra_valida(palabras):
    #seleccionar una palabra al azar de la lista
    palabra = random.choice(palabras)

    while '-' in palabra or ' ' in palabra:
        palabra = random.choice(palabras)

    return palabra.upper()

def ahorcado():
    print('======================')
    print('¡Bienvenido al Juego del Ahorcado!')
    print('======================')


    palabra = obtener_palabra_valida(palabras)

    letras_por_adivinar = set(palabra)
    letras_adivinadas = set()
    abecedario = set(string.ascii_uppercase) #No ñ

    vidas = 7

    while len(letras_por_adivinar) > 0 and vidas > 0:

        print(f"Te quedan {vidas} vidas. \nHaz usado estas letras: {' '.join(letras_adivinadas)}")

        #MOSTRAR EL ESTADO ACTUAL DE LAS PALABRAS
        #si está la letra mostrarla
        #si no está la letra agregar un guion
        palabra_lista = [letra if letra in letras_adivinadas else '-' for letra in palabra]
        #mostrar estado del ahorcado
        print(vidas_diccionario_visual[vidas])
        #mostrar letras de la palabra actual separadas por un espacio
        print(f"Palabra: {' '.join(palabra_lista)}")

        letra_usuario = input("Escoge una letra: ").upper()

        #Si la letra escogida por el usuario esta en el 
        #abecedario y no está en el conjunto de letras que ya se han
        #ingresado se añade la letra al conjunto de letras ingresadas
        if letra_usuario in abecedario - letras_adivinadas:
            letras_adivinadas.add(letra_usuario)

            #Si la letra está en la palabra
            #quitar la letra del conjunto de letras pendientes por adivinar
            #si no está en la palabra, quitar una vida
            if letra_usuario in letras_por_adivinar:
                letras_por_adivinar.remove(letra_usuario)
                print('')
            else:
                vidas -= 1
                print(f"\nTu letra, {letra_usuario} no está en la palabra.")
        #si la letra escogida por el usuario ya fue ingresada
        elif letra_usuario in letras_adivinadas:
            print("\nYa escogiste esa letra, por favor escoge una letra nueva")
        else:
            print("\nEsta letra no es valida.")
    
    #el juego llega a esta linea cuando se adivina todas las letras de la palabra o cuando se agotan las vidas del jugador
    if vidas == 0:
        print(vidas_diccionario_visual[vidas])
        print(f"¡Ahorcado! Perdiste. La palabra era: {palabra}")
    else:
        print(f"¡Excelente! ¡Adivinaste la palabra: {palabra}!")


ahorcado()