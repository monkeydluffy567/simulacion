library(readxl)
prueba <- read_excel("C:/Users/gabrielfather/Desktop/prueba.xlsx")
View(prueba)
a=data.frame(  
  "estadistica"=c("media","minimo","maximo","varianza","desviacion estandar"),
  "Nota"=c(mean(prueba$Nota),min(prueba$Nota),max(prueba$Nota),var(prueba$Nota),sd(prueba$Nota)),
  "Edad"=c(mean(prueba$Edad),min(prueba$Edad),max(prueba$Edad),var(prueba$Edad),sd(prueba$Edad))
)
print(a)
View(a)
