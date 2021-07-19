# -*- coding: utf-8 -*-
"""
Created on Fri Jul 16 19:54:00 2021

@author: DAN-HDT
"""
import numpy as np
import matplotlib.pyplot as plt
E = 1e11
A = 0.01
dof= 2
corX=[]
corY=[]
corX.append(0)
corY.append(0)
corX.append(1)
corY.append(0)
corX.append(2)
corY.append(0)
corX.append(1)
corY.append(-1)
for i in range(len(corX)):
    plt.scatter(corX[i],corY[i])
    plt.annotate("N"+str(i+1), (corX[i],corY[i]))
elemI=[]
elemJ=[]
elemI.append(1)
elemJ.append(4)
elemI.append(2)
elemJ.append(4)
elemI.append(3)
elemJ.append(4)
for i in range(len(elemI)):
    nodeI=elemI[i]
    nodeJ=elemJ[i]
    xI=corX[nodeI-1]
    yI=corY[nodeI-1]
    xJ=corX[nodeJ-1]
    yJ=corY[nodeJ-1]
    plt.plot([xI,xJ],[yI,yJ],'-',linewidth=4)
    plt.annotate("E"+str(i+1), ((xI+xJ)/2,(yI+yJ)/2))
node_num=len(corX)
elem_num=len(elemI)
Kg=np.zeros((node_num*dof,node_num*dof))
Fg=np.zeros((node_num*dof,1))

#BoudaryCondition
import fplot as fp
BC=[1,2,3,4,5,6]
fp.bcplot(BC,corX,corY)
Fg[6]=1000
Fg[7]=-1000
print(Fg)
#Solve
L=[]
C=[]
S=[]
for i in range(len(elemI)):
    nodeI=elemI[i]
    nodeJ=elemJ[i]
    xi=corX[nodeI-1]
    yi=corY[nodeI-1]
    xj=corX[nodeJ-1]
    yj=corY[nodeJ-1]
    L.append(np.sqrt((xj-xi)**2 + (yj-yi)**2))
    C.append((xj-xi)/L[i])
    S.append((yj-yi)/L[i])
    print('Element'+str(i+1)+':','C=',C[i],',S=',S[i],',L=',L[i])
    mtnode=[nodeI, nodeJ]
    print(fp.mtbool(mtnode, dof))
    mt_boole=fp.mtbool(mtnode, dof)
    Ke=fp.mt_ke(E, A, L[i], S[i], C[i])
    print(Ke)
    Kg=fp.mt_kg(Kg,Ke,mt_boole)
    print(Kg)
 #Luu lai ma tran do cung tong the ban dau
 #Luu lai ma tran luc tong the ban dau
print('Patch Kg:',Kg)
Ku=np.array(Kg)
Ug=fp.bcpatch(Ku,Fg,BC) #khu dieu kien bien
print('Patch Kg:',Ku)
#print('inverseKg: ',invKg)
print('Displacement: ',Ug)
N=np.matmul(Kg,Ug) 
print(N)