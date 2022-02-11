import random
 
plik = open('slowka.txt')                                                                               #otwarcie pliku ze slowkami
pl = []                    
ang = []                                                                                                #listy do slowek oraz najwyszych wynikow
najwynik = []                 
for line in plik:                                                                                       #rozdzielanie slowek na listy
    rozdzielone = line.split(" ")
    pl.append(rozdzielone[0])
    ang.append(rozdzielone[1].rstrip())

print("==============")
print("Nauka slowek")                                                                                   #prowizoryczna oprawa graficzna
print("==============\n")
with open('wyniki.txt') as wynikiplik:                                                                  #odczytanie najwyzszego wyniku
    for line in wynikiplik:
        odczytwynik = line.split(" z ")
        najwynik.append(odczytwynik[0].strip())
try:
    print(f"Najwiecej poprawnych odpowiedzi = {max(najwynik)}\n")
except:
    print("Tutaj pojawi się najlepszy wynik!\n")
liczbapowt = int(input("Podaj liczbe slowek do przetlumaczenia: "))                                     #wybranie liczby slowek
jakie = input("Z angielskiego na polski (wpisz anpl) czy z polskiego na angielski (wpisz plan)?")       #wybranie 'trybu' nauki
print("\nPodaj znaczenie podanych słówek: ")
wynik = 0                                                                                               #zmienna z wynikiem
if jakie == "plan":                                                                                     #petla dla trybu plan
    for i in range(liczbapowt):
        los = random.randint(0,len(pl)-1)
        odp = input(pl[los]+" - ")
        odp = odp.lower()
        if odp == ang[los]:
            print("\nDobrze!\n")
            wynik+=1
        else:
            print(f"\nZle! Poprawna odpowiedz to {ang[los]}\n")
if jakie == "anpl":                                                                                     #petla dla trybu anpl
    print("\nBEZ POLSKICH ZNAKOW!!\n")
    for i in range(liczbapowt):
        los = random.randint(0,len(pl)-1)
        odp = input(ang[los]+" - ")
        odp = odp.lower()
        if odp == pl[los]:
            print("\nDobrze!\n")
            wynik+=1
        else:
            print(f"\nZle! Poprawna odpowiedz to {pl[los]}\n")
procent = wynik/liczbapowt*100                                                                           #uzyskanie procentowego wyniku
print(f"Twoj wynik to {wynik} z {liczbapowt} poprawnych odpowiedzi! ({procent}%)")                       #wypisanie wyniku
zapis = input("Zapisac wynik? (napis tak/nie): ")
if zapis == "tak":
    with open('wyniki.txt', 'a') as f:
        f.write(f"\n{wynik} z {liczbapowt} poprawnych odpowiedzi! {procent}")                            #zapisanie wyniku do pliku
        f.close()