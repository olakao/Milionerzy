def wczytajPytania():
    # wczytuje pytania i odpowiedzi z pliku
    with open('Pytania_o_milion.txt', encoding='utf-8') as pyt:
        ques_answ = pyt.readlines()
        for i in range(0, len(ques_answ)-1): 
            ques_answ[i] = ques_answ[i][:-1]
    return ques_answ

def wczytajWygrane():
    # wczytuje kolejne wygrane z pliku
    with open('kolejne_wygrane.txt', encoding='utf-8') as wygrane:
        wygrane = wygrane.readlines()
        return wygrane

def dodajPytanie():
    # dodaje pytanie do pliku
    with open('Pytania_o_milion.txt', 'a', encoding='utf-8') as pyt:
        pytanie = "\n" + input("Podaj treść pytania: ") + "\n"
        a = "a) " + input("Podaj odpowiedź a): ") + "\n"
        b = "b) " + input("Podaj odpowiedź b): ") + "\n"
        c = "c) " + input("Podaj odpowiedź c): ") + "\n"
        d = "d) " + input("Podaj odpowiedź d): ") + "\n"
        prawidłowa = input("Podaj która odpowiedź jest poprawna a, b, c czy d: ") + ")"
        pyt.write(f"{pytanie}{a}{b}{c}{d}{prawidłowa}")
