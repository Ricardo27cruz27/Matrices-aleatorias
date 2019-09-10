### TAREA 3 ###

## Ejercicio 1 ##
m=10000
p=c(10,100)

#semicirculo de Wigner
wigner<-function(x){
  return(sqrt(2-(x^2))/pi)
}

#GOE
goe<-function(p){
  H<-matrix(rnorm(p*p),p,p)
  Hs<-(H+t(H))/2
  return(eigen(Hs)$value)
}

vp.goe.10<-c()
for(i in 1:m){
  vp.goe.10<-c(vp.goe.10,goe(10))  
}
vp.goe.100<-c()
for(i in 1:m){
  vp.goe.100<-c(vp.goe.100,goe(100))
}

curve(wigner(x),from = sqrt(1.999999),
      to = -sqrt(1.999999),
      col="black",
      ylim = c(0,.5),xlim=c(-2,2))
#p=10 goe
goe.den.10<-density(vp.goe.10/sqrt(10))
points(goe.den.10$x,goe.den.10$y,type = 'l',col="red")

#p=100 goe
goe.den.100<-density(vp.goe.100/sqrt(100))
points(goe.den.100$x,goe.den.100$y,type = 'l',col="red")



#GUE
rcomplex<-function(p){
  return(complex(real = rnorm(p),imaginary = rnorm(p)))
}

gue<-function(p){
  H<-matrix(0,p,p)
  for(i in 1:p){
    for(j in 1:i){
      if(i==j){
        H[i,j]<-rnorm(1)
      }
      else{
        H[i,j]<-rcomplex(1)
        H[j,i]<-Conj(H[i,j])
      }
    }
  }
  Hs<-(H+t(H))/2
  return(eigen(Hs)$value)
}

vp.gue.10<-c()
for(i in 1:m){
  vp.gue.10<-c(vp.gue.10,gue(10))  
}
vp.gue.100<-c()
for(i in 1:m){
  vp.gue.100<-c(vp.gue.100,gue(100))
}

curve(wigner(x),from = sqrt(1.999999),
      to = -sqrt(1.999999),
      col="black",
      ylim = c(0,.5),xlim=c(-2,2))
#p=10 gue
gue.den.10<-density(vp.gue.10/sqrt(20))
points(gue.den.10$x,gue.den.10$y,type = 'l',col="darkblue")

#p=100 gue
gue.den.100<-density(vp.gue.100/sqrt(200))
points(gue.den.100$x,gue.den.100$y,type = 'l',col="darkblue")



#GSE
gse<-function(p){
  q<-p/2
  X<-matrix(rcomplex(q*q),q,q)
  Y<-matrix(rcomplex(q*q),q,q)
  H1<-cbind(X,Y)
  H2<-cbind(-Conj(Y),Conj(X))
  H<-rbind(H1,H2)
  Hs<-(H+t(Conj(H)))/2
  return(eigen(Hs)$value)
}

vp.gse.10<-c()
for(i in 1:m){
  vp.gse.10<-c(vp.gse.10,gse(20))  
}
vp.gse.100<-c()
for(i in 1:m){
  vp.gse.100<-c(vp.gse.100,gse(200))
}

curve(wigner(x),from = sqrt(1.999999),
      to = -sqrt(1.999999),
      col="black",add=T,
      ylim = c(0,.5),xlim=c(-2,2))
#p=10 gse
gse.den.10<-density(vp.gse.10/sqrt(40))
plot(gse.den.10$x,gse.den.10$y,type = 'l',col="green")

#p=100 gse
gse.den.100<-density(vp.gse.100/sqrt(400))
plot(gse.den.100$x,gse.den.100$y,type = 'l',col="green")



curve(wigner(x),from = sqrt(1.999999),
      to = -sqrt(1.999999),
      col="black",
      ylim = c(0,.5),xlim=c(-2,2),
      ylab="p(x)",main="P=10",lwd=2)
points(goe.den.10$x,goe.den.10$y,type = 'l',col="red",lwd=2)
points(gue.den.10$x,gue.den.10$y,type = 'l',col="darkblue",lwd=2)
points(gse.den.10$x,gse.den.10$y,type = 'l',col="green",lwd=2)
legend(-2,.5,legend = c("Wigner","GOE","GUE","GSE"),lwd = 1.2,col = c("black","red","darkblue","green"),cex = .5)

curve(wigner(x),from = sqrt(1.999999),
      to = -sqrt(1.999999),
      col="black",
      ylim = c(0,.5),xlim=c(-2,2),
      ylab="p(x)",main="P=100",lwd=2)
points(goe.den.100$x,goe.den.100$y,type = 'l',col="red",lwd=2)
points(gue.den.100$x,gue.den.100$y,type = 'l',col="darkblue",lwd=2)
points(gse.den.100$x,gse.den.100$y,type = 'l',col="green",lwd=2)
legend(-2,.5,legend = c("Wigner","GOE","GUE","GSE"),lwd = 1.2,col = c("black","red","darkblue","green"),cex = .5)




## EJERCICIO 2
m=1000
p=100

ps<-function(s){
  return((pi*s/2)*exp(-pi*(s^2)/4))
}


dif100<-c()
for(i in 1:m){
  ordenados<-sort(goe(p))
  for (j in 1:(p-1)) {
    dif100<-c(dif100,
              ordenados[j+1]-ordenados[j])
  }
}

dif2<-c()
for(i in 1:m){
  ordenados<-sort(goe(2))
  for (j in 1:(2-1)) {
    dif2<-c(dif2,
              ordenados[j+1]-ordenados[j])
  }
}

curve(ps(x),from = 0,
      to = 5,
      col="black",
#      ylim=c(0,1),
      ylab="p(x)",main="diferencias",lwd=2)


den.dif<-density(dif100)
points(den.dif$x,den.dif$y,
       type = 'h',
       col="purple")
den.dif<-density(dif2)
points(den.dif$x,den.dif$y,
       type = 'h',
       col="red")

