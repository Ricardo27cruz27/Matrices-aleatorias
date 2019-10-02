# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 21:12:28 2019

@author: ricardo
"""

### EJERCICIO 1 ###
import numpy as np
import matplotlib.pyplot as plt
#generamos la matriz
p=100
n=200
Z=np.random.normal(0,1,(p,n))
mu=np.repeat(1,p)
SIGMA=np.diag(np.repeat(1,p))
sigma=.2
D=np.diag(np.repeat(sigma,p))
X=np.dot(D,Z)
S=np.corrcoef(X)
S_1=np.linalg.inv(S)
#creamos la función para generar el riesgo
def Riesgos(G,mu,S_1,SIGMA):
    R_t=(G**2)/(np.dot(np.dot(np.transpose(mu),np.linalg.inv(SIGMA)),mu))
    R_in=(G**2)/(np.dot(np.dot(np.transpose(mu),S_1),mu))
    R_out=(G**2)*(np.dot(np.dot(np.dot(np.transpose(mu),S_1),S_1),mu)/((np.dot(np.dot(np.transpose(mu),S_1),mu))**2))
    return R_t, R_in, R_out

#Ejecutamos la función
R_T1= [0] * 100
R_I1=[0] * 100
R_O1=[0] * 100
for i in range(1,101):
    RISK=Riesgos(i,mu,S_1,SIGMA)
    R_T1[i-1]=RISK[0]
    R_I1[i-1]=RISK[1]
    R_O1[i-1]=RISK[2]
    


### modificacion a p
p=50
n=200
Z=np.random.normal(0,1,(p,n))
mu=np.repeat(1,p)
SIGMA=np.diag(np.repeat(1,p))
sigma=.2
D=np.diag(np.repeat(sigma,p))
X=np.dot(D,Z)
S=np.corrcoef(X)
S_1=np.linalg.inv(S)

def Riesgos(G,mu,S_1,SIGMA):
    #n=200
    #w=G*(np.dot(S_1,mu)/(np.dot(np.dot(np.transpose(mu),S_1),mu)))
    R_t=(G**2)/(np.dot(np.dot(np.transpose(mu),np.linalg.inv(SIGMA)),mu))
    R_in=(G**2)/(np.dot(np.dot(np.transpose(mu),S_1),mu))
    R_out=(G**2)*(np.dot(np.dot(np.dot(np.transpose(mu),S_1),S_1),mu)/((np.dot(np.dot(np.transpose(mu),S_1),mu))**2))
    return R_t, R_in, R_out

R_T2= [0] * 100
R_I2=[0] * 100
R_O2=[0] * 100
for i in range(1,101):
    RISK=Riesgos(i,mu,S_1,SIGMA)
    R_T2[i-1]=RISK[0]
    R_I2[i-1]=RISK[1]
    R_O2[i-1]=RISK[2]
    



### modificacion a n
p=100
n=150
Z=np.random.normal(0,1,(p,n))
mu=np.repeat(1,p)
SIGMA=np.diag(np.repeat(1,p))
sigma=.2
D=np.diag(np.repeat(sigma,p))
X=np.dot(D,Z)
S=np.corrcoef(X)
S_1=np.linalg.inv(S)

def Riesgos(G,mu,S_1,SIGMA):
    #n=200
    #w=G*(np.dot(S_1,mu)/(np.dot(np.dot(np.transpose(mu),S_1),mu)))
    R_t=(G**2)/(np.dot(np.dot(np.transpose(mu),np.linalg.inv(SIGMA)),mu))
    R_in=(G**2)/(np.dot(np.dot(np.transpose(mu),S_1),mu))
    R_out=(G**2)*(np.dot(np.dot(np.dot(np.transpose(mu),S_1),S_1),mu)/((np.dot(np.dot(np.transpose(mu),S_1),mu))**2))
    return R_t, R_in, R_out

R_T3= [0] * 100
R_I3=[0] * 100
R_O3=[0] * 100
for i in range(1,101):
    RISK=Riesgos(i,mu,S_1,SIGMA)
    R_T3[i-1]=RISK[0]
    R_I3[i-1]=RISK[1]
    R_O3[i-1]=RISK[2]
    

### modificacion a sigma
p=100
n=200
Z=np.random.normal(0,1,(p,n))
mu=np.repeat(1,p)
SIGMA=np.diag(np.repeat(1,p))
sigma=.55
D=np.diag(np.repeat(sigma,p))
X=np.dot(D,Z)
S=np.corrcoef(X)
S_1=np.linalg.inv(S)

def Riesgos(G,mu,S_1,SIGMA):
    #n=200
    #w=G*(np.dot(S_1,mu)/(np.dot(np.dot(np.transpose(mu),S_1),mu)))
    R_t=(G**2)/(np.dot(np.dot(np.transpose(mu),np.linalg.inv(SIGMA)),mu))
    R_in=(G**2)/(np.dot(np.dot(np.transpose(mu),S_1),mu))
    R_out=(G**2)*(np.dot(np.dot(np.dot(np.transpose(mu),S_1),S_1),mu)/((np.dot(np.dot(np.transpose(mu),S_1),mu))**2))
    return R_t, R_in, R_out

R_T4= [0] * 100
R_I4=[0] * 100
R_O4=[0] * 100
for i in range(1,101):
    RISK=Riesgos(i,mu,S_1,SIGMA)
    R_T4[i-1]=RISK[0]
    R_I4[i-1]=RISK[1]
    R_O4[i-1]=RISK[2]
    



### modificacion a mu
p=100
n=200
Z=np.random.normal(0,1,(p,n))
mu=np.repeat(.75,p)
SIGMA=np.diag(np.repeat(1,p))
sigma=.2
D=np.diag(np.repeat(sigma,p))
X=np.dot(D,Z)
S=np.corrcoef(X)
S_1=np.linalg.inv(S)

def Riesgos(G,mu,S_1,SIGMA):
    #n=200
    #w=G*(np.dot(S_1,mu)/(np.dot(np.dot(np.transpose(mu),S_1),mu)))
    R_t=(G**2)/(np.dot(np.dot(np.transpose(mu),np.linalg.inv(SIGMA)),mu))
    R_in=(G**2)/(np.dot(np.dot(np.transpose(mu),S_1),mu))
    R_out=(G**2)*(np.dot(np.dot(np.dot(np.transpose(mu),S_1),S_1),mu)/((np.dot(np.dot(np.transpose(mu),S_1),mu))**2))
    return R_t, R_in, R_out

R_T5= [0] * 100
R_I5=[0] * 100
R_O5=[0] * 100
for i in range(1,101):
    RISK=Riesgos(i,mu,S_1,SIGMA)
    R_T5[i-1]=RISK[0]
    R_I5[i-1]=RISK[1]
    R_O5[i-1]=RISK[2]
    
    
    
fig1, ax=plt.subplots()
ax.plot(R_T1,range(1,101),label="TRUE")
ax.plot(R_I1,range(1,101),label="IN")
ax.plot(R_O1,range(1,101),label="OUT")
leg=ax.legend()
fig1.suptitle('p=100, n=200, sigma=.2, mu=1')
#fig
    

fig, axs = plt.subplots(2,2)
axs[0, 0].plot(R_T2, range(1,101),label="TRUE")
axs[0, 0].plot(R_I2,range(1,101),label="IN")
axs[0, 0].plot(R_O2,range(1,101),label="OUT")
axs[0, 0].set_title('p=50')
axs[0, 1].plot(R_T3, range(1,101),label="TRUE")
axs[0, 1].plot(R_I3,range(1,101),label="IN")
axs[0, 1].plot(R_O3,range(1,101),label="OUT")
axs[0, 1].set_title('n=150')
axs[1, 0].plot(R_T4, range(1,101),label="TRUE")
axs[1, 0].plot(R_I4,range(1,101),label="IN")
axs[1, 0].plot(R_O4,range(1,101),label="OUT")
axs[1, 0].set_title('sigma=.55')
axs[1, 1].plot(R_T5, range(1,101),label="TRUE")
axs[1, 1].plot(R_I5,range(1,101),label="IN")
axs[1, 1].plot(R_O5,range(1,101),label="OUT")
axs[1, 1].set_title('mu=.75')


fig1
fig

#
#fig2, ax=plt.subplots()
#ax.plot(R_T,range(1,101),label="TRUE")
#ax.plot(R_I,range(1,101),label="IN")
#ax.plot(R_O,range(1,101),label="OUT")
#leg=ax.legend()
#fig2.suptitle('p=50, n=200, sigma=.2, mu=1')
##fig
#
#fig3, ax=plt.subplots()
#ax.plot(R_T,range(1,101),label="TRUE")
#ax.plot(R_I,range(1,101),label="IN")
#ax.plot(R_O,range(1,101),label="OUT")
#leg=ax.legend()
#fig3.suptitle('p=100, n=150, sigma=.2, mu=1')
##fig
#
#
#fig4, ax=plt.subplots()
#ax.plot(R_T,range(1,101),label="TRUE")
#ax.plot(R_I,range(1,101),label="IN")
#ax.plot(R_O,range(1,101),label="OUT")
#leg=ax.legend()
#fig4.suptitle('p=100, n=200, sigma=.55, mu=1')
##fig
#    
#fig5, ax=plt.subplots()
#ax.plot(R_T,range(1,101),label="TRUE")
#ax.plot(R_I,range(1,101),label="IN")
#ax.plot(R_O,range(1,101),label="OUT")
#leg=axs.legend()
#fig5.suptitle('p=100, n=200, sigma=.2, mu=.75')
##fig
#
#
