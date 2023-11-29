#banners
from os import system
from time import sleep
    
def mesaj_banner(text):
    while True:
        b=""
        system("cls")
        if len(text)>10:
            print(text[0:9])
        else:
            print (text)

        for i in range (1, len(text)):
            b+=text[i]
        b+=text[0]
        text=b
        sleep(0.5)        

mesaj=input()
mesaj_banner (mesaj+"   ")