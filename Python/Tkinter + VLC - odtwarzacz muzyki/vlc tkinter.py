from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter import Menu
import vlc
import glob

playlista = glob.glob('*.mp3')                                # lista z piosenkami
muzyka = vlc.MediaPlayer('')

def plik():                                                   # funkcja do wyboru pliku
    wyborpliku = filedialog.askdirectory()

okno = Tk()                                                   # właściwości okna
okno.title("Odtwarzacz VLC")
#okno.geometry("450x350")
okno.configure(background="#b0a8e3")

menu = Menu(okno)                                             # menu 
opcja1 = Menu(menu, tearoff=0)
opcja1.add_command(label="Wybierz folder...", command=plik, background='#b0a8e3')
menu.add_cascade(label='Folder', menu=opcja1)

napis = Label(okno, text="Odtwaczacz muzyki VLC", background='#699cb8').pack()      # napis 

Label(okno, background="#b0a8e3").pack()                        # pusta linia

Label(okno, text="Playlista:", background='#699cb8').pack(anchor=W)                 # playlista
for i in range(len(playlista)):
    l = str(i+1)
    nazwa = playlista[i]
    Label(okno, text=(l +" - "+ nazwa), background="#b0a8e3").pack(anchor=W)

Label(okno, background="#b0a8e3").pack()

Label(okno, text="Wybierz numer piosenki: ", background="#b0a8e3").pack()

wartosc = IntVar(value=1)
spinbox = Spinbox(okno, from_= 1, to=len(playlista), textvariable=wartosc, background='#699cb8').pack()

def przyciskklik():
    global muzyka
    muzyka.stop()
    muzyka = vlc.MediaPlayer(playlista[wartosc.get()-1])
    muzyka.play()

def przycisk2klik():
    global muzyka
    muzyka.pause()    

Label(okno, background="#b0a8e3").pack()

przycisk = Button(okno,text='Odtwórz', command=przyciskklik, background='#505287').pack(side=LEFT, expand=TRUE, fill=BOTH)
przycisk = Button(okno,text='▶⏸', command=przycisk2klik, background='#505287').pack(side=LEFT, expand=TRUE, fill=BOTH)

okno.config(menu=menu)
okno.mainloop()
input()
