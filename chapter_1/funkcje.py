from matematyka.funkcje_matematyczne import oblicz_kwadrat_liczby

def wylicz_kwadrat_funkcji(x):
    return x**2

def odejmij_dwie_liczby(a, b):
    return a - b

def wypisz_cokolwiek(message):
    print(message)
    return None

def podnies_alarm():
    print('ALAAAAARM!!!!')

wynik = wylicz_kwadrat_funkcji(5)
wynik = wylicz_kwadrat_funkcji(10)
wynik = odejmij_dwie_liczby(10, 4)

print(wynik)
print(wynik)
podnies_alarm()

print(print)