def zamiana_iter(liczba,system):
    liczby = []
    if system == 16:
        while liczba!=0:
            if liczba < 10:
                liczby.append(liczba)
            else:
                liczby.append(liczba%system)
            liczba=liczba//system
        liczby=liczby[::-1]
        for i in range(len(liczby)):
            if liczby[i] == 10:
                liczby[i] = "A"
            elif liczby[i] == 11:
                liczby[i] = ("B")
            elif liczby[i] == 12:
               liczby[i] = ("C")
            elif liczby[i] == 13:
                liczby[i]= ("D")
            elif liczby[i] == 14:
                liczby[i] = ("E")
            elif liczby[i] == 15:
                liczby[i] = ("F")
    else:
        while liczba!=0:
            liczby.append(liczba%system)
            liczba=liczba//system
        liczby=liczby[::-1]
    return liczby

print "Zamiana iteracyjnie:", zamiana_iter(1500190,2)


def zamiana(liczba,system):
    if system != 16:
        wynik = liczba%system
        if liczba<=1:
            return str(liczba)
        else:
            return str(zamiana(liczba//system,system)) + str(wynik)
    else:
        wynik = liczba%system
        if liczba < 10:
            return liczba
        elif liczba == 10:
            wynik = "A"
            return "A"
        elif liczba == 11:
            wynik = "B"
            return "B"
        elif liczba == 12:
            wynik = "C"
            return "C"
        elif liczba == 13:
            wynik = "D"
            return "D"
        elif liczba == 14:
            wynik = "E"
            return "E"
        elif liczba == 15:
            wynik = "F"
            return "F"
        else:
            return str(zamiana(liczba//system,system)) + str(wynik)
        

print zamiana(15,16)
    

