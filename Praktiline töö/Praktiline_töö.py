from module1 import *
palk=[1200,2500,750,395,1535,1600,3100]
inimesed=["A","B","C","D","E","J","F"]

while True:
  print("0-lõpetamine, 1-lisane andmed, 2-sorteerimine,3-Otsi nimest,4-TOP,5-Maksimaalne palk")
  a = int(input())
  if a == 0:
      break
  elif a == 1:
      inimesed, palk = lisamine(palk,inimesed)
      print(palk,inimesed)
  elif a == 2:
      p,i=sorteerimine(palk,inimesed)
      for i in range(len(inimesed)):
          print(inimesed[i]," Tema palk   ", palk[i])
  elif a == 3:
        ots_nimi,ots_palk=nimi(palk,inimesed)
        for i in range(len(ots_nimi)):
            print(ots_nimi[i]," Tema palk   ", ots_palk[i])
  elif a == 4:
      p, i=topbogat(palk, inimesed)
  elif a == 5:
        max_palk,kellel=maksimum(palk,inimesed)
        print("Maksimaalne palk ", max_palk, " saab  ",kellel)

    
                



