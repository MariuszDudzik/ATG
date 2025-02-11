try:
    wejscie = input()
    lista = wejscie.split()
    listaInt = [int(i) for i in lista]
except (EOFError, ValueError):
    print("Błąd")
sumaW = 0
for i in range(0, len(listaInt)):
    sumaW = sumaW + listaInt[i]
if sumaW % 2 != 0:
    print("NIE")
else:
    element0 = None
    znacznik = True
    while znacznik and listaInt:
        listaInt.sort(reverse=True)
        if listaInt[0] == 0:
            print("TAK")
            znacznik = False
            break
        else:
            element0 = listaInt[0]
            listaInt.pop(0)
            if len(listaInt) >= element0:
                for i in range(0, element0):
                    if listaInt[i] > 0:
                        listaInt[i] -= 1
                    else:
                        print("NIE")
                        znacznik = False
                        break
            else:
                print("NIE")
                znacznik = False
