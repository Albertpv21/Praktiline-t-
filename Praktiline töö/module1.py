def lisamine(palk,inimesed):
    add=input("Keda lisame?")
    inimesed.append(add)
    add_zp=int(input("Milline palk?"))
    palk.append(add_zp)
    return palk,inimesed     
def sorteerimine(palk,inimesed): 
    abi_p=0
    abi_i=""
    n=len(inimesed)
    for i in range(0,n-1):
        for j in range(i+1,n):
            if palk[i]>palk[j]:
                abi_p=palk[i]
                palk[i]=palk[j]
                palk[j]=abi_p
                abi_i=inimesed[i]
                inimesed[i]=inimesed[j]
                inimesed[j]=abi_i
    return palk,inimesed
def nimi(palk,inimesed):
    ots_nimi=[]
    ots_palk=[]
    palk_keda=0
    keda=input("Sisesta nimi... ")
    n=len(inimesed)
    for j in range(n):
        if inimesed[j]==keda:
            palk_keda=palk[j]
            ots_nimi.append(inimesed[j])
            ots_palk.append(palk_keda)
        else:pass
    return ots_nimi,ots_palk
def topbogat(palk,inimesed):
    top,inimes=sorteerimine(palk,inimesed)
    k= int(input("Vali mitu inimest tahad näha toppis: " ))
    palk.reverse()
    inimesed.reverse()
    for i in range(0,k,1):
        print(palk[i])
        print(inimesed[i])
    return palk, inimesed

def maksimum(palk,inimesed):
    m_palgad=[]
    nimed=[]
    max_palk=palk[0]
    kellel=inimesed[0]
    for p in palk:
        if p>max_palk:
            max_palk=p
            i=palk.index(max_palk)
            kellel=inimesed[i]
    n=palk.count(max_palk)
    palk_copy=palk.copy()
    inimesed_copy=inimesed.copy()
    for i in range(n):
        j=palk_copy.index(max_palk)
        m_palgad.append(palk_copy.pop(j))
        nimed.append(inimesed_copy.pop(j))
    return m_palgad, nimed





