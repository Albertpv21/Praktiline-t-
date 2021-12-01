from module1 import *
palgad=[1200,2500,750,395,1535,1600,3100]
inimesed=["A","B","C","D","E","J","F"]

while True:
    print("Lisamine-1,3=suurim palk,Keskmine-6,Otsi inimest-7,Remove-2")
    valik = input("Millist valite->")
    if valik == "1":
        vastus= lisamine(inimesed,palgad)
        print(vastus)
    elif valik =="7":
        vastus=otsing_nimi_jargi(inimesed,palgad)
        print(vastus)
    elif valik =="3":
        vastus=suurim_palk(inimesed,palgad)
        print(vastus)
    elif valik =="6":
        vastus=keskmine(inimesed,palgad)
        print(vastus)
    elif valik =="2":
        vastus=remove(inimesed,palgad)
        print(vastus)
        

    
                



