from random import randint
import time

tesadufi = randint(1, 40)

sans = 6

print("Oyuncu, 1-40 arası bir ədəd təxmin et. 6 səhv etmə şansın var.")

while sans > 0:
    daxil = int(input("Ədədi daxil edin: "))
    time.sleep(1.5)
    if daxil < tesadufi:
        sans -= 1
        print("Yanlış, tapılacaq ədəd daha böyükdür")
        if sans > 0:
            print(f"Oyunçu {sans} şansın qaldı")
        else:
            print(f"Yanlış, cavab: {tesadufi} idi,\n Oyun bitdi zəif :) ")
    elif daxil > tesadufi:
        sans -= 1
        print("Yanlış, tapılacaq ədəd daha kiçikdir")
        if sans > 0:
            print(f"{sans} şansınız qaldı")
        else:
            print(f"Yanlış, cavab: {tesadufi} idi,\nOyun bitdi ZƏİF :) ")
    else:
        print(f"Təbriklər oyuncu {tesadufi} cavabı dogrudur\nSən ƏJDAHASAN :)")
        break

    
