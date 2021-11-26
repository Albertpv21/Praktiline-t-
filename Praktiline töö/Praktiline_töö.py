from module1 import *
palgad=[1200,2500,750,395,1200,1600,3100]
inimesed=["A","B","C","D","E","D","F"]

while True:
    print("Lisamine-1,Otsi inimest-7")
    valik = input("Millist valite->")
    if valik == "1":
        i,p = lisamine(inimesed,palk)
    elif valik =="7":
        inimesed,palk=otsing_nimi_jargi(inimesed,palgad)


    
                



