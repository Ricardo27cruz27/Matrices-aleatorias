### EJERCICIO 1 ###
library(matrixcalc)
n=10
H<-matrix(rnorm(n*n,0,0.2),n,n)
H2<-(H+t(H))/2
vp<-eigen(H2)
vp
J<-matrix(0,n*(n+1)/2,n*(n+1)/2)
epsilon<-1e-7
index<-1
for(i in 1:n){
  for(j in i:n){
    Hp<-H2
    Hp[i,j]<-Hp[i,j]+epsilon
    if(j!=i){
      Hp[j,i]<-Hp[j,i]+epsilon
    }
    vpp<-eigen(Hp)
    val.pert<-(vp$values-vpp$values)/epsilon
    vect.pert<-t(vp$vectors)%*%(vpp$vectors-vp$vectors)/epsilon
    vect.pert<-vect.pert[lower.tri(vect.pert, diag = FALSE)]
    J[,index]<-c(val.pert,vect.pert)
    index<-index+1
  }
}

det<-abs(det(J))
det
vandermonde<-vandermonde.matrix(eigen.values, 10)
det.Vander <-1/abs(det(vandermonde))
det.Vander  
(det-det.Vander)/det.Vander


### EJERCICIO 2 ###

library(elliptic)
fun<-function(x){
  sqrt(2-x^2)/((z-x)*pi)  
}

##0<lambda<sqrt(2)
z1<-complex(10,runif(10,0,sqrt(2)),imaginary = 1)
Wig1<-function(z){
  return(z-sqrt(z^2-2))
}
G1<-c()
int1<-c()
for(i in 1:10){
  z<-z1[i]
  int1<-c(int1,myintegrate(fun,0,sqrt(2)))
  G1<-c(G1,Wig1(z))
}



##0<lambda<-sqrt(2)
z2<-complex(10,runif(10,0,sqrt(2)),imaginary = 1)
Wig2<-function(z){
  return(z+sqrt(z^2-2))
}
G2<-c()
int2<-c()
for(i in 1:10){
  z<-z2[i]
  int2<-c(int2,myintegrate(fun,sqrt(2),0))
  G2<-c(G2,Wig2(z))
}

mean(int2-G2)
mean(int1-G1)
