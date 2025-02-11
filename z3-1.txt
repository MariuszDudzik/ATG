slownik = {}

try:
    while True:
        wiersz = input()
        if wiersz.strip() != "":
            lista = list(map(int, wiersz.split()))
            klucz = lista[0]
            wartosci = lista[1:]
            slownik[klucz] = wartosci
except EOFError:
    pass

stopnie = 0
for klucz, wartosc in slownik.items():
    zlicz = len(wartosc)
    stopnie = stopnie + zlicz

srednio = stopnie / len(slownik)

srednioStr = str(srednio)

if '.' in srednioStr:
    czesc_calkowita, czesc_dziesietna = srednioStr.split('.')
    if len(czesc_dziesietna) >= 2:
        if czesc_dziesietna[2] == "5":
            czesc_dziesietna = czesc_dziesietna[:2] + '6' + czesc_dziesietna[3:]
            srednio = float(czesc_calkowita + '.' + czesc_dziesietna)

zaokraglona = round(srednio, 2)                                                                      
print(zaokraglona)