def lisamine(i,p): 
    """
    i-inimeste nimikiri,p-palka nimikiri 
    """
    kogus = int(input("Lisa inimest: "))
    for j in range(kogus):
        nimi = input("Nimi: ")
        i.append(nimi)
        palgad = int(input("Palk: "))
        p.append(palgad)
        return i,p
def otsing_nimi_jargi(inimesed:list,palgad:list):
    """Tagastame jäejend või tekst
    :rtype var: tulemus
    """
    nimi=input("Keda otsime?")
    for inimene in inimesed:
        if inimene==nimi:
            n=inimesed.count(nimi)
            print("Inimene on olemas,selline kohtume",n,"korda")
            b=-1
            for i in range(n):
                k=inimesed.index(nimi,b)
                palk=palgad[k]
                print(nimi,palk)
        else:
             t="Ei ole nimekirjas"
    return t
def suurim_palk(i,p):
    suurim=max(p)
    b=p.index(suurim)
    kellel=i[b]
    return suurim,kellel
def keskmine(i,p):
    """Keskmise palka leidmine.Kui ta on loetelus,siis näime kes saad seda kätte
    :rtype var:
    """
    summa=0
    for palk in p:
        summa+=palk
    kesk=summa/len(p)
    print(kesk)
    vahe=0
    if 0<=p.index(kesk)<len(p)-1:
        kesk=i[p.index(kesk)]
        return kesk
    else:
        kesk="Puudub"
        return kesk
def remove(inimesed:list,palgad:list):
    """
    """
    a=input("Keda otsime?")
    if a not in inimesed:
        print("Selle nime ei ole olemas")
    else:
        b=inimesed.index(a)
        inimesed.remove(a)
        palgad.pop(b)






