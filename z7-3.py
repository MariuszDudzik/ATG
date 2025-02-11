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


def zrob_liste_sasiedztwa(macierz):
    lista_sasiedztwa = []
    for i in range(len(macierz)):
        wierzcholek = []
        wierzcholek.append(i+1)
        for j in range(len(macierz[i])):
            if macierz[i][j] > 0:
                wierzcholek.append([j+1, macierz[i][j]])
        lista_sasiedztwa.append(wierzcholek)
    return lista_sasiedztwa


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
    
    def znajdz_max(self):
        maks = self.odleglosci[0]
        index = 0
        for i in range(1, len(self.odleglosci)):
            if self.odleglosci[i] > maks:
                maks = self.odleglosci[i]
                index = i
        return maks
        
    def wyswietl_odleglosci(self):
        for i in range(len(self.odleglosci)):
            print(f"{i+1} = {self.odleglosci[i]}")
            
            
class SredPer:
    def __init__(self, lista_sasiedztwa, ilosc_w):
        self.lista = []
        self.srednica = 0
        self.peryferia = []
        self._oblicz_srednice(lista_sasiedztwa, ilosc_w)
        self._peryferia()
    
    def _oblicz_srednice(self, lista_sasiedztwa, ilosc_w):
        for i in range(1, ilosc_w +1):
            dObj = Dijkstra(lista_sasiedztwa, ilosc_w, i)
            maks = dObj.znajdz_max()
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
        
    def get_srednica(self):
        return self.srednica
    
    def wyswietl_peryferia(self):
            print(' '.join(map(str, self.peryferia)))
            
    def get_peryferia(self):
        return self.peryferia
        
                          
def main():
    wejscie = wczytaj() 
    ilosc_w = len(wejscie)
    lista_sasiedztwa = zrob_liste_sasiedztwa(wejscie)
    midObj = SredPer(lista_sasiedztwa, ilosc_w) 
    midObj.wyswietl_peryferia()


if __name__ == "__main__":
    main()
