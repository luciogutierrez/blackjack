# Head
import random

# Nueva tarjeta
def sacar_tarjeta():
    return random.randint(1,12)

def reparto_inicial():
    gamer = []
    crupier = []
    gamer.append(sacar_tarjeta())
    gamer.append(sacar_tarjeta())
    crupier.append(sacar_tarjeta())
    return gamer, crupier

def suma_partida(partida):
    total1 = 0
    total2 = 0
    for num in partida:
        if num < 10:
            total1 += num
        else:
            total1 += 10
    if 1 in partida:            
        for num in partida:
            if num == 1:
                total2 += 11
            elif num > 1 and num < 10:
                total2 += num
            else:
                total2 += 10
    return total1, total2

def jugada_nueva(partida):
    partida.append(sacar_tarjeta())
    suma1, suma2 = suma_partida(partida)
    return partida, suma1, suma2

def cabecera():
    print('------------- Blackjack -------------')
    print()
    print('bienvenido')
    print()
    print('Objetivo: sumar 21 puntos sin pasarse, pero sumar más puntos de los que tiene el crupier.')
    print()
    print('Reglas')
    print('Regla 1: el 1 puede tomar el valor de 1 o 11 segun convenga.')
    print('Regla 2: los números 10, 11 y 12 tienen un valor de 10.')
    print()
    print('Modo de juego')
    print('1- El crupier repartirá dos cartas descubiertas al jugador y una a sí mismo.')
    print('2- El jugador decidirá si se planta con las cartas ya repartidas o si pide más cartas.')
    print('3- Cuando el jugador no quiera más cartas se plantará, sediendo el turno al crupier.')
    print('4- Luego el crupier jugará su mano.')
    print()
    print('Menú')
    print('s - sacar nueva carta')
    print('p - plantarte con el juego actual')
    print('c - sacar nueva carta para crupier')
    print('x - salir del juego')
    print()    

cabecera()    
gamer, crupier = reparto_inicial()
suma1_g, suma2_g = suma_partida(gamer)
suma1_c, suma2_c = suma_partida(crupier)
print("your game: ", gamer, suma1_g, suma2_g)
print("home game: ", crupier)
print()    
respuesta=''
while respuesta != 'x':
    respuesta = input('¿que deseas hacer?: ')
    if respuesta == 's':
        gamer, suma1_g, suma2_g = jugada_nueva(gamer)
        print("your game: ", gamer, suma1_g, suma2_g)
        if suma1_g > 21:
            print("PERDISTE")
            break
        elif suma1_g == 21 or suma2_g == 21:
            print("FELICINDADES! GANASTE")
            break
    elif respuesta == 'p' or respuesta == 'c':
        crupier, suma1_c, suma2_c = jugada_nueva(crupier)
        print()
        print("home game: ", crupier, suma1_c, suma2_c)
        if suma1_c > 21:
            print("La casa pierde")
            break
        if suma1_c == 21 or suma2_c == 21:
            print("La casa gana")
            break
        if (suma1_c < 22 and suma1_c > suma1_g) and suma1_c > suma2_g:
            print("La casa gana")
            break
    else:
        continue