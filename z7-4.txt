def bledy_wejscia(wejscie):
    znacznik = True
    if len(wejscie) < 2:
        print(len(wejscie))
        znacznik = False

    n_m = wejscie[0]
    if len(n_m) != 2:
        znacznik = False
    
    n, m = n_m    
    if n < 2 or n > 100 or m < n - 1 or m > (n * (n - 1)) // 2:
        znacznik = False

    for i in range(1, m + 1):
        a_b_w = wejscie[i]
        if len(a_b_w) != 3:
            znacznik = False
            break
        a, b, w = a_b_w
        if (a < 1 or a > n or b < 1 or b > n or
             w < 1 or w > 1000):
            znacznik = False
    return znacznik


class HeapSort:
    @staticmethod
    def sortowanie(tablica, opcja):
        def _stworz_kopiec(tablica, n):
            for i in range(n // 2 - 1, -1, -1):
                _sprawdz_dol(tablica, n, i)

        def _sprawdz_dol(tablica, n, i):
            rodzic_idx = i
            lewy_idx = 2 * i + 1
            prawy_idx = 2 * i + 2
            wiekszy_brat_idx = None

            def wiekszy(a, b):
                if opcja == "K": 
                    if a[2] != b[2]:
                        return a[2] > b[2]
                    elif a[0] != b[0]:
                        return a[0] > b[0]
                    else:
                        return a[1] > b[1]
                elif opcja == "C":
                        return a > b
                elif opcja == "M":
                    if a[0] != b[0]:
                        return a[0] > b[0]
                    elif a[0] != b[0]:
                        return a[1] > b[1]
                    else:
                        return a[2] > b[2]

            if lewy_idx < n and prawy_idx < n:
                wiekszy_brat_idx = lewy_idx if wiekszy(tablica[lewy_idx], tablica[prawy_idx]) else prawy_idx
            elif lewy_idx < n:
                wiekszy_brat_idx = lewy_idx

            if wiekszy_brat_idx is not None and wiekszy(tablica[wiekszy_brat_idx], tablica[rodzic_idx]):
                rodzic_idx = wiekszy_brat_idx

            if rodzic_idx != i:
                tablica[i], tablica[rodzic_idx] = tablica[rodzic_idx], tablica[i]
                _sprawdz_dol(tablica, n, rodzic_idx)

        n = len(tablica)
        _stworz_kopiec(tablica, n)

        for i in range(n - 1, 0, -1):
            tablica[i], tablica[0] = tablica[0], tablica[i]
            _sprawdz_dol(tablica, i, 0)
        return tablica  

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
        
        
class DSU:
    def __init__(self, n):
        self.lista_rodzic = []
        self.lista_ranga = []
        self._stworz_lista_rodzic(n) 
        self._stworz_lista_ranga(n)
            
    def _stworz_lista_rodzic(self, n):
        for i in range(1, n+1):
            self.lista_rodzic.append(i)
            
    def _stworz_lista_ranga(self, n):
        for i in range(n):
            self.lista_ranga.append(0)
                   
    def find(self, wierzcholek):
        if self.lista_rodzic[wierzcholek-1] != wierzcholek:
            self.lista_rodzic[wierzcholek-1] = self.find(self.lista_rodzic[wierzcholek-1])
        return self.lista_rodzic[wierzcholek-1]

    def union(self, krawedz):
        w1 = krawedz[0]
        w2 = krawedz[1]
        rodzic_w1 = self.find(w1)
        rodzic_w2 = self.find(w2)

        if rodzic_w1 != rodzic_w2:
            if self.lista_ranga[rodzic_w1-1] >= self.lista_ranga[rodzic_w2-1]:
                self.lista_rodzic[rodzic_w2-1] = rodzic_w1
            elif self.lista_ranga[rodzic_w1-1] < self.lista_ranga[rodzic_w2-1]:
                self.lista_rodzic[rodzic_w1-1] = rodzic_w2
            else:
                self.lista_rodzic[rodzic_w2-1] = rodzic_w1
                self.lista_ranga[rodzic_w1-1] += 1
       
    
class MST(): 
    def __init__(self, krawedzie, n):
        self.dsu = DSU(n)
        self.mst = []
        self.koszt = 0
        self._stworz_mst(krawedzie)

    def _stworz_mst(self, krawedzie):    
        for i in range(len(krawedzie)):
            if self.dsu.find(krawedzie[i][0]) != self.dsu.find(krawedzie[i][1]):
                self.dsu.union(krawedzie[i])
                self.mst.append(krawedzie[i])
                self.koszt += krawedzie[i][2]
                
    def get_mst(self):
        return self.mst
    
    def get_koszt(self):
        return self.koszt
    
    def wyswietl(self):
        print("SIEĆ PODSTAWOWA (MST):")
        for krawedz in self.mst:
            print(f"{krawedz[0]}-{krawedz[1]}: {krawedz[2]}")
            
    def wyswietl_koszt(self):
        koszt = self.get_koszt()
        print(f"Łączny czas: {koszt}")

        
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

def zamien_wierzcholki(krawedzie):
    for i in range(len(krawedzie)):
        if krawedzie[i][0] > krawedzie[i][1]:
            krawedzie[i][0], krawedzie[i][1] = krawedzie[i][1], krawedzie[i][0]
    return krawedzie


class Dijkstra:
    def __init__(self, lista_sasiedztwa, ilosc_w, wierzcholek):
        self.odleglosci = []
        self.odwiedzone = []
        self.kolejka = []
        self._ustaw_inf(ilosc_w)
        self._ustaw_start(wierzcholek)
        self._dijkstra(lista_sasiedztwa)
        
    def _ustaw_inf(self, ilosc_w):
        for i in range(ilosc_w):
            self.odleglosci.append(float('inf'))
            
    def _ustaw_start(self, wierzcholek):
        start = [wierzcholek, wierzcholek, 0]
        self.kolejka.append(start)
        self.odleglosci[wierzcholek-1] = start[2]
        
    def _dijkstra(self, lista_sasiedztwa):
        while len(self.kolejka) > 0:
            akt_wierzcholek = self.kolejka[0][1]
            akt_wartosc_drogi = self.kolejka[0][2]
            self.kolejka.pop(0)
            self.odwiedzone.append(akt_wierzcholek)
            for i in range(1,len(lista_sasiedztwa[akt_wierzcholek-1])):
                sasiad = lista_sasiedztwa[akt_wierzcholek-1][i][0] 
                droga_sasiada = lista_sasiedztwa[akt_wierzcholek-1][i][1]            
                droga_temp = akt_wartosc_drogi + droga_sasiada 
                if sasiad not in self.odwiedzone and droga_temp < self.odleglosci[sasiad-1]:
                    self.odleglosci[sasiad-1] = droga_temp
                    self.kolejka.append([akt_wierzcholek, sasiad, droga_temp])
            self.kolejka = HeapSort.sortowanie(self.kolejka, "K")
            
    def znajdz_max(self, opcja):
        maks = self.odleglosci[0]
        index = 0
        for i in range(1, len(self.odleglosci)):
            if self.odleglosci[i] > maks:
                maks = self.odleglosci[i]
                index = i
        if opcja == "I":
            return index + 1
        else: 
            return maks
        
    def get_odleglosci(self):
        return self.odleglosci
            
    def wyswietl_odleglosci(self):
        for i in range(len(self.odleglosci)):
            print(f"{i+1} = {self.odleglosci[i]}")
            
            
class Parametry:
    def __init__(self, lista_sasiedztwa, ilosc_w):
        self.lista = []
        self.srednica = 0
        self.promien = 0
        self.peryferia = []
        self.centrum = []
        self.macierz_prze = []
        self._oblicz_srednice(lista_sasiedztwa, ilosc_w)
        self._peryferia()
        self._wyznacz_promien()
        self._centrum()
    
    def _oblicz_srednice(self, lista_sasiedztwa, ilosc_w):
        for i in range(1, ilosc_w +1):
            dObj = Dijkstra(lista_sasiedztwa, ilosc_w, i)
            self.macierz_prze.append(dObj.get_odleglosci()) # dodatkowo przygotowuje macierz odleglosci
            maks = dObj.znajdz_max("M")
            self.lista.append(maks)      
        m = self.lista[0]
        for i in range(1, len(self.lista)):
            if self.lista[i] > m:
                m = self.lista[i]
        self.srednica = m
        
    def _peryferia(self):
        for i in range(len(self.lista)):
            if self.lista[i] == self.srednica:
                self.peryferia.append(i+1)
        self.peryferia = HeapSort.sortowanie(self.peryferia, "C")
        
    def _centrum(self):
        for i in range(len(self.lista)):
            if self.lista[i] == self.promien:
                self.centrum.append(i+1)
        self.centrum = HeapSort.sortowanie(self.centrum, "C")
        
    def _wyznacz_promien(self):
        self.promien = self.lista[0]
        for i in range(len(self.lista)):
            if self.promien > self.lista[i]:
                self.promien = self.lista[i]
    
    def get_promien(self):
        return self.promien
    
    def get_srednica(self):
        return self.srednica
            
    def get_peryferia(self):
        return self.peryferia 
    
    def get_centrum(self):
        return self.centrum
    
    def get_macierz_prze(self):
        return self.macierz_prze
    
    def wyswietl_parametry(self):
        print (f"\nPARAMETRY SIECI:\n"
            f"Średnica: {self.srednica}\n"
            f"Promień: {self.promien}\n"
            f"Centrum: {self.centrum}\n"
            f"Peryferium: {self.peryferia}")
        
    def wyswietl_czasy_przejazdow(self):
        print("\nCZASY PRZEJAZDÓW:")
        for i in range(len(self.macierz_prze)):
            print(' '.join(map(str, self.macierz_prze[i])))
    
            
class Listy:
    def __init__(self, krawedzie, n):
        self.lista_sasiedztwa = []
        self.lista_sasiedztwa_p = []
        self.lista_wierzcholkow = []
        self.lista_pk = []
        self.lista_grafow = []
        self.lista_mostow = []
        self.lista_komponentow = []
        self.lista_sasiedztwa = self._zrob_liste_sasiedztwa(krawedzie, n, "R")
        self.lista_sasiedztwa_p = self._zrob_liste_sasiedztwa(krawedzie, n, "P")
        self._zrob_liste_wierzcholkow()
        self.lista_grafow = self._zrob_liste_grafow(self.lista_sasiedztwa_p)
      # self._zrob_liste_mostow(krawedzie, n)
        self._zrob_liste_pk()
      # self.lista_komponentow = self._zrob_liste_komponentow(krawedzie, n)
        
    def _zrob_liste_sasiedztwa(self, krawedzie, n, opcja):
        lista_sasiedztwa = []
        for i in range(n):
            lista_sasiedztwa.append([i + 1])    
        
        for i in range(len(krawedzie)):  
            krawedz = krawedzie[i]
            if opcja == "R":
                lista_sasiedztwa[krawedz[0] - 1].append([krawedz[1], krawedz[2]])
                lista_sasiedztwa[krawedz[1] - 1].append([krawedz[0], krawedz[2]])
            else:
                lista_sasiedztwa[krawedz[0] - 1].append(krawedz[1])
                lista_sasiedztwa[krawedz[1] - 1].append(krawedz[0])
        return lista_sasiedztwa
    
    def _zrob_liste_wierzcholkow(self):
        for i in range(len(self.lista_sasiedztwa)):
            self.lista_wierzcholkow.append(self.lista_sasiedztwa[i][0])
    
    def _zrob_liste_grafow(self, lista_sasiedztwa):
        lista_w = self.lista_wierzcholkow
        lista_g = []
        while len(lista_w) > 0:
            graf = DFS.dfs(lista_sasiedztwa, lista_w[0])
            lista_g.append(graf)
            pomocnicza = []
            for i in range(len(lista_w)):
                if lista_w[i] not in graf:
                    pomocnicza.append(lista_w[i])
            lista_w = pomocnicza
        return lista_g
    
    def _zrob_liste_mostow(self, krawedzie, n):
        for i in range(len(self.lista_grafow)):
            sciezka_pierwotna = DFS.dfs(self.lista_sasiedztwa_p, self.lista_grafow[i][0])
            licznik = len(krawedzie)
            for j in range(licznik):
                nowe_krawedzie = krawedzie[:j] + krawedzie[j+1:]
                nowa_lista_sasiedztwa = self._zrob_liste_sasiedztwa(nowe_krawedzie, n, "P")
                sciezka = DFS.dfs(nowa_lista_sasiedztwa, self.lista_grafow[i][0])
                if len(sciezka_pierwotna) != len(sciezka):
                    if krawedzie[j] not in self.lista_mostow:
                        self.lista_mostow.append(krawedzie[j])
                        
    def _zrob_liste_komponentow(self, krawedzie, n):
        n_krawedzie = []
        for i in range(len(krawedzie)):
            if krawedzie[i] not in self.lista_mostow:
                n_krawedzie.append(krawedzie[i])
        nowa_lista_sasiedztwa = self._zrob_liste_sasiedztwa(n_krawedzie, n, "P")
        lista_k = self._zrob_liste_grafow(nowa_lista_sasiedztwa)
        for i in range(len(lista_k)):
            lista_k[i] = HeapSort.sortowanie(lista_k[i], "C")
        return lista_k
    
    def _zrob_liste_pk(self):
        lista_pierwotna = DFS.dfs(self.lista_sasiedztwa_p, 1)
        for wierzcholek in self.lista_wierzcholkow:
            nowa_lista_sasiedztwa = self._usun_wierzcholek(self.lista_sasiedztwa_p, wierzcholek)
            start=0
            if wierzcholek == 1:
                start = 2
            else:
                start = 1
            lista_obcieta = DFS.dfs(nowa_lista_sasiedztwa, start)
            if len(lista_obcieta) < len(lista_pierwotna) - 1:
                self.lista_pk.append(wierzcholek)

    def _usun_wierzcholek(self, lista_sasiedztwa, wierzcholek): 
        nowa_lista = []
        for sasiad in lista_sasiedztwa:
            if sasiad[0] == wierzcholek:
                nowa_lista.append([wierzcholek])
            else:
                nowi_sasiedzi = [s for s in sasiad if s != wierzcholek]
                nowa_lista.append(nowi_sasiedzi)
        return nowa_lista    
  
                
    def get_lista_wierzcholkow(self):
        return self.lista_wierzcholkow
              
    def get_lista_grafow(self):
        return self.lista_grafow
                         
    def get_lista_mostow(self):
        return self.lista_mostow   
        
    def get_lista_sasiedztwa(self):
        return self.lista_sasiedztwa
    
    def get_lista_sasiedztwa_p(self):
        return self.lista_sasiedztwa_p
    
    def get_lista_komponentow(self):
        return self.lista_komponentow
    
    def get_lista_pk(self):
        return self.lista_pk
    
    def wyswietl_mosty(self):
        print("\nMOSTY:")
        if len(self.lista_mostow) > 0:
            for i in range(len(self.lista_mostow)):
                print(' '.join(map(str, self.lista_mostow[i][:-1])))
        else:
            print("BRAK MOSTÓW") 
            
    def wyswietl_pk(self):
        if self.lista_pk:
            print("\nPUNKTY KRYTYCZNE:")
            print(" ".join(map(str, self.lista_pk)))
        else:
            print("\nPUNKTY KRYTYCZNE:")
            print("BRAK")
            

def main():
    wejscie = wczytaj()
    if bledy_wejscia(wejscie) == True:
        krawedzie = wejscie[1:]
        ilosc_w = wejscie[0][0]
        krawedzie = zamien_wierzcholki(krawedzie)
        lstObj = Listy(krawedzie, ilosc_w)
        spojnosc = lstObj.get_lista_grafow()
        if len(spojnosc) == 1:
            posortowanaTablica = HeapSort.sortowanie(krawedzie, "K")
            mstObj = MST(posortowanaTablica, wejscie[0][0])
            mst = mstObj.get_mst()
            mstObj.wyswietl()
            mstObj.wyswietl_koszt()
            lista_sasiedztwa = lstObj.get_lista_sasiedztwa()
            parObj = Parametry(lista_sasiedztwa, ilosc_w)
            parObj.wyswietl_parametry()
            parObj.wyswietl_czasy_przejazdow()
            lstObj.wyswietl_pk()
        else:
            print("BłĄD")
    else:
        print("BłĄD")

if __name__ == "__main__":
    main()