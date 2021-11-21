# MÃ³dulo que implementa uma Ã¡lgebra sobre polinÃ³mios
# 2021-11-21
# by Mónica Martins

import matplotlib.pyplot as plt

Pol=[]

def menu():
    print("""Bem vindo! Este programa tem várias funcionalidades. O que queres fazer?
    (1) - Criar polinómio
    (2) - Calcular polinómio
    (3) - Calcular tabela
    (4) - Simplificar polinómio
    (5) - Calcular derivada do polinómio
    (6) - Mostrar representação gráfica do polinómio
    (0) - Sair
     """)
    
def criarTermo(coef, exp):
    return(coef, exp)

def criarPolinomio():
    return []

def inserirTermo(p,t):
    return p.append(t)

def verTermo(t):
    c,e=t
    if e==0:
        return str(c)
    elif e==1:
        return str(c) +'x'
    else:
        return (str(c) +"x^"+ str(e))
    
def verPolinomio(p):
    res=""
    for t in p:
        if res=="":
            res=verTermo(t)
        else:
            res=res + "+" + verTermo(t)
    return res
    
def calcPol(p,x):
    resultado=0
    for (c,e) in (p):
        resultado= resultado +c*(x**e)
    return (resultado)

def tabela(p,nlinhas):
    for i in range(nlinhas):
        print(str(i)+ "::"+ str(calcPol(p,i)))
        
def chaveOrd(t):
    (c,e)=t
    return e

def ordenarPol(p):
    p.sort(reverse=True, key=chaveOrd)

def derivarPol(p):
    res=[]
    for (c,e) in p:
        if e==1:
            res.append((c*e,0))
        elif e<=0:
            res.append((c*e,e-1))

    return res

def simplificaPol(p):
    ordenarPol(p)
    poln=[]
    for i in range(1,len(p)):
        coef,exp=p[i]
        coef0,exp0=p[i-1]
        if exp0==exp:
            inserirTermo(poln,(coef+coef0,exp))     
        else:
            if exp0>exp:                                # se o expoente do elemento anterior for maior
                if i==1:                                # e o elemento que estamos a observar for o primeiro
                    inserirTermo(poln,(coef0,exp0))     # adicionamos o anterior porque o elemento na pos=0 é o unico com esse grau
            else:
                inserirTermo(poln,(coef,exp))           
    return verPolinomio(poln)


def mostraPol(myPol):
    x=[i for i in range(-100,100)]
    y=[]
    for n in x:
        y.append(calcPol(myPol,n))
        
    plt.plot(x,y)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()

op=1
while op!=0:
    print(" ")
    menu()
    op=int(input("Opção: "))
    print(" ")
    if op==1:
        Pol=criarPolinomio()
        n=int(input("Quantos termos tem o polinómio? "))
        for i in range(n):
            co=int(input('Coeficiente do termo '+str(i+1) +': '))
            ex=int(input('Expoente do termo '+str(i+1) +': '))
            inserirTermo(Pol,(co,ex))
        verPolinomio(Pol)
    elif len(Pol) == 0:
        print("Ainda não foi criado um polinómio!")
    else:
        if op==2:
            x=int(input("Qual é o valor de x? "))
            print("O valor do polinómio é"+ str(calcPol(Pol, x)))
        elif op==3:
            elem=int(input("Quantas linhas tem a tabela?"))
            print("x  Valor")
            for i in range(elem):
                print(str(i)+"  "+ str(calcPol(Pol,i)))
        elif op==4:
            print(simplificaPol(Pol))
        elif op==5:
            print(derivarPol(Pol))
        elif op==6:
            mostraPol(Pol)
            
            
                