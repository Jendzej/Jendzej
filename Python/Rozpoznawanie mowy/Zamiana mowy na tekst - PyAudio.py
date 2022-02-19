import speech_recognition as sr
import time
r = sr.Recognizer()
jezyk = 'pl-PL'
zmianajezyka = "nie"
dyktowanie = "nie"
print("Powiedz 'Pokaż mi swoje opcje' aby zobaczyc dostepne komendy")
while True:    
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration = 0.1)
        print('- Powiedz cokolwiek:')
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio, language = jezyk)
            print('Powidziałeś:', text)
            if text.lower() == 'zamknij program':
                print('- Zamykam program. BYE!')
                break
            if text.lower() == 'pokaż mi swoje opcje':
                print("Dostepne komendy:\n - Dyktowanie tekstu do pliku\n - Zmiana jezyka (nieodwracalna :DDD)")
                time.sleep(2)
            if text.lower() == 'dyktowanie tekstu do pliku':
                f = open('tekst.txt', 'a')
                print("- Powiedz 'koniec dyktowania', aby zakonczyc dyktowanie! ")
                dyktowanie = "tak"
                while dyktowanie == "tak":
                    with sr.Microphone() as source:
                        r.adjust_for_ambient_noise(source, duration = 1)
                        audio = r.listen(source)
                        try:
                            pisanie = r.recognize_google(audio, language = jezyk)
                            print(f"Do pliku text.txt dopisujesz: {pisanie}")
                            if pisanie.lower() == "koniec dyktowania":
                                print("- Konczenie dyktowania do pliku...")
                                dyktowanie = "nie"
                            else:
                                f.write(pisanie+"\n")
                        except:
                            print('Przepraszam, nie mogę rozpoznać, co powiedziałeś...')
                f.close()
            if text.lower() == 'zmiana języka':
                print("Na jaki jezyk zmienic?\n - angielski\n - niemiecki\n - francuski\n - rosyjski\n - hiszpanski")
                time.sleep(2)
                zmianajezyka = "tak"
                while zmianajezyka == "tak":
                    with sr.Microphone() as source:
                        r.adjust_for_ambient_noise(source, duration = 1)
                        print("Na jaki jezyk chcesz zmienic? ")
                        audio = r.listen(source)
                        try:
                            zmiana = r.recognize_google(audio, language=jezyk)
                            print(f"Zmieniasz jezyk na {zmiana}")
                            if zmiana.lower() == "angielski":
                                jezyk = 'en-US'
                                print(f"- Zmieniono jezyk na {zmiana}")
                                zmianajezyka = "nie"
                            elif zmiana.lower() == "niemiecki":
                                jezyk = 'de-DE'
                                print(f"- Zmieniono jezyk na {zmiana}")
                                zmianajezyka = "nie"
                            elif zmiana.lower() == "francuski":
                                jezyk = 'fr-FR'
                                print(f"- Zmieniono jezyk na {zmiana}")
                                zmianajezyka = "nie"
                            elif zmiana.lower() == "rosyjski":
                                jezyk = 'ru-RU'
                                print(f"- Zmieniono jezyk na {zmiana}!!")
                                zmianajezyka = "nie"
                            elif zmiana.lower() == "hiszpanski":
                                jezyk = 'es-ES'
                                print(f"- Zmieniono jezyk na {zmiana}")
                            elif zmiana.lower() == "cofnij":
                                zmianajezyka = "nie"
                        except: 
                            print('! Przepraszam, nie mogę rozpoznać, co powiedziałeś...')
        except:
            print('Przepraszam, nie mogę rozpoznać, co powiedziałeś...')