# Head
import random
import os

# Nueva tarjeta
def sacar_tarjeta():
    return random.randint(1, 12)

# Limpiar pantalla
def limpiar_pantalla():
    if os.name == 'nt':
        os.system('CLS')
    if os.name == 'posix':
        os.system('clear')

# Reparto inicial de cartas
def reparto_inicial():
    gamer = []
    crupier = []
    gamer.append(sacar_tarjeta())
    gamer.append(sacar_tarjeta())
    crupier.append(sacar_tarjeta())
    return gamer, crupier

# Calculo del score de cada jugador
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

# nueva jugada
def jugada_nueva(partida):
    partida.append(sacar_tarjeta())
    suma1, suma2 = suma_partida(partida)
    return partida, suma1, suma2

# cabecera principal
def cabecera():
    print()
    print('------------------------ Solitaire Blackjack ------------------------')
    print()
    print('Objetivo')
    print('El objetivo del juego es sumar 21 puntos sin pasarse')
    print('pero además sumar más puntos de los obtenidos por el crupier.')
    print()
    print('Reglas')
    print('Regla 1: El número "1" puede tomar el valor de "1" u "11" según convenga al jugador.')
    print('Regla 2: Cada número del "2" al "10" suman el mismo número de puntos a la partida.')
    print('Regla 3: Los números "11" y "12" suman 10 puntos a la partida.')
    print()
    print('Modo de juego')
    print('1- El crupier repartirá dos cartas descubiertas al jugador y una a sí mismo.')
    print('2- Si la suma de las cartas está cerca de 21 puede plantarse y ceder el turno al crupier.')
    print('3- Si la suma es baja puede optar por sacar otra carta.')
    print('4- Si la suma de las cartas es mayor a 21 pierde automáticamente.')
    print('5- Si la suma de las cartas con cualquier combinación es igual a 21 gana automáticamente.')
    print('6- La jugada compuesta por un "1" + un "10, 11 u 12" se conoce como Blackjack y gana automáticamente.')
    print('7- Cuando el jugador no quiera más cartas se plantará, cediendo el turno al crupier.')
    print('8- El jugador jugará la partida del crupier para determinar al vencedor.')
    print('9- En caso de empate el crupier deberá sacar otra carta para romper el empate.')
    print()

# menú
def menu():
    print('Menú')
    print('s - Sacar nueva carta')
    print('p - Plantarte y pasar el turno al crupier')
    print()


# Módulo principal
limpiar_pantalla()
cabecera()
print('Bien, empecemos...')
jugador = input('Ingresa tu alias de jugador: ')
print()

while True:
    limpiar_pantalla()
    print()
    print('------------------------ Solitaire Blackjack ------------------------')
    print()
    menu()
    gamer, crupier = reparto_inicial()
    suma1_g, suma2_g = suma_partida(gamer)
    suma1_c, suma2_c = suma_partida(crupier)
    turno = 'Jugador'
    print("Tus cartas", jugador+": ", gamer)
    print('Sumatoria normal:', suma1_g)
    if suma2_g != 0:
        print('Sumatoria alternativa:', suma2_g)
    print('------------------------',)
    print("Cartas de Crupier: ", crupier)
    print('Sumatoria normal:', suma1_c)
    if suma2_g != 0:
        print('Sumatoria alternativa:', suma2_c)
    print()
    print()
    while True:
        if suma1_g == 21 or suma2_g == 21:
            print("(: FELICINDADES! GANASTE")
            break

        if suma1_c == 21 or suma2_c == 21:
            print("(: LA CASA GANA!")
            break

        if suma2_g == 0:
            if suma1_c > 10:
                if suma1_c > suma1_g or suma2_c > suma1_g:
                    print("(: LA CASA GANA!")
                    break

        if suma2_g > 0 and suma2_g < 22:
            if suma1_c > suma1_g and suma1_c > suma2_g:
                print("(: LA CASA GANA!")
                break

        if turno == 'Jugador':
            print('Tu turno', jugador)
            respuesta = input('¿que deseas hacer?: ')
        else:
            print('Turno del Crupier')
            respuesta = input('¿que deseas hacer?: ')

        if respuesta not in 'sp':
            print('Las únicas respuestas validas son las letras "s", "p"')
            continue

        if respuesta == 'p':
            respuesta = 's'
            turno = 'Crupier'

        if respuesta == 's' and turno == 'Jugador':
            gamer, suma1_g, suma2_g = jugada_nueva(gamer)
            print()
            print("Tus cartas", jugador+": ", gamer)
            print('Sumatoria normal:', suma1_g)
            if suma2_g != 0:
                print('Sumatoria alternativa:', suma2_g)
            if suma1_g > 21:
                print("): PERDISTE")
                break
            if suma1_g == 21 or suma2_g == 21:
                print("(: FELICINDADES! GANASTE")
                break

        if respuesta == 's' and turno == 'Crupier':
            crupier, suma1_c, suma2_c = jugada_nueva(crupier)
            print()
            print("Cartas de Crupier: ", crupier)
            print('Sumatoria normal:', suma1_c)
            if suma2_c != 0:
                print('Sumatoria alternativa:', suma2_c)
            if suma1_c > 21:
                print("): LA CASA PIERDE!")
                break
            if suma1_c == 21 or suma2_c == 21:
                print("(: LA CASA GANA!")
                break
            if (suma1_c < 22 and suma1_c > suma1_g) and suma1_c > suma2_g:
                print("(: LA CASA GANA!")
                break

    while True:
        print('')
        print('-------------------------------')
        partida = input('Deseas jugar otra partida s/n: ')
        if partida not in 'sn':
            print('Las únicas respuestas validas son las letras "s", "n"')
            continue
        if partida in 'ns':
            break

    if partida == 's':
        continue

    if partida == 'n':
        break
