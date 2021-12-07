import matplotlib.pyplot as plt

def getEMD(linha):
    emd=[]
    novaLinha=linha.replace("\n","")
    campos=novaLinha.split(",")
    emd.append("emd"+str(int(campos[1])+1))
    for i in range(2,len(campos)):
        emd.append(campos[i])
       
    return emd


def lerDataset(fnome):
    f = open(fnome, encoding="utf-8")
    bd=[]
    f.readline()
    for linha in f:
        emd=getEMD(linha)
        bd.append(emd)

    return bd


def chaveOrd(l):
    data=l[1]
    data=data.split("-")
    return data
    

def listarDataset(bd):
    bd.sort(key=chaveOrd,reverse=True)
    print(" id    |    data    |       nome       |        apto     ")
    for exame in bd:
        print(exame[0] +"    " + exame[1] +"    "  + exame[2]+" " + exame[3] +"         " + exame[11])
        

def consultarDataset(bd, id):
    i=0
    while bd[i][0] != id:
        i=i+1
    return bd[i]


def modalidades(bd):
    modalidades=[]
    for exame in bd:
        if exame[7] not in modalidades:
            modalidades.append(exame[7])
    modalidades.sort()
    return modalidades


def distribPorModalidade(bd):
    modalidade={}
    for exame in bd:
        if exame[7] in modalidade.keys():
            modalidade[exame[7]]= modalidade[exame[7]] + 1
        else:
            modalidade[exame[7]]=1
    return modalidade


def distribPorClube(bd):
    clube={}
    for exame in bd:
        if exame[8] in clube.keys():
            clube[exame[8]]= clube[exame[8]] + 1
        else:
            clube[exame[8]]=1
    return clube


def distribPorAno(bd):
    ano={}
    for exame in bd:
        data=exame[1].split("-")
        if data[0] in ano.keys():
            ano[data[0]]= ano[data[0]] + 1
        else:
            ano[data[0]]=1
    return ano


def distrib(bd, i):
    dist={}
    for exame in bd:
        if exame[i] in dist.keys():
            dist[exame[i]]= dist[exame[i]] + 1
        else:
            dist[exame[i]]=1
    
    return dist


def plotDistribPorAno(bd):
    dic=distribPorAno(bd)
    x=dic.keys()
    y=[]
    for i in dic.keys():
        y.append(dic[i])
        
    fig = plt.figure(figsize=(15, 5))
    plt.bar(x, y, align='edge', width=0.3)
    plt.show()
 

def plotDistribPorModalidade(bd):
    dic=distribPorModalidade(bd)
    x=dic.keys()
    y=[]
    for i in dic.keys():
        y.append(dic[i])
        
    fig= plt.figure(figsize=(15, 5))
    plt.bar(x, y, align='edge', width=0.3)
    plt.show()
    

def plotDistrib(bd, i):
    dic=distrib(bd, i)
    x=dic.keys()
    y=[]
    for i in dic.keys():
        y.append(dic[i])
        
    fig= plt.figure(figsize=(15, 5))
    plt.bar(x, y, align='edge', width=0.3)
    plt.show()


