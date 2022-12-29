
# Exercise 4 reference:
# https://adventofcode.com/2022/day/4

def verifica_solape_total(ind, elfo1, elfo2):
    ini1, fin1 = elfo1.split('-')
    ini2, fin2 = elfo2.split('-')
    if int(ini1) < int(ini2):
        print("La pareja de elfos {} tiene solape: {}".format(ind,int(fin2) <= int(fin1)))
        return int(fin2) <= int(fin1)
    elif int(ini1) > int(ini2): 
        print("La pareja de elfos {} tiene solape: {}".format(ind,int(fin1) <= int(fin2)))
        return int(fin1) <= int(fin2)
    else:
        print("La pareja de elfos {} tiene solape: {}".format(ind,True))
        return True


def ejercicio4(fichero):

    return sum(
        map(
        lambda linea: verifica_solape_total(linea[0],*linea[1].strip().split(',')),
        enumerate(open(fichero).readlines())
        )
    )

def main():
    num_solapes=ejercicio4('day04/day4.txt')
    print("El numero total de parejas con solape es", num_solapes)

if __name__ == "__main__":
    main()