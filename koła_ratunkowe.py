import random

def półNa50(nrPyt, ques_answ, randomPytanie):
    # koło ratunkowe 50 na 50
    rand = []
    pytanie = randomPytanie[nrPyt]*6
    for i in range(1,5):
        if ques_answ[pytanie+i][:1] != ques_answ[pytanie+5][:1]:
            rand.append(ques_answ[pytanie+i][:1])
    random.shuffle(rand)
    for i in range(1,5):
        if ques_answ[pytanie+i][:1] == ques_answ[5+randomPytanie[nrPyt]*6][:1] or \
            ques_answ[pytanie+i][:1] == rand[0]:
            print(ques_answ[pytanie+i])

def publiczność():
    # koło ratunkowe Pytanie do randomowej publiczności
    a = random.randint(1,100)
    b = random.randint(1,100-a)
    c = random.randint(1,100-a-b)
    print("Twoja randomowa publiczność odpowiada:")
    print("a)", a,"%, b)", b, "%, c)", c, "%, d)", 100-a-b-c, "%")

def przyjaciel(nrPyt, ques_answ, randomPytanie):
    # koło ratunkowe Pytanie do przyjaciela, 3 stopnie zaawansowania przyjaciela
    lista = ["a","b","c","d"]
    prawidłowa = ques_answ[5+randomPytanie[nrPyt]*6][:1]
    lista.append(prawidłowa)
    typPrzyjaciela = random.randint(1,3)
    if typPrzyjaciela == 1:
        print("Twojemu miłemu przyjacielowi wydaje się że odpowiedź to:", end=" ")
    if typPrzyjaciela == 2:
        print("Twój inteligentny przyjaciel wykonbinował, że odpowiedź to:", end=" ")
    if typPrzyjaciela == 3:
        print("Twój obeznany w temacie przyjaciel twierdzi, że odpowiedź to:", end=" ")
    if typPrzyjaciela == 2:
        lista.extend(prawidłowa * 10)
    if typPrzyjaciela == 3:
        lista.extend(prawidłowa * 20)
    random.shuffle(lista)
    print(lista[1])
