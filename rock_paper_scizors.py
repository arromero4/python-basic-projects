import random

def jugar():
    usuario = input(f'Escoge una opcion: \npi-para piedra \npa-para papel \nti-para tijera \n').lower()
    computadora = random.choice(['pi','pa','ti'])

    if usuario == computadora:
        return '¡Empate!'
    
    if gano_el_jugador(usuario, computadora):
        return '¡Ganaste!'
    
    return '¡Perdiste'


def gano_el_jugador(jugador, oponente):
    #retornar true si gana el jugador
    #piedra gana a tijera
    #tijera gana al papel
    #papel gana a la piedra

    if((jugador == 'pi' and oponente == 'ti')
    or (jugador == 'ti' and oponente == 'pa')
    or (jugador == 'pa' and oponente == 'pi')):

        return True
    else:
        return False

print(jugar())


