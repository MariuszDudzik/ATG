try:
    wejscieA = input()
    wejscieS = input()
    listaA = wejscieA.split()
    listaS = wejscieS.split()
    listaAInt = [int(i) for i in listaA]
    listaSInt = [int(i) for i in listaS]

    for i in range(0, len(listaAInt)):
        for j in range(0, len(listaAInt)):
            odejmowanie = (listaAInt[j] - listaAInt[i])
            if odejmowanie in listaSInt:
                if j < len(listaAInt) - 1:
                    print(1, end=' ')
                else:
                    print(1, end='')
            else:
                if j < len(listaAInt) - 1:
                    print(0, end=' ')
                else:
                    print(0, end='')
        print()
except (EOFError, ValueError):
    print("BŁĄD")
