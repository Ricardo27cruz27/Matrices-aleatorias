#a)
B=matrix(c(.074,.537,.332,.208,
           .537,4.2,2.355,1.637,
           .332,2.355,6.114,3.781,
           .208,1.637,3.781,2.493),
         4)

W=matrix(c(.32,1.697,.554,.217,
             1.697,12.143,4.364,2.11,
             .554,4.364,4.291,2.482,
             .217,2.11,2.482,1.723),
           4)


l_1<-eigen(solve(W)%*%B)$values[1]
theta<-l_1/(1+l_1)

f.95 = 0.9793 
p=4
m=42
n=5

phi=2*asin(sqrt((max(p,n)-.5)/(m+n-1)))
gamma=2*asin(sqrt((min(p,n)-.5)/(m+n-1)))
mu=2*log(tan((phi+gamma)/2))
sigma=((16/((m+n-1)^2))*(1/((sin(phi+gamma)^2)*sin(phi)*sin(gamma))))^(1/3)
theta_TW=(exp(mu+(f.95*sigma)))/(1+exp(mu+(f.95*sigma)))

relativo<-(theta_TW/theta)-1
relativo
l_1_hat<-theta_TW/(1-theta_TW)


#b)
library(MASS)
set.seed(27)
p<-100
n<-200
k=10
mu<-rep(0,p)
Sigma<-matrix(0,p,p)
diag(Sigma)<-runif(p,0,1)
muestra<-function(){
  Y<-matrix(0,n,p)
  for (i in 1:n){
    Y[i,]<-mvrnorm(1,mu,Sigma)
  }
  return(Y)
}

MUESTRAS<-list()
for(i in 1:k){
 MUESTRAS[[i]]<-muestra() 
}



library(heplots)
boxM(MUESTRAS)
