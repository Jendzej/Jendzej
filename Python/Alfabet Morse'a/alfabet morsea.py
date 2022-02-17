import os

print("ZAMIANA TEKSTU NA KOD MORSE'A")
stan = "dziala"

while stan == "dziala":
    tekst = input("Wprowadz tekst: ")
    tekst_output = ""
    for i in range(len(tekst)):
        tekst.lower()
        if tekst[i] == "a":
            tekst_output+=("• —")  
        if tekst[i] == "b":
            tekst_output+=("— • • •")
        if tekst[i] == "c":
            tekst_output+=("— • — •")
        if tekst[i] == "d":
            tekst_output+=("— • •")
        if tekst[i] == "e":
            tekst_output+=("•")
        if tekst[i] == "f":
            tekst_output+=("• • — •")
        if tekst[i] == "g":
            tekst_output+=("— — •")
        if tekst[i] == "h":
            tekst_output+=("• • • •")
        if tekst[i] == "i":
            tekst_output+=("• •")
        if tekst[i] == "j":
            tekst_output+=("• — — —")
        if tekst[i] == "k":
            tekst_output+=("— • —")
        if tekst[i] == "l":
            tekst_output+=("• — • •")
        if tekst[i] == "m":
            tekst_output+=("— —")
        if tekst[i] == "n":
            tekst_output+=("— •")
        if tekst[i] == "o":
            tekst_output+=("— — —")
        if tekst[i] == "p":
            tekst_output+=("• — — •")
        if tekst[i] == "q":
            tekst_output+=("— — • —")
        if tekst[i] == "r":
            tekst_output+=("• — •")
        if tekst[i] == "s":
            tekst_output+=("• • •")
        if tekst[i] == "t":
            tekst_output+=("— ")
        if tekst[i] == "u":
            tekst_output+=("• • — ")
        if tekst[i] == "v":
            tekst_output+=("• • • — ")
        if tekst[i] == "w":
            tekst_output+=("• — — ")
        if tekst[i] == "x":
            tekst_output+=("— • • — ")
        if tekst[i] == "y":
            tekst_output+=("— • — — ")
        if tekst[i] == "z":
            tekst_output+=("— — • • ")
        if tekst[i] == "1":
            tekst_output+=("• — — — — ")
        if tekst[i] == "2":
            tekst_output+=("• • — — — ")
        if tekst[i] == "3":
            tekst_output+=("• • • — — ")
        if tekst[i] == "4":
            tekst_output+=("• • • • — ")
        if tekst[i] == "5":
            tekst_output+=("• • • • • ")
        if tekst[i] == "6":
            tekst_output+=("— • • • • ")
        if tekst[i] == "7":
            tekst_output+=("— — • • • ")
        if tekst[i] == "8":
            tekst_output+=("— — — • • ")
        if tekst[i] == "9":
            tekst_output+=("— — — — • ")
        if tekst[i] == "0":
            tekst_output+=("— — — — — ")
        if tekst[i] == ".":
            tekst_output+=("• — • — • — ")
        if tekst[i] == ",":
            tekst_output+=("— — • • — — ")
        if tekst[i] == "'":
            tekst_output+=("• — — — — • ")
        if tekst[i] == '"':
            tekst_output+=("• — • • — • ")
        if tekst[i] == "_":
            tekst_output+=("• • — — • — ")
        if tekst[i] == ":":
            tekst_output+=("— — — • • • ")
        if tekst[i] == ";":
            tekst_output+=("— • — • — • ")
        if tekst[i] == "?":
            tekst_output+=("• • — — • •")
        if tekst[i] == "!":
            tekst_output+=("— • — • — —")
        if tekst[i] == "-":
            tekst_output+=("— • • • • —")
        if tekst[i] == "+":
            tekst_output+=("• — • — •")
        if tekst[i] == "/":
            tekst_output+=("— • • — •")
        if tekst[i] == "(":
            tekst_output+=("— • — — •")
        if tekst[i] == ")":
            tekst_output+=("— • — — • —")
        if tekst[i] == "=":
            tekst_output+=("— • • • —")
        if tekst[i] == "@":
            tekst_output+=("• — — • — •")
        if tekst[i] == "ą":
            tekst_output+=("• — • —")
        if tekst[i] == "ć":
            tekst_output+=("— • — • •")
        if tekst[i] == "ę":
            tekst_output+=("• • — • •")
        if tekst[i] == "é":
            tekst_output+=("• • — • •")
        if tekst[i] == "ł":
            tekst_output+=("• — • • —")
        if tekst[i] == "ń":
            tekst_output+=("— — • — —")
        if tekst[i] == "ó":
            tekst_output+=("— — — •")
        if tekst[i] == "ś":
            tekst_output+=("• • • — • • •")
        if tekst[i] == "ż":
            tekst_output+=("— — • • — •")
        if tekst[i] == "ź":
            tekst_output+=("— — • • —")
        if tekst[i] == " ":
            tekst_output+=("  ")
        tekst_output+=("  ")
    print(tekst_output)
    tts = tekst.encode('utf-8').decode('cp1250')
    os.system(f'espeak.lnk -v pl "{tts}"')

    f = open("slownik.txt", "a")
    f.write(f'{tekst} - {tekst_output}\n')
    f.close()
    czy_koniec = input("Wpisz tak, jezeli chcesz przetlumaczyc kolejne slowo, lub nie, jezeli chcesz skonczyc: ")
    if czy_koniec == "nie":
        stan = "koniec"
    elif czy_koniec == "tak":
        stan = "dziala"
    else:
        print("Niezrozumiale polecenie - restartowanie programu")
        stan = "dziala"
if stan == "koniec":
    print("Dziekuje za skorzystanie z programu! Wpisane i przetlumaczone slowa znajduja sie w pliku slownik.txt w folderze programu!")
