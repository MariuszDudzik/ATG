import ast

slownik = ast.literal_eval(input()) # konwertowanie ciągu znaków, który wygląda jak struktura danych Pythona na odpowiedni obiekt Pythona.

liczba_pytan = int(input())
if liczba_pytan < 1 or liczba_pytan > 100:
    raise ValueError

pytania = []
while liczba_pytan > 0:
    linia = input()
    lista = list(linia.split())
    pytania.append(lista)
    liczba_pytan -= 1
    
for i in range(0, len(pytania)):
    if pytania[i][0] == "neighbours":
        klucz = int(pytania[i][1])
        sasiedzi = slownik[klucz]
        liczba_sasiadow = len(sasiedzi)
        print(liczba_sasiadow)
    elif pytania[i][0] == "connection":
        klucz = int(pytania[i][1])
        sasiad = int(pytania[i][2])
        wartosc = slownik[klucz]
        if sasiad in wartosc:
            print("Yes")
        else:
            print("No")