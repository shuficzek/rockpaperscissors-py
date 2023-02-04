import random #Importuje losowanie.
import time #Importuje czas.
zabawa = ["Papier", "Kamień", "Nożyce"] #Słowa które będą losowane.
print ("Gra papier kamień nożyce.") #Pokazanie tytułu gry.
for i in range(25): #Ile razy wykona się tę komendy.
    losowanie = random.choice(zabawa) #Losowanie słów z zmiennej zabawa.
    time.sleep(3) #Odczekiwanie co ile się pokaże wylosowane słowo.
    print(losowanie) #Pokazanie wylosowanego słowa.
