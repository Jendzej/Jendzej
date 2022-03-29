from turtle import *
import random

def Polkole_prawe(zolw):
    zolw.color("red")
    zolw.penup()
    zolw.goto(0,-200)
    zolw.begin_fill()
    zolw.pendown()
    zolw.circle(200, 180)
    zolw.goto(0,-200)
    zolw.end_fill()
    zolw.seth(0)
    
def Polkole_lewe(zolw):
    zolw.color("blue")
    zolw.penup()
    zolw.goto(0,-200)
    zolw.begin_fill()
    zolw.pendown()
    zolw.circle(200, -180)
    zolw.goto(0,-200)
    zolw.end_fill()
    zolw.seth(0)
    
def zakrec(zolw, wybrany_kolor):
    print(f"Wybrany przez ciebie kolor to {wybrany_kolor}")
    obroty = random.randint(15,30)
    zolw.speed(10)
    for i in range(50):
        zolw.left(obroty)
    hd = zolw.heading()    
    if hd > 90.0 and hd < 270.0:
        wynik = "niebieski"
    else:
        wynik = "czerwony"
    print(f"Wylosowano kolor - {wynik}")
    if wybrany_kolor == wynik:
        print("Brawo! Udało Ci się odgadnąć kolor!")
    else:
        print("Nie udało Ci się odgadnąć koloru :(")