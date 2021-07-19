# -*- coding: utf-8 -*-
"""
Created on Fri Jul 16 19:56:05 2021

@author: DAN-HDT
"""
import numpy as np
import matplotlib.pyplot as plt
def bcplot(bc,corx,cory):
    for i in range(len(bc)):
        m=np.mod(bc[i],2)
        if(m!=0):
            x=corx[int((bc[i]-1)/2)]
            y=cory[int((bc[i]-1)/2)]
            plt.plot(x-0.05,y,'>',c='g',markersize=10);
        elif (m==0):    
            x=corx[int((bc[i]-2)/2)]
            y=cory[int((bc[i]-2)/2)]
            plt.plot(x,y-0.05,'^',c='g',markersize=10);
def fcplot(Ftt):
    print('Plot Force')
def mtbool(mtnode,dof):
    mtbool_elem=[]
    node_elem=len(mtnode)
    for i in range(node_elem):
        s = (mtnode[i] - 1)*dof;
        for j in range(dof):
            mtbool_elem.append(s+j+1)
    mtboole=np.array([mtbool_elem])
    return(mtboole)           
def mt_ke(E,A,L,S,C):
    Ae = ((E*A)/L)
    Ke =Ae*np.array([[C**2, C*S, -C**2, -C*S],
                  [C*S, S**2, -C*S, -S**2],
                  [-C**2, -C*S, C**2, C*S],
                  [-C*S, -S**2, C*S, S**2]])
    return(Ke)
def mt_kg(Kg,Ke,mt_boole):
    for i in range(4):
        #print(mt_boole[0,i]-1)
        indexi=mt_boole[0,i]-1
        for j in range(4):
            indexj=mt_boole[0,j]-1
            Kg[indexi,indexj]=Kg[indexi,indexj]+Ke[i,j]
    return Kg
def bcpatch(Kg_bd,Fg_bd,BC):
    n = len(BC)
    gdof = len(Kg_bd)
    for i in range(n):
        c = BC[i]-1;
        for j in range(gdof):
            Kg_bd[c,j]=0#khu hang
            Kg_bd[j,c]=0#khu cot
        Kg_bd[c,c] = 1;
        Fg_bd[c] = 0;
    invKg=np.linalg.inv(Kg_bd)
    #print('inverseKg: ',invKg)
    Ug=np.matmul(invKg,Fg_bd)
    return(Ug)
    