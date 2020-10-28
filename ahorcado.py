from partida import Partida
from servicesPartidas import ServicesPartidas
from jugadores import Jugadores

class Ahorcado():

    def un_jugador(self):
        nombre = str(input("Eliga su nombre: "))
        intento = int(input("Eliga dificultad: "))
        partidas = ServicesPartidas()
        p = partidas.iniciar_partida(nombre, intento, '', '')
        for i in range(0, p.intentos):
            letra = input("\nIngrese su letra: ")
            if letra == 'salir':
                return True
            respuesta = partidas.intentar_letra(p, letra.upper())
            print(respuesta)
            if respuesta == 'Gano' or respuesta == 'Perdio':
                return True

    def dos_jugadores(self):
        dicJugadores = {}
        partidas = ServicesPartidas()
        for j in range(0, 2):
            nombre = str(input("Eliga su nombre: "))
            intento = int(input("Eliga dificultad: "))
            palabra = str(input("Ingrese palabra para %s: "%nombre))
            tipoPalabra = str(input("Ingrese la categoria: "))
            p = partidas.iniciar_partida(nombre, intento, palabra, tipoPalabra)
            for i in range(0, p.intentos):
                letra = str(input("\nIngrese su letra: "))
                if letra == 'salir':
                    return True
                respuesta = partidas.intentar_letra(p, letra.upper())
                print(respuesta)
                if respuesta == 'Gano' or respuesta == 'Perdio':
                    if j == 0:
                        dicJugadores[nombre] = p.__dict__
                        break
                    else:
                        dicJugadores[nombre] = p.__dict__
                        return True