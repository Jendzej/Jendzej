import speech_recognition as sr
from turtle import *
from MODULY import *

r = sr.Recognizer()
jezyk = 'pl-PL'

polecenia = {
    "start" : "zakrec(strzalka, wybrany_kolor)"
}
wybory = ["niebieski", "czerwony"]
wybrany_kolor = ""

circle_draw = Turtle()
circle_draw.hideturtle()
circle_draw.speed(0)
Polkole_prawe(circle_draw)
Polkole_lewe(circle_draw)

strzalka = Turtle()
strzalka.penup()
strzalka.shapesize(7,7,3)

text_turtle = Turtle()
text_turtle.penup()
text_turtle.speed(0)
text_turtle.hideturtle()
text_turtle.goto(-300, -250)
text_turtle.write("Wybierz kolor (niebieski/czerwony)",font=('Arial', 22, 'normal'))
text_turtle.goto(-300, -280)
text_turtle.write("A następnie powiedz 'start' by zakrecic kolem!",font=('Arial', 22, 'normal'))

while True:
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration = 1)
        print('- Powiedz cokolwiek:')
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio, language = jezyk)
            print('Powidziałeś:', text)
            text = text.lower()
            text_lista = text.split(" ")
            for slowa in text_lista:
                if slowa in polecenia:
                    eval(polecenia[slowa])
                if slowa in wybory:
                    wybrany_kolor = slowa
        except:
            print("Nie rozpoznaje co mowisz lub wystapil jakis blad :///")