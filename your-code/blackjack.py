# Proyecto 1 de IronHack - Data Analytics
# Presentado por:
# Lucio Gutiérrez
# &
# Ricardo Magaña

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
    print('________________________ Solitaire Blackjack ________________________')
    print()
    print('Objetivo')
    print('El objetivo del juego es sumar 21 puntos sin pasarse')
    print('pero además sumar más puntos de los obtenidos por el crupier.')
    print()
    print('Reglas')
    print('1- El juego genera números aleatorios entre 1 y 12.')
    print('2- El número 1 puede sumar 1 u 11 puntos a la partida según convenga al jugador.')
    print('3- Cada número del 2 al 10 suman la misma cantidad de puntos a la partida.')
    print('4- Los números 11 y 12 suman 10 puntos a la partida.')
    print()
    print('Modo de juego')
    print('1- El crupier repartirá dos cartas descubiertas al jugador y una a sí mismo.')
    print('3- Si lo considerá necesario el jugador puede optar por sacar otra carta.')
    print('4- Si la suma es mayor a 21 pierde automáticamente.')
    print('5- Si la suma es igual a 21 gana automáticamnte.')
    print('6- Un 1 + un 10, 11 u 12 se conoce como Blackjack y gana automáticamnte.')
    print('7- Cuando el jugador no quiera más cartas se plantará, cediendo el turno al crupier.')
    print()

# menú
def menu():
    print('Menú')
    print('s - sacar nueva carta')
    print('p - plantarte y pasar el turno al crupier')
    print()


if __name__ == '__main__':
    # Módulo principal
    limpiar_pantalla()
    cabecera()
    print('Bien, empecemos...')
    jugador = input('Ingresa tu alias de jugador: ')
    print()

    while True:
        limpiar_pantalla()
        print()
        print('________________________ Solitaire Blackjack ________________________')
        print()
        menu()
        gamer, crupier = reparto_inicial()
        suma1_g, suma2_g = suma_partida(gamer)
        suma1_c, suma2_c = suma_partida(crupier)
        turno = 'Jugador'
        print("Tus cartas", jugador+": ", gamer)
        print('suma normal     :', suma1_g)
        if suma2_g != 0:
            print('suma alternativa:', suma2_g)
        print('------------------------',)
        print()
        print("Cartas del Crupier: ", crupier)
        print('suma normal     :', suma1_c)
        if suma2_c != 0:
            print('suma alternativa:', suma2_c)
        print()
        while True:
            if suma1_g == 21 or suma2_g == 21:
                print("(: FELICINDADES! GANASTE")
                break

            if suma1_c == 21 or suma2_c == 21:
                print("(: LA CASA GANA!")
                break

            if suma1_c > 15:
                if suma1_c > suma1_g or suma2_c > suma1_g:
                    print("(: LA CASA GANA!")
                    break

            if suma2_g > 0 and suma2_g < 22:
                if suma1_c > suma1_g and suma1_c > suma2_g:
                    print("(: LA CASA GANA!")
                    break

            if turno == 'Jugador':
                print()
                print('Tu turno', jugador)
                respuesta = input('¿que deseas hacer?: ')
            else:
                print()
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
                print('suma normal     :', suma1_g)
                if suma2_g != 0:
                    print('suma alternativa:', suma2_g)
                if suma1_g > 21:
                    print("): PERDISTE")
                    break
                if suma1_g == 21 or suma2_g == 21:
                    print("(: FELICINDADES! GANASTE")
                    break

            if respuesta == 's' and turno == 'Crupier':
                crupier, suma1_c, suma2_c = jugada_nueva(crupier)
                print()
                print("Cartas del Crupier: ", crupier)
                print('suma normal     :', suma1_c)
                if suma2_c != 0:
                    print('suma alternativa:', suma2_c)
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
            print('_______________________________')
            print()
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