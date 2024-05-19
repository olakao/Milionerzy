import sys
from koła_ratunkowe import *
from praca_na_plikach import *

bold = '\033[1m'; italics = '\033[3m'; underline = '\033[4m'
blue = '\033[94m'; red = '\033[91m'; green = '\033[92m'; end = '\033[0m'

def Milionerzy():
    # zabawa w Milionerów
    print(underline + blue + 'Witaj w zabawie ' + bold + 'Milionerzy' + end)
    print(italics + 'Jesteś gotów?' + end)
    
    ques_answ = wczytajPytania()    # lista pytań i odpowiedzi z pliku
    wygrane = wczytajWygrane()      # lista kolejnych wygranych z pliku

    randomPytanie = []
    for i in range (int(len(ques_answ)/6)): 
        randomPytanie.append(i)
    random.shuffle(randomPytanie)
    koła = ["50 na 50", "Pytanie do randomowej publiczności", "Pytanie do przyjaciela"]

    def askQues(nrPyt):
        pytanie = randomPytanie[nrPyt]*6
        print(bold + ques_answ[pytanie] + end)
        for i in range(pytanie + 1, pytanie + 5):
            print(ques_answ[i])
        
        if koła != []:
            koło = input("   Czy chcesz skorzystać z koła ratunkowego? T/N: ").upper()
            if koło == "T":
                print("   Oto dostępne koła:")
                for i in range(len(koła)):
                    print("     ", i+1, koła[i])
                try:
                    nrKoła = int(input("   Podaj numer koła które wybierasz: "))-1
                    if nrKoła <= len(koła)-1 and nrKoła >=0 :
                        if koła[nrKoła] == "50 na 50": 
                            półNa50(nrPyt, ques_answ, randomPytanie)
                            del koła[nrKoła]
                        elif koła[nrKoła] == "Pytanie do randomowej publiczności": 
                            publiczność()
                            del koła[nrKoła]
                        elif koła[nrKoła] == "Pytanie do przyjaciela": 
                            przyjaciel(nrPyt, ques_answ, randomPytanie)
                            del koła[nrKoła]
                    else: print("Przykro mi, nie ma takiego koła")
                except ValueError:
                    print("Przykro mi, nie ma takiego koła")

        odpowiedź = input("Podaj którą odpowiedź uznajesz za prawidłową, a, b, c czy d? ").lower()
        if odpowiedź == ques_answ[pytanie+5][:1]:
            print(green + "Super! Twoja wygrana to:" + end)
            print(wygrane[nrPyt])
        else:
            print(red + "Przykro mi, autor miał co innego na myśli!" + end)
            return False

    for i in range(12):
        poziom = askQues(i)
        if poziom == False:
            if i<3: sys.exit("Twoja wygrana to zero groszy")
            elif i<8: sys.exit("Twoja wygrana to π!")
            else: sys.exit("Twoja wygrana to nieskończenie wiele!")
        if i == 2: print('Gratulacje! Przekroczyłeś próg gwarantowany π\n')
        elif i == 7: print('Gratulacje! Osiągnąłeś próg gwarantowany nieskończenie wiele\n')
