import random
from partida import Partida
from palabras import Palabras

class ServicesPartidas():
    pass

    def iniciar_partida(self, nombre, intentos, palabra, tipo_palabra):
        if palabra == '' and tipo_palabra == '':
            if intentos < 1 or intentos > 10:
                raise ValueError
            else:
                x=Palabras 
                indice = random.randint(1, len(x.diccionario))
                indice -= 1
                posicion = x.diccionario['%s'% indice]
                palabra = posicion['palabra']
                tipo_palabra = posicion['tipo_palabra']
                intentosTotales = intentos * len(list(palabra))
                intento = Partida(palabra, intentosTotales, tipo_palabra, nombre)
                print("La palabra es del tipo: ", tipo_palabra)
                print("\nLa palabra posee ", len(palabra), " letras")
                print("\n", intento._palabra_aciertos)
                return intento
        else:
            intentosTotales = intentos * len(list(palabra))
            intento = Partida(palabra, intentosTotales, tipo_palabra, nombre)
            print("La palabra es del tipo: ", tipo_palabra)
            print("\nLa palabra posee ", len(palabra), " letras")
            print("\n", intento._palabra_aciertos)
            return intento

    def get_random_palabra(self):
        x=Palabras
        indice = random.randint(0, len(x.diccionario))
        indice -= indice
        posicion = x.diccionario['%s'% indice]
        return posicion

    def intentar_letra(self, intento, letra):
        contador = 0
        a = False
        for l in intento._palabra: 
            if l == letra:
                intento._palabra_aciertos[contador] = letra
                a = True  
            contador += 1
        print(intento._palabra_aciertos) 
        if intento._palabra_aciertos == intento._palabra:
            intento.intentos -= 1
            return "Gano"
        elif a != True:
            intento.intentos -= 1 
            if intento.intentos == 0:
                return "Perdio"
            else:
                return "Continua"
        else:
            intento.intentos -= 1
            if intento.intentos == 0:
                return "Perdio"
            else:
                return "Continua"        
