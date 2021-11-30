from module1 import *
palgad=[1200,2500,750,395,1535,1600,3100]
inimesed=["A","B","C","D","E","J","F"]

while True:
    print("Lisamine-1,3=suurim palk,Keskmine-6,Otsi inimest-7")
    valik = input("Millist valite->")
    if valik == "1":
        i,p = lisamine(inimesed,palgad)
    elif valik =="7":
        inimesed,palk=otsing_nimi_jargi(inimesed,palgad)
    elif valik =="3":
        i,p=suurim_palk(inimesed,palgad)
    elif valik =="6":
        i,p=keskmine(inimesed,palgad)


    
                



