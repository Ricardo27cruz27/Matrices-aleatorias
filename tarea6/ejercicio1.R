b<-1
s_b<-.01
s_f<-0.000158
s_e<-0.0045
n<-80
k<-4
N<-100
cota<-(((s_e)/(s_f*s_b))^2)/n


l_1<-c()
l_2<-c()
l_3<-c()
l_1_hat<-c()
l_2_hat<-c()
l_3_hat<-c()

for(p in 50:200){
  l_1<-c(l_1,(s_f*p*(b*b*k+s_b))+s_e)
  l_2<-c(l_2,(s_f*p*s_b)+s_e)
  l_3<-c(l_3,s_e)
  l_1_hat<-c(l_1_hat,((s_f*p*(b*b*k+s_b))+s_e)*(1+(s_e/(n*s_f*(s_b+(k*b^2))))))
  if(p>=cota){
    l_2_hat<-c(l_2_hat,((s_f*p*s_b)+s_e)*(1+(s_e/(n*s_f*s_b))))
  }
  else{
    l_2_hat<-c(l_2_hat,s_e*((1+sqrt(p/n))^2))
  }
  l_3_hat<-c(l_3_hat,s_e*((1+sqrt(p/n))^2))
}

plot(rep(50:200,6),
     c(l_1,l_2,l_3,l_1_hat,l_2_hat,l_3_hat),
     col=c(rep(1,151),rep(2,151),rep(3,151),rep(4,151),rep(5,151),rep(6,151)))
plot(rep(50:200,3),c(l_1,l_2,l_3),col=c(rep(1,151),rep(2,151),rep(3,151)))



#R=LF'+e
R<-function(){
  resultado<-c()
  for(p in 50:200){
    L<-matrix(rnorm(p*k,b,sqrt(s_b)),p,k)
    F_<-matrix(rnorm(n*k,0,sqrt(s_f)),n,k)
    e<-matrix(rnorm(p*n,0,sqrt(s_e)),p,n)
    R<-L%*%t(F_)+e
    SIGMA<-R%*%t(R)/n
    resultado<-c(resultado,eigen(SIGMA)$values[1:5])
  }
  return(resultado)
}



sim<-R()
sim

v<-c()
for (i in 50:200) {
  v<-c(v,rep(i,5))
}
plot(v,sim,col=rep(1:5,151),frame.plot = F)



simulaciones<-function(N){
  simulaciones<-matrix(0,N,755)
  for(i in 1:N){
    simulaciones[i,]<-R()
  }
  return(simulaciones)
}

SIMULACIONES<-simulaciones(N)


v2<-c()
for (i in 50:200) {
  v2<-c(v2,rep(i,N*5))
}


tercer<-function(datos){
  quantile(datos,.75)
}
primer<-function(datos){
  quantile(datos,.25)
}

plot(v2,SIMULACIONES,xlab="p")
lines(v[which(1:length(v)%%5==1)],
      primerquartil[which(1:length(v)%%5==1)],
      col="red", lty = 2)
lines(v[which(1:length(v)%%5==1)],
      tercerquartil[which(1:length(v)%%5==1)],
      col="blue", lty =2)
lines(v[which(1:length(v)%%5==1)],
      promedio[which(1:length(v)%%5==1)],
      col="white",lty=2)
lines(50:200,l_1,col="green")
lines(50:200,l_2,col="green")
lines(50:200,l_3,col="green")

#prom<-colSums(SIMULACIONES)/2
promedio<-apply(SIMULACIONES, 2,mean)
primerquartil<-apply(SIMULACIONES, 2, tercer)
tercerquartil<-apply(SIMULACIONES,2,primer)


#plot(v,tercerquartil,col="blue")

legend(50, .2, legend=c("3q L1", "mean L1","1q L1","teoricos"),
       col=c("red", "white","blue","green"), lty=c(2,2,2,1), cex=0.8)




#PLOT CON LA CORRECCION
plot(v2,SIMULACIONES,xlab="p")
lines(v[which(1:length(v)%%5==1)],
      primerquartil[which(1:length(v)%%5==1)],
      col="red", lty = 2)
lines(v[which(1:length(v)%%5==1)],
      tercerquartil[which(1:length(v)%%5==1)],
      col="blue", lty =2)
lines(v[which(1:length(v)%%5==1)],
      promedio[which(1:length(v)%%5==1)],
      col="white",lty=2)
lines(50:200,l_1_hat,col="green")
lines(50:200,l_2_hat,col="green")
lines(50:200,l_3_hat,col="green")
