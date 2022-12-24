
# Exercise 1 reference:
# https://adventofcode.com/2022/day/1

def ejercicio1v2(fichero):

    lista_calorias = [(i+1, sum(map(int, e.splitlines())) )
    for i,e in enumerate(open(fichero).read().split("\n\n"))]

    return max(lista_calorias,
    key=lambda t:t[1]
    )

def main():
    elfo, calorias = ejercicio1v2('day01/day1.txt')
    print('El elfo numero {} acumula el maximo de calorias: {}'.format(elfo, calorias))

if __name__ == "__main__":
    main()