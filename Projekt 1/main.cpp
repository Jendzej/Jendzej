#include <iostream>

using namespace std;

int main()
{
    int liczba, potega, liczba_org, licznik=1;
    cout << "Podaj liczbe, ktora chcesz spotegowac" << endl;
    cin >> liczba;
    liczba_org = liczba;
    cout << "Podaj potege" << endl;
    cin >> potega;
    while(licznik<potega){
        liczba = liczba * liczba_org;
        cout << liczba<< endl;
        licznik+=1;
    }
    cout << liczba;
    return 0;
}
