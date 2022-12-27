
# Exercise 2 reference:
# https://adventofcode.com/2022/day/2

def calcula_puntuacion(turno):
    oponente = turno[0]
    jugada = turno[1]

    dicc_puntuacion={'X':1, 'Y':2, 'Z':3}
    puntuacion=0
    puntuacion += dicc_puntuacion[jugada]
    if oponente=='A':               # el oponente saca piedra
        puntuacion += 3*(jugada=='X')+6*(jugada=='Y')+0*(jugada=='Z')
    elif oponente=='B':             # el oponente saca papel
        puntuacion += 0*(jugada=='X')+3*(jugada=='Y')+6*(jugada=='Z')
    elif oponente=='C':             # el oponente saca tijera
        puntuacion += 6*(jugada=='X')+0*(jugada=='Y')+3*(jugada=='Z')
    return puntuacion



def ejercicio2(fichero):

    return sum( 
        calcula_puntuacion(turno) for turno in 
        map(lambda x: x.split(), open(fichero).readlines())
    )



def main():
    puntuacion = ejercicio2('day02/day2.txt')
    print('La puntuacion acumulada es:', puntuacion)

    
if __name__ == "__main__":
    main()