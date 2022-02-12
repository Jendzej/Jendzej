#include <iostream>

using namespace std;

int silnia(int liczba){
    int licznik,l;
    l = liczba -1;
    for(int i=liczba-1; i!=1; i--) {
        licznik = i;
        liczba = liczba*licznik;
        l-=1;
    }
    if (l!=1) {
        silnia(liczba);
        }
    return liczba;
}
int main()
{
    int liczba, wynik_silni;
    cout << "Podaj liczbe" << endl;
    cin >> liczba;
    wynik_silni = silnia(liczba);
    cout << wynik_silni << endl;
}
