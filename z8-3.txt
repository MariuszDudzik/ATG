def wczytaj():
    wejscie =[]
    try:
        while True:
            wiersz = input()
            if wiersz.strip() != "":
                lista = list(map(int, wiersz.split()))
                wejscie.append(lista)
        
    except EOFError:
        pass
    return wejscie


def zrob_liste_sasiedztwa(wejscie):
    lista = []
    for i in range(len(wejscie)):
        wiersz =[]
        wiersz.append(i+1)
        for j in range(0, len(wejscie[i])):
            if wejscie[i][j] >= 1:
                wiersz.append(j+1)
        lista.append(wiersz)
    return lista

class DFS():
    @staticmethod
    def dfs(lista_sasiedztwa, wierzcholek):
        def czy_odwiedzony(wierzcholek, odwiedzone):
            if wierzcholek in odwiedzone:
                return True
            else:
                return False

        def czy_pusty_stos(stos):
            if len(stos) != 0:
                return False
            else:
                return True
            
        stos = []
        odwiedzone = []
        znacznik = True
        sasiad = wierzcholek
        while znacznik:                
            if sasiad != None:
                wierzcholek = sasiad
                stos.append(wierzcholek)
                if czy_odwiedzony(wierzcholek, odwiedzone) == False:
                    odwiedzone.append(wierzcholek)
                sasiad = None
                for i in range(1, len(lista_sasiedztwa[wierzcholek-1])):            
                    if czy_odwiedzony(lista_sasiedztwa[wierzcholek-1][i], odwiedzone) == False:
                            sasiad = lista_sasiedztwa[wierzcholek-1][i]
                            break
            else:
                if czy_pusty_stos(stos) == False:
                    stos.pop(len(stos) -1)
                    if czy_pusty_stos(stos) == False:
                        wierzcholek = stos[len(stos) -1]
                        for i in range(1, len(lista_sasiedztwa[wierzcholek-1])):
                            if czy_odwiedzony(lista_sasiedztwa[wierzcholek-1][i], odwiedzone) == False:
                                sasiad = lista_sasiedztwa[wierzcholek-1][i]
                                break
                    else:
                        znacznik = False
                else:
                    znacznik = False
        return odwiedzone

class Hamilton:
    def __init__(self, lista_sasiedztwa):
        self.wierzcholek = 0
        self.lista_sasiedztwa = lista_sasiedztwa
        self.lista_zbiorow = []
        self.lista_wierzcholkow = []
        self.flaga_polhamiltonowski = False
        self.flaga_hamiltonowski = False
        self.sciezka = []
        self._zrob_liste_wierzcholkow()
        self._sciezka()
    
    def _zrob_liste_wierzcholkow(self):
        for i in range(len(self.lista_sasiedztwa)):
            self.lista_wierzcholkow.append(self.lista_sasiedztwa[i][0])
    
    def _poczatkowe_zbiory(self):
        zbior_jednoelementowy = []
        for i in range(len(self.lista_sasiedztwa)):
            if i+1 != self.wierzcholek:
                if i+1 in self.lista_sasiedztwa[self.wierzcholek - 1]:
                    zbior_jednoelementowy.append([[i+1], i+1, 1])
                else:
                    zbior_jednoelementowy.append([[i+1], i+1, float('inf')]) #elementy zbioru, akt wierzcholek, waga
        self.lista_zbiorow.append(zbior_jednoelementowy)
        

    def _sciezka(self):
        for h in range(len(self.lista_wierzcholkow)):
            # Ustawianie wierzcholka startowego
            self.wierzcholek = self.lista_wierzcholkow[h]
            self.lista_zbiorow = []
        
            self._poczatkowe_zbiory()

            # Budowanie podzbiorów
            for i in range(len(self.lista_wierzcholkow) - 2):
                powiekszony_zbior = []
                for aktualny_wierzcholek in self.lista_zbiorow[i]:
                    if aktualny_wierzcholek[2] != float('inf'):
                        for k in self.lista_wierzcholkow:
                            if k != self.wierzcholek and k not in aktualny_wierzcholek[0]:
                                if k in self.lista_sasiedztwa[aktualny_wierzcholek[1] - 1]:
                                    podzbior_temp = aktualny_wierzcholek[0] + [k]
                                    nowa_waga = aktualny_wierzcholek[2] + 1
                                    powiekszony_zbior.append([podzbior_temp, k, nowa_waga])
                self.lista_zbiorow.append(powiekszony_zbior)

            # Sprawdzenie czy istnieje cykl Hamiltona
            w = len(self.lista_wierzcholkow)
            n = len(self.lista_zbiorow) - 1
            for ostatni_podzbior in self.lista_zbiorow[n]:
                if len(ostatni_podzbior[0]) == w - 1:
                    self.flaga_polhamiltonowski = True
                    if self.wierzcholek in self.lista_sasiedztwa[ostatni_podzbior[1] - 1]:
                        self.flaga_hamiltonowski = True
                        self.sciezka = ostatni_podzbior[0]
                        break

            # Jeśli znaleziono cykl Hamiltona, przerwij
            if self.flaga_hamiltonowski:
                break
                       
                    
    def wyswietl_wynik(self):
        if not self.flaga_polhamiltonowski:
            print("Graf nie jest hamiltonowski")
        elif self.flaga_polhamiltonowski and not self.flaga_hamiltonowski:
            print("Graf jest półhamiltonowski")
        else:
            print("Graf jest hamiltonowski")
          #  wynik = f"{self.wierzcholek} " + ' '.join(map(str, self.sciezka)) + f" {self.wierzcholek}"
          #  print("Graf jest hamiltonowski: " + wynik)
            
                    
    def get_lista_zbiorow(self):
        return self.lista_zbiorow
                                                

def main():
    wejscie = wczytaj()
    lista_sasiedztwa = zrob_liste_sasiedztwa(wejscie)
    spojnosc = DFS.dfs(lista_sasiedztwa, 1)
    if len(lista_sasiedztwa) == len(spojnosc):
        objH = Hamilton(lista_sasiedztwa)
        objH.wyswietl_wynik()
    else:
        print("Graf jest niespójny")
        
             
if __name__ == "__main__":
    main()