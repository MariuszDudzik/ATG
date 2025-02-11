try:
    macierz = []
    krawedzie = 0
    while True:
        wiersz = input()
        if wiersz == "":
            break
        macierz.append([int(x) for x in wiersz.split()])
except EOFError:
    pass
    
    skierowany = False 
    for i in range(0, len(macierz)):
        for j in range(0, len(macierz[i])):
            if macierz[i][j] != macierz[j][i]:
                skierowany = True
                break
    if skierowany:
        print("Graf jest skierowany")
    else:
        print("Graf jest nieskierowany")

except (ValueError):
    print("BŁĄD")
