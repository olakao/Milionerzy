from Milionerzy import *

print(bold + "Witaj w naszym wspaniałym świecie Milionerów!" + end)
print("1. Chcę zagrać w " +blue+bold+ "Milionerów" + end + "! \
      \n2. Chcę dodać pytanie do pliku. \
      \n3. Chcę wyjść z programu :(")

try:
    opcja = int(input("Którą opcję wybierasz? "))
    if opcja <= 3 and opcja > 0:
        if opcja == 1:
            Milionerzy()
        elif opcja == 2:
            dodajPytanie()
        elif opcja == 3:
            sys.exit("Wybrałeś opcję wyjścia z programu")
    else: print("Przykro mi, nie ma takiej opcji")

except ValueError:
    print("Przykro mi, nie ma takiej opcji")
