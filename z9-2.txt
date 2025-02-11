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
                    if a[1] != b[1]:
                        return a[1] < b[1]
                    elif a[0] != b[0]:
                        return a[0] < b[0]
               
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

    
class LF:
    def __init__(self, lista_sasiedztwa):
        self.lista_sasiedztwa = lista_sasiedztwa
        self.lista_moc = []
        self.lista_kolejnosc = []
        self.lista_kolory_wierzcholkow = []
        self.liczba_chromatyczna = 0
        self._zrob_lista_moc()
        self._zrob_lista_kolejnosc()
        self._sortuj_sasiedztwo()
        self._kolor_poczatkowy()
        self._koloruj()
        self._liczba_chromatyczna()
        self._wypisz_wyniki()  
        
    def _sortuj_sasiedztwo(self):
        for i in range(len(self.lista_sasiedztwa)):
            if len(self.lista_sasiedztwa[i]) > 1:
                self.lista_sasiedztwa[i][1:] = HeapSort.sortowanie(self.lista_sasiedztwa[i][1:], "C")
        
    def _zrob_lista_moc(self):
        for i in range (len(self.lista_sasiedztwa)):
            self.lista_moc.append([i +1, len(self.lista_sasiedztwa[i]) - 1])
           
    def _zrob_lista_kolejnosc(self):
         self.lista_kolejnosc = HeapSort.sortowanie(self.lista_moc, "M")
            
    def _kolor_poczatkowy(self):
        for i in range (len(self.lista_sasiedztwa)):
            self.lista_kolory_wierzcholkow.append(0)
            
    def _koloruj(self):
        for i in range(len(self.lista_kolejnosc)):
            wierzcholek = self.lista_kolejnosc[i][0]
            kolor = 1
            kolory_sasiadow = []
            for j in range(1, len(self.lista_sasiedztwa[wierzcholek - 1])):
                nr_sasiada = self.lista_sasiedztwa[wierzcholek - 1][j]
                kolory_sasiadow.append(self.lista_kolory_wierzcholkow[nr_sasiada - 1])
            while kolor in kolory_sasiadow:
                kolor += 1
            self.lista_kolory_wierzcholkow[wierzcholek - 1] = kolor
            
    def _liczba_chromatyczna(self):
        maks = self.lista_kolory_wierzcholkow[0]
        for i in range(len(self.lista_kolory_wierzcholkow)):
            if maks < self.lista_kolory_wierzcholkow[i]:
                maks = self.lista_kolory_wierzcholkow[i]
        self.liczba_chromatyczna = maks
        
    def _wypisz_wyniki(self):
        print("Pokolorowanie wierzchołków:", " ".join(map(str, self.lista_kolory_wierzcholkow)))
        print(f"Liczba chromatyczna == {self.liczba_chromatyczna}")
        
                   
def main():
    lista_sasiedztwa = wczytaj()
    obj = LF(lista_sasiedztwa)
 
             
if __name__ == "__main__":
    main()