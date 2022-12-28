
# Exercise 3 reference:
# https://adventofcode.com/2022/day/3

def peso_letra(letra):
    if letra.islower():
        return 1+ord(letra)-ord('a')
    else:
        return 27+ord(letra)-ord('A')


def calcula_prioridad(i,mochila):
    long_box = int(len(mochila)/2)
    box1=mochila[0:long_box]
    box2=mochila[long_box:]
    lista_repetidos=[ (letra, peso_letra(letra))
            for letra in set(box1) if letra in box2]
    print("\n--> Mochila numero",i+1,":", mochila)
    print("Compartimento 1:", box1)
    print("Compartimento 2:", box2)
    print("Articulos en ambos compartimentos:", lista_repetidos)

    return sum(letra[1] for letra in lista_repetidos)


def ejercicio3(fichero):
    return sum(
        calcula_prioridad(i,mochila.strip()) 
        for i,mochila in
        enumerate(open(fichero).readlines())
    )

def main():
    sum_prioridades=ejercicio3('day03/day3.txt')
    print('\n--> La prioridad acumulada es:', sum_prioridades)

    
if __name__ == "__main__":
    main()