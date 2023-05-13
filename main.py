from os import system
from random import randint,choice
from threading import Thread
from keyboard import is_pressed

system("cls")
def kierunek():
    #test
    wartosc=0
    global direction
    print("Podaj kierunek...")
    while wartosc==0:
        if is_pressed("w")==True:
            direction="up"
            wartosc+=1
        elif is_pressed("a")==True:
            direction="left"
            wartosc+=1
        elif is_pressed("s")==True:
            direction="down"
            wartosc+=1
        elif is_pressed("d")==True:
            direction="right"
            wartosc+=1


def output(lista):
    for x in range(0,len(lista)):
        for j in range (0,len(lista[x])):
            print(lista[x][j],end=" ")

        print()

def losowanie(tablica):
    #losowanie koordynatow 2 blokow dwojkowych
    for z in range(0,2):
        x=randint(0,3)
        y=randint(0,3)
        while tablica[x][y]!=0:
            x=randint(0,3)
            y=randint(0,3)
        tablica[x][y]=2

def max(lista):
    max=0
    for x  in range(0,len(lista)):
        for j in range(0,len(lista[x])):
            if int(lista[x][j])>=max:
                max=int(lista[x][j])
            else:
                max=max
    
    return max    

def check(lista):
    sum=0
    for x in range(0,len(lista)):
        for j in range(0,len(lista[x])):
            if lista[x][j]==0:
                sum+=1
    if sum == 0:
        return True
    else:
        return False

def losowanie_2(lista):
    liczby=[2,4]
    x=randint(0,3)
    y=randint(0,3)
    while lista[x][y]!=0:
        x=randint(0,3)
        y=randint(0,3)
    liczba=choice(liczby)
    lista[x][y]=liczba

def move(lista,direction):
    ilosc=0
    wynik=0
    while wynik==0:

        if direction=="up":
            pass
        ###w trakcie pracy
        
#stworzenie tablicy

direction = " "
tablica=[]
for x in range (0,4):
    tablica.append([])
    for j in range(0,4):
        tablica[x].append(0)

losowanie(tablica)

while True:
    system("cls")
    output(tablica)
    #kierunek()
    direction = input("Kierunek:")
    move(tablica,direction)
    print("JEST")
    system("pause>nul")
    if max(tablica)==2048:
        system("cls")
        print("Wygrales!")
        exit()
    else:
        pass
    if check(tablica)==True:
        system("cls")
        print("Przegrales!")
        exit()
    else:
        pass
    losowanie_2(tablica)
    

    