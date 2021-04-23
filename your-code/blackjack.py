# Head
import random
import os

# Nueva tarjeta


def sacar_tarjeta():
    return random.randint(1, 12)

# Limpiar pantalla


def limpiar():
    if os.name == 'nt':
        os.system('CLS')
    if os.name == 'posix':
        os.system('clear')


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
    print()
    print('--------------------------- Blackjack ---------------------------')
    print()
    print('Objetivo: el objetivo del juego es sumar 21 puntos sin pasarse')
    print('pero además sumar más puntos de los obtenidos por el crupier.')
    print()
    print('Reglas')
    print('Regla 1: el número "1" puede tomar el valor de "1" u "11" según convenga al jugador.')
    print('Regla 2: cada numero del "2" al "10" suman el mismo valor a la partida.')
    print('Regla 3: los números "11" y "12" suman un valor de 10 a la partida.')
    print()
    print('Modo de juego')
    print('1- El crupier repartirá dos cartas descubiertas al jugador y una a sí mismo.')
    print('2- Si la suma de las cartas esta cerca de 21 puede plantarse y ceder el turno al crupier.')
    print('   por el contrario si la suma es baja puede optar por sacar otra carta, recordando que en caso')
    print('   de que la suma de sus cartas sea mayor a 21 pierde atomáticamente.')
    print('3- La jugada compuesta por un "1" y un "10", "11" o "12" se conoce como Blackjack y gana automaticamnte.')
    print('4- Si la suma de las cartas con cualquier combinación es igual a 21 gana automaticamnte.')
    print('5- Cuando el jugador no quiera más cartas se plantará, cediendo el turno al crupier.')
    print('6- Luego el crupier jugará su mano.')
    print()
    print('Menú')
    print('s - sacar nueva carta')
    print('p - plantarte con el juego actual')
    print('x - salir del juego')
    print()


limpiar()
cabecera()
jugador = input('Bien, empecemos... Ingresa tu alias de jugador: ')
print()
gamer, crupier = reparto_inicial()
suma1_g, suma2_g = suma_partida(gamer)
suma1_c, suma2_c = suma_partida(crupier)
turno = 'Jugador'
print("Tus cartas", jugador+": ", gamer)
print('Sumatoria normal:', suma1_g)
if suma2_g != 0:
    print('Sumatoria alternativa:', suma2_g)
print('-------------------------------------------',)
print("Cartas de Crupier: ", crupier)
print('Sumatoria normal:', suma1_c)
if suma2_g != 0:
    print('Sumatoria alternativa:', suma2_c)
print()
print()
respuesta = ''
while respuesta != 'x':
    if turno == 'Jugador':
        print('Tu turno', jugador)
        respuesta = input('¿que deseas hacer?: ')
    else:
        print('Tu turno Crupier')
        respuesta = input('¿que deseas hacer?: ')

    if respuesta not in 'spx':
        print('Las únicas respuestas validas son las letras "s", "p" o "x"')
        continue

    if respuesta == 'p':
        respuesta = 's'
        turno = 'Crupier'

    if respuesta == 's' and turno == 'Jugador':
        gamer, suma1_g, suma2_g = jugada_nueva(gamer)
        # Considerar hacer función para los resultados
        print("Tus cartas", jugador+": ", gamer)
        print('Sumatoria normal:', suma1_g)
        if suma2_g != 0:
            print('Sumatoria alternativa:', suma2_g)
        if suma1_g > 21:
            print("PERDISTE")
            break
        elif suma1_g == 21 or suma2_g == 21:
            print("FELICINDADES! GANASTE")
            break

    if respuesta == 's' and turno == 'Crupier':
        crupier, suma1_c, suma2_c = jugada_nueva(crupier)
        print()
        print("Cartas de Crupier: ", crupier)
        print('Sumatoria normal:', suma1_c)
        if suma2_c != 0:
            print('Sumatoria alternativa:', suma2_c)
        if suma1_c > 21:
            print("La casa pierde")
            break
        if suma1_c == 21 or suma2_c == 21:
            print("La casa gana")
            break
        if (suma1_c < 22 and suma1_c > suma1_g) and suma1_c > suma2_g:
            print("La casa gana")
            break