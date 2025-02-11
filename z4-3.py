lista_sasiedztwa = []
stopnie_wierzcholkow = []
ilosc_wierzcholkow = 0
ilosc_krawedzi = 0


def iloscWierzcholkow():
    global ilosc_wierzcholkow
    global lista_sasiedztwa
    ilosc_wierzcholkow = len(lista_sasiedztwa)
    print("Ilość wierzchołków:", ilosc_wierzcholkow)

    
def iloscKrawedzi():
    global ilosc_krawedzi
    global stopnie_wierzcholkow
    global lista_sasiedztwa 
    zlicz_krawedz = 0
    for i in range(ilosc_wierzcholkow):
        zlicz_krawedz += len(lista_sasiedztwa[i]) - 1   
    ilosc_krawedzi = zlicz_krawedz // 2
    print("Ilość krawędzi:", ilosc_krawedzi)

    
def stopnieWierzcholkow():
    global stopnie_wierzcholkow
    global lista_sasiedztwa
    for i in range(ilosc_wierzcholkow):
        stopnie_wierzcholkow.append(len(lista_sasiedztwa[i]) - 1)
    print("Stopnie wierzchołków:", ' '.join(map(str, stopnie_wierzcholkow)))
   

def sredniStopien():
    global stopnie_wierzcholkow
    zlicz_stopnie = 0
    for i in range(len(stopnie_wierzcholkow)):
        zlicz_stopnie += stopnie_wierzcholkow[i]
    sredni_stopien = zlicz_stopnie / len(stopnie_wierzcholkow)
    srednioStr = str(sredni_stopien)
    if '.' in srednioStr:
        czesc_calkowita, czesc_dziesietna = srednioStr.split('.')
        if len(czesc_dziesietna) > 2:
            if czesc_dziesietna[2] == "5":
                czesc_dziesietna = czesc_dziesietna[:2] + '6' + czesc_dziesietna[3:]
                sredni_stopien = float(czesc_calkowita + '.' + czesc_dziesietna)
    zaokraglona = round(sredni_stopien, 2)                                                                      
    print("Średni stopień:", f"{zaokraglona:.2f}")

    
def klasyGrafow():    
    global klasa
    global ilosc_wierzcholkow
    klasa = False
    izolowane = 0
    
    for i in range(ilosc_wierzcholkow):
        if len(lista_sasiedztwa[i]) == 1: #sprawdzam czy ilozowany wierzcholek i ile potrzebne dalej
            izolowane += 1   
    
    if ilosc_krawedzi == (ilosc_wierzcholkow * (ilosc_wierzcholkow - 1)) / 2:
        print("Jest to graf pełny")
        klasa = True

    if ilosc_wierzcholkow > 2 and ilosc_krawedzi == ilosc_wierzcholkow:
        print("Jest to cykl")
        klasa = True

    if ilosc_krawedzi == ilosc_wierzcholkow - izolowane - 1:
        liczba_stopien_1 = 0
        liczba_stopien_2 = 0
        for stopien in stopnie_wierzcholkow:
            if stopien == 1:
                liczba_stopien_1 += 1
            elif stopien == 2:
                liczba_stopien_2 += 1
        if liczba_stopien_1 == 2 and liczba_stopien_2 == (ilosc_wierzcholkow - 2):
            klasa = True
            print("Jest to ścieżka")

    if izolowane == 0 and ilosc_krawedzi == ilosc_wierzcholkow - 1:
        klasa = True
        print("Jest to drzewo")


    if izolowane == 0:
        rowne_stopnie = True
        for i in range(1, len(stopnie_wierzcholkow)):
            if stopnie_wierzcholkow[0] != stopnie_wierzcholkow[i]:
                rowne_stopnie = False
                break      
        if rowne_stopnie and len(lista_sasiedztwa[0]) >= 3:
            hiperkostka = True
            for i in range (len(lista_sasiedztwa)): # wierzcholek 
                for j in range(1, len(lista_sasiedztwa[i])): # sasiedzi wierzcholka
                    sasiad_idx = lista_sasiedztwa[i][j] - 1 # indeks sasiada
                    for k in range(1, len(lista_sasiedztwa[i])):
                        zlicz = 0
                        if lista_sasiedztwa[sasiad_idx][k] != i + 1:
                            sasiad2_idx = lista_sasiedztwa[sasiad_idx][k] - 1 # indeks oddalonego o 2
                            for l in range(0, len(lista_sasiedztwa[i])):
                                if lista_sasiedztwa[sasiad2_idx][l] in lista_sasiedztwa[i]: 
                                    zlicz += 1
                            if zlicz != 2:
                                hiperkostka = False
                                break
                    if not hiperkostka:
                        break
            if hiperkostka:
                klasa = True
                print("Jest to hiperkostka")


    if not klasa:
        print("Graf nie należy do żadnej z podstawowych klas")
        
def main():
    
    try:
        while True:
            wiersz = input()
            if wiersz.strip() != "":
                lista = list(map(int, wiersz.split()))
                lista_sasiedztwa.append(lista)
    except EOFError:
        pass
    
    iloscWierzcholkow()
    iloscKrawedzi()
    stopnieWierzcholkow()
    sredniStopien()
    klasyGrafow()
    
  
if __name__ == "__main__":
    main()