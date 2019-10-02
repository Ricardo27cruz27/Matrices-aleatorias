# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 14:35:59 2019

@author: ricardo
"""

####
import numpy as np
import bs4 as bs
import pickle		#serializes any python object// here we serialize before saving s&p500 data
import requests
import datetime as dt 
import pandas_datareader.data as web
import os
import matplotlib.pyplot as plt
import seaborn as sns

#Utilizamos 2 funciones para descargar la información de 40 activos en 434 días comenzando en 2015

def save_sp500_ticker():
	resp = requests.get('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
	#soup is the object that comes from BeautifulObject
	soup = bs.BeautifulSoup(resp.text, 'lxml')
	#table == will find table data// should be specified
	table = soup.find('table',{'class':'wikitable sortable'})
	tickers = []
	#tr = table row, td = table data
	#for each table row
	for row in table.findAll('tr')[1:]:
		ticker = row.findAll('td')[0].text # we want the 0th column, we want the text from soupobject
		# get past BRK...
		mapping = str.maketrans(".","-") 
		ticker = ticker.translate(mapping)
		
		tickers.append(ticker)

	with open("sp500tickers.pickle","wb") as f:
		pickle.dump(tickers,f)

	print(tickers)

	return tickers

save_sp500_ticker()

def get_data_from_yahoo(reload_sp500=False):
	if reload_sp500:
		tickers = save_sp500_ticker()
	else:
		with open("sp500tickers.pickle","rb") as f:
			tickers = pickle.load(f)

	# Now we will save all SP500 data as csv files
	if not os.path.exists('stock_dfs'):	# if this directory doesn't exist
		os.makedirs('stock_dfs')

	start =dt.datetime(2015,1,1)
	end = dt.datetime(2016,9,20)

	#Solo tomamos los primeros 40 y tomamos el precio de cierre durante 434 días
	X=np.zeros((40,434))
	i=0
	for ticker in tickers[:40]:
		ticker2=ticker[:-1]
		df = web.DataReader(ticker2,'yahoo',start,end)
		X[i,]=df.Close
		i=i+1
	return X
		
#Tenemos la matriz de activos.
X=get_data_from_yahoo()
prev=X[:,:219]
M=np.zeros((40,218))
for i in range(40):
    compra=prev[i,0]
    for j in range(218):
        M[i,j]=np.log(X[i,j+1]/compra)

X_1=M[:,:109]
X_2=M[:,109:]
S1=np.corrcoef(X_1)
S_1=np.linalg.inv(S1)
#S2=np.dot(X_1,np.transpose(X_1))/217
val,vec= np.linalg.eig(S1)
val
sns.distplot(val, hist=False, kde=True, 
             bins=int(.5), color = 'darkblue', 
             hist_kws={'edgecolor':'black'},
             kde_kws={'linewidth': 4})


max(val)
Q=109/40
def l_max(sigma=1):
    resultado=sigma*(1+(1/Q)+(2/np.sqrt(Q)))
    return resultado

sum(val>l_max())/40
val[0:5]
sum(val>l_max(.75))/40

traza=sum(val)
constante=(traza-sum(val[0:5]))/(40-5)
val2=val
val2[5:40]=constante
S_2=np.dot(np.dot(vec,np.diag(val2)),np.transpose(vec))

p=40
n=109
mu1=np.mean(X_1,axis=1)
mu2=np.mean(X_2,axis=1)
#creamos la función para generar el riesgo
def Riesgos2(G,mu1,mu2,S_1,S_2):
    R_in=(G**2)/(np.dot(np.dot(np.transpose(mu1),S_1),mu1))
    R_out=(G**2)*(np.dot(np.dot(np.dot(np.transpose(mu1),S_2),S_2),mu1)/((np.dot(np.dot(np.transpose(mu1),S_2),mu1))**2))
    R_in_c=(G**2)/(np.dot(np.dot(np.transpose(mu2),S_1),mu2))
    R_out_c=(G**2)*(np.dot(np.dot(np.dot(np.transpose(mu2),S_2),S_2),mu2)/((np.dot(np.dot(np.transpose(mu2),S_2),mu2))**2))
    return R_in, R_out, R_in_c, R_out_c

#Ejecutamos la función
R_I=[0] * 100
R_O=[0] * 100
R_I_C=[0] * 100
R_O_C=[0] * 100
for i in range(1,101):
    RISK=Riesgos2(i,mu1,mu2,S_1,S_2)
    R_I[i-1]=RISK[0]
    R_O[i-1]=RISK[1]
    R_I_C[i-1]=RISK[2]
    R_O_C[i-1]=RISK[3]
    

fig1, ax=plt.subplots()
ax.plot(R_I,range(1,101),label="IN")
ax.plot(R_O,range(1,101),label="OUT")
ax.plot(R_I_C,range(1,101),label="IN_clean")
ax.plot(R_O_C,range(1,101),label="OUT_clean")
leg=ax.legend()

#Código auxiliar.
#i=1
#for ticker in tickers[:40]:
#    ticker2=ticker[:-1]
#    df = web.DataReader(ticker2,'yahoo',start,end)
#    print(df.shape)
#    print(i)
#    i=i+1
#
