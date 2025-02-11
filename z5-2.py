def wczytaj():
    wejscie =[]
    try:
        while True:
            wiersz = input()
            if wiersz.strip() != "":
                lista = list(wiersz.split())
                wejscie.append(lista)
        
    except EOFError:
        pass
    return wejscie

def przerob(wejscie):
    listaA = []
    for i in range(len(wejscie)):
        listaB = []
        for j in range(len(wejscie[i])):
            spr = int(wejscie[i][j])
            listaB.append(spr)
        listaA.append(listaB)    
    return listaA  


def bledy_wejscia(wejscie):
    znacznik = True
    lista_wierzcholkow = []
    try:
        for i in range(len(wejscie)):
            for j in range(len(wejscie[i])):
                spr = int(wejscie[i][j])
    except ValueError:
        znacznik = False
        
    wejscie = przerob(wejscie) 
    lista_sasiedztwa = wejscie[:-1]
                       
    for i in range(len(lista_sasiedztwa)):
        lista_wierzcholkow.append(lista_sasiedztwa[i][0])
        
    znk = 1
    for i in range(len(lista_wierzcholkow)):
        if lista_wierzcholkow[i] != znk:
            znacznik = False
            break
        else:
            znk += 1
            
    for i in range(len(lista_sasiedztwa)):
        for j in range(len(lista_sasiedztwa[i])):
            if lista_sasiedztwa[i][j] not in lista_wierzcholkow:
                znacznik = False
                break
    if len(wejscie[-1]) != 1:
        znacznik = False
        
    for i in range(len(lista_sasiedztwa)):
        for j in range(1, len(lista_sasiedztwa[i])):
            if lista_sasiedztwa[i][j] == lista_sasiedztwa[i][0]:
                znacznik = False
                break
                
    for i in range(len(lista_sasiedztwa)):
        for j in range(2, len(lista_sasiedztwa[i])):
            x = lista_sasiedztwa[i][j-1]
            y = lista_sasiedztwa[i][j]
            if y < x:
                znacznik = False
                break
                
    for i in range(len(lista_sasiedztwa)-1):
        x = lista_sasiedztwa[i][0]
        y = lista_sasiedztwa[i+1][0]
        if y > x:
            zncznik = False
            break
        
    return znacznik
        
def czy_odwiedzony(wierzcholek, odwiedzone):
    if wierzcholek in odwiedzone:
        return True
    else:
        return False
    
def push_stos(wierzcholek, stos):
    stos.append(wierzcholek)
    return stos
    
def push_odwiedzone(wierzcholek, odwiedzone):
    odwiedzone.append(wierzcholek)
    return odwiedzone
    
def pop_stos(stos):
    stos.pop(len(stos)-1)
    return stos
    
def get_top_stos(stos):
    return stos[len(stos)-1]
    
def czy_pusty_stos(stos):
    if len(stos) != 0:
        return False
    else:
        return True
    
def czy_spojny(lista_sasiedztwa, odwiedzone):
    znacznik = True
    for i in range(len(lista_sasiedztwa)):
        w = lista_sasiedztwa[i][0]
        if w not in odwiedzone:
            znacznik = False
            break
    return znacznik

def main():
    wejscie = wczytaj()
    stos = []
    odwiedzone = []
    znacznik = bledy_wejscia(wejscie)
    if znacznik == True:
        wejscie = przerob(wejscie)
        lista_sasiedztwa = wejscie[:-1]
        wierzcholek = wejscie[len(wejscie)-1][0]
        znacznik = True
        sasiad = wierzcholek
        while znacznik:
            if sasiad != None:
                wierzcholek = sasiad
                stos = push_stos(wierzcholek, stos)
                if czy_odwiedzony(wierzcholek, odwiedzone) == False:  
                    odwiedzone = push_odwiedzone(wierzcholek, odwiedzone)
                sasiad = None
                for i in range(1, len(lista_sasiedztwa[wierzcholek-1])):
                    if czy_odwiedzony(lista_sasiedztwa[wierzcholek-1][i], odwiedzone) == False:
                        if sasiad == None:
                            sasiad = lista_sasiedztwa[wierzcholek-1][i]
                        else:
                            if sasiad > lista_sasiedztwa[wierzcholek-1][i]:
                                sasiad = lista_sasiedztwa[wierzcholek-1][i]
            else:
                if czy_pusty_stos(stos) == False:
                    stos = pop_stos(stos)
                    if czy_pusty_stos(stos) == False:
                        wierzcholek = get_top_stos(stos)
                        for i in range(1, len(lista_sasiedztwa[wierzcholek-1])):
                            if czy_odwiedzony(lista_sasiedztwa[wierzcholek-1][i], odwiedzone) == False:
                                if sasiad == None:
                                    sasiad = lista_sasiedztwa[wierzcholek-1][i]
                                else:
                                    if sasiad > lista_sasiedztwa[wierzcholek-1][i]:
                                        sasiad = lista_sasiedztwa[wierzcholek-1][i]
                    else:
                        znacznik = False
                else:
                    znacznik = False

        if czy_spojny(lista_sasiedztwa, odwiedzone):
            print("Porządek DFS:", ' '.join(map(str, odwiedzone)))
            print("Graf jest spójny")
        else:
            print("Graf jest niespójny")
    else:
        print("BŁĄD")

if __name__ == "__main__":
    main()