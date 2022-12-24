def ejercicio1(lineas):
    last=0          # calorias almacenadas por el elfo actual
    max=(0,0)       # (max_calorias, elfo) hasta el momento
    cont=0          # identificador del elfo (numero) - 1 
    for l in lineas:
        linea = l.strip()
        if linea == "":
            if last>max[0]:
                max=(last,cont+1)
            last=0
            cont+=1
        else:
            last+=int(linea)
    return max
    

def main():
    with open('day01/day1.txt','r') as fichero:
        lineas=fichero.readlines()
        maxcalorias, elfo = ejercicio1(lineas)
        print("El elfo numero",elfo,"tiene el maximo de calorias: ",maxcalorias)

if __name__ == "__main__":
    main()

