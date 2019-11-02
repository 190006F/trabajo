#calculadora nro1
#esta calculadora realiza el calculo de área del trapecio(en metros cuadrados)

#declaracion de variables
Base_mayor,altura,base_menor,area_trapecio=0.0,0.0,0.0,0.0

#calculadora
Base_mayor=12.0
base_menor=5.0
altura=10.0
area_trapecio=((Base_mayor+base_menor)/2)*altura

#Mostrar Datos
print("la Base mayor es:",Base_mayor)
print("la base menor es:",base_menor)
print("la altura es:",altura)
print("el area del Trapecio es:",area_trapecio)

print("")
#calculadora nro2
#esta calculadora realiza el calculo de el trabajo desarrollado por una maquina en (joule)

#declaracion de variables
Fuerza,distancia,trabajo=0.0,0.0,0.0
#calculadora
Fuerza=200.5
distancia=20.7
trabajo=Fuerza*distancia
#Mostrar Datos
print("la Fuerza es:",Fuerza,"Newton")
print("la distancia es:",distancia,"metros")
print("el Trabajo desarrollado por la maquina es:",trabajo,"joule")

print("")
#calculadora nro3
#esta calculadora realiza el calculo de la potencia(en Whatts) de una persona al levantar una carga

#declaracion de variables
trabajo,tiempo,potencia=0.0,0.0,0.0

#calculadora
trabajo=50.0
tiempo=60.0
potencia=trabajo/tiempo

#Mostrar Datos
print("el trabajo es:",trabajo,"joule")
print("el tiempo es:",tiempo,"segundos")
print("la potencia desarrollada por la persona es:",potencia,"Whatts")

print("")
#calculadora nro4
#esta calculadora realiza el calculo de el promedio de tres notas

#declaracion de variables
nota1,nota2,nota3,promedio=0.0,0.0,0.0,0.0

#calculadora
nota1=15.0
nota2=10.0
nota3=17.0
promedio=(nota1+nota2+nota3)/3

#Mostrar Datos
print("la nota1 es:",nota1)
print("la nota2 es:",nota2)
print("la nota3 es:",nota3)
print("el promedio de las tres notas es:",promedio)

print("")
#calculadora nro5
#esta calculadora realiza el calculo de el volumen en (metros cúbicos) de un prisma cuadrangular

#declaracion de variables
Area_de_la_base,altura,Volumen=0.0,0.0,0.0

#calculadora
Area_de_la_base=30.2
altura=7.5
Volumen=Area_de_la_base*altura

#Mostrar Datos
print("el área de la base es:",Area_de_la_base)
print("la altura es:",altura)
print("el Volumen del prima es:",Volumen,"metros cúbicos")

print("")
#calculadora nro6
#esta calculadora realiza el calculo de la Densidad en (kilogramos por metro cúbico) de una sustancia

#declaracion de variables
masa,Volumen,Densidad=0.0,0.0,0.0

#calculadora
masa=20.4
Volumen=40.0
Densidad=masa/Volumen

#Mostrar Datos
print("la masa es:",masa,"Kgramo")
print("el volumen es:,",Volumen,"metros cúbico")
print("la Densidad de la sustancia es:",Densidad,"Kgramos/metro cúbico")

print("")
#calculadora nro7
#esta calculadora realiza el calculo de el peso de una carga

#declaracion de variables
masa,gravedad_terrestre,peso=0.0,0.0,0.0

#calculadora
masa=100.0
gravedad_terrestre=9.8
peso=masa*gravedad_terrestre

#Mostrar Datos
print("la masa de la carga es:",masa,"Kgramo")
print("la gravedad terrestre es:",gravedad_terrestre)
print("el peso de la carga es:",peso)

print("")
#calculadora nro8
#esta calculadora realiza el calculo de el valor de una caja se galletas

#declaracion de variables
nro_galletas,costo_galleta,valor_caja_galletas=0,0.0,0.0

#calculadora
nro_galletas=200
costo_galleta=30.0
valor_caja_galletas=nro_galletas*costo_galleta

#Mostrar Datos
print("el numero de galletas es:",nro_galletas)
print("el costo de cada galleta es:",costo_galleta,"centimos")
print("el valor de la caja de galletas es:",valor_caja_galletas,"soles")

print("")
#calculadora nro9
#esta calculadora realiza el calculo de el pago del consumo de agua

#declaracion de variables
nro_litros,costo_cada_litro,pago_por_consumo=0.0,0.0,0.0

#calculadora
nro_litros=25.4
costo_cada_litro=1.0
pago_por_consumo=nro_litros*costo_cada_litro

#Mostrar Datos
print("el numero de litros es:",nro_litros)
print("el costo de cada litro es:",costo_cada_litro,"soles")
print("el pago total por el consumo es:",pago_por_consumo)

print("")
#calculadora nro10
#esta calculadora realiza el calculo de distancia que a rrecorrido un auto que realizo(M.R.U.V)

#declaracion de variables
velocidad_inicial,tiempo,aceleracion,distancia=0.0,0.0,0.0,0.0

#calculadora
velocidad_inicial=24.0
tiempo=8.0
aceleracion=4.0
distancia=(velocidad_inicial*tiempo)+(aceleracion*tiempo**2)/2

#Mostrar Datos
print("la velocidad inicial es:",velocidad_inicial,"metros por segundo")
print("el tiempo en segundos es:",tiempo)
print("la aceleracion es:",aceleracion,"metros/segundo al cuadrado")
print("la distancia que rrecorrio el auto es:",distancia,"metros")

print("")
#calculadora nro11
#esta calculadora realiza el calculo de suma de 10 primeros numeros "n"

#declarar variables
n,suma=0,0

#calculadora
n=10
suma=(n*(n+1))/2

#Mostrar Datos
print("el valor de n es:",n)
print("la suma de los 10 primeros numeros es:",suma)

print("")
#calculadora nro12
#esta calculadora realiza el calculo de la hipotenusa de un triangulo rectangulo en (centímetros)

#declarar variables
cateto1,cateto2,hipotenusa=0.0,0.0,0.0

#calculadora
cateto1=4.0
cateto2=3.0
hipotenusa=(cateto1**2+cateto2**2)**1/2
#Mostrar Datos
print("el cateto1 es:",cateto1)
print("el cateto2 es:",cateto2)
print("el valor de la hipotenusa es:",hipotenusa,"centímetros")

print("")
#calculadora nro13
#esta calculadora realiza el calculo de convercion de temperaturas "desde una temperatura que esta en celcius(c) hacia kelvin(k) y luego a faringe(f)"

#declarar variables
temperatura_C,temperatura_K,temperatura_F=0.0,0.0,0.0

#calculadora
temperatura_C=100.0
temperatura_K=temperatura_C+273                  #formula: C=K-273
temperatura_F=(9*(temperatura_K)-2457+160)/5      #formula: F=(9K-2457+160)/5

#Mostrar Datos
print("la temperatura en grados celcius es:"+str(temperatura_C)+"°")
print("la temperatura en grados Kelvin es:"+str(temperatura_K)+"°")
print("la temperatura en grados Faringe es:"+str(temperatura_F)+"°")

print("")

#calculadora nro14
#esta calculadora realiza el calculo de el área de un triangulo equilátero en (metros cuadrados)

#declarar variables
lado,area_triangulo=0.0,0.0

#calculadora
lado=5.2
area_triangulo=((lado**2)*(3**1/2))/4

#Mostrar Datos
print("el lado en centímetros del triangulo es:",lado)
print("el area del triangulo equilátero es:",area_triangulo,"metros cuadrados")

print("")
#calculadora nro15
#esta calculadora realiza el calculo de el valor de la intensidad de corriente electrica de un material conductor (ley de Ohm)

#declarar variables
voltaje,resistencia,intensidad_corriente=0.0,0.0,0.0

#calculadora
voltaje=240.0
resistencia=150.0
intensidad_corriente=voltaje/resistencia

#Mostrar Datos
print("el valor de el voltaje en voltios es:",voltaje)
print("el valor de la resistencia en ohmmions es:",resistencia)
print("el valor de la intencidad de coriente eléctrica es:",intensidad_corriente,"Amperios")

print("")
#calculadora nro16
#esta calculadora realiza el calculo de la energía cinética de un auto

#declarar variables
masa,velocidad,energia_cinetica=0.0,0.0,0.0

#calculadora
masa=700.4
velocidad=20.0
energia_cinetica=(masa*velocidad**2)/2

#Mostrar Datos
print("el valor de la masa en kilogramos del auto es:",masa)
print("el valor de la velocidad en metros por segundo del auto es:",velocidad)
print("el valor de la Energía cinética del auto es:",energia_cinetica,"joule")

print("")
#calculadora nro17
#esta calculadora realiza el calculo de masa total de un camión (con carga adicional) en una balanza electronica

#declarar variables
masa_carga,masa_camion,masa_total=0.0,0.0,0.0

#calculadora
masa_carga=300.5
masa_camion=1000.0
masa_total=masa_carga+masa_camion

#Mostrar Datos
print("el valor de la masa de la carga:",masa_carga,"Kilogramos")
print("el valor de la masa del camión:",masa_camion,"Kilogramos")
print("el valor de la masa total es:",masa_total,"Kilogramos")

print("")
#calculadora nro18
#esta calculadora realiza el calculo de la suma de ángulos internos de un paralelogramo

#declarar variables
angulo1,angulo2,angulo3,angulo4,suma=0.0,0.0,0.0,0.0,0.0

#calculadora
angulo1=30.5
angulo2=angulo1   #paralelo de lados
angulo3=45.5
angulo4=angulo3   #paralelo de lados
suma=angulo1+angulo2+angulo3+angulo4

#Mostrar Datos
print("el valor de el angulo1 es:"+str(angulo1)+"°")
print("el valor de el angulo2 es:"+str(angulo2)+"°")
print("el valor de el angulo3 es:"+str(angulo3)+"°")
print("el valor de el angulo4 es:"+str(angulo4)+"°")
print("la suma de los ángulos internos del paralelogramo es:"+str(suma)+"°")

print("")
#calculadora nro19
#esta calculadora realiza el calculo de el área total de un tronco de pirmide

#declarar variables
area_lateral,perimetro_base_menor,perimetro_base_mayor,area_total=0.0,0.0,0.0,0.0

#calculadora
area_lateral=55.4
perimetro_base_menor=13.2
perimetro_base_mayor=15.7
area_total=area_lateral+perimetro_base_menor+perimetro_base_mayor

#Mostrar Datos
print("el área lateral en metros cuadrados del tronco de pirámide es:",area_lateral)
print("el perímetro en metros de la base menor es:",perimetro_base_menor)
print("el perímetro en metros de la base mayor es:",perimetro_base_mayor)
print("el área total de el tronco de piramide es:",area_total)

print("")
#calculadora nro20
#esta calculadora realiza el calculo de el precio final de un producto


#declarar variables
precio,igv,precio_final=0.0,0.0,0.0

#calculadora
precio=250.2
igv=0.18*precio
precio_final=precio+igv

#Mostrar Datos
print("el precio del producto es:S/"+str(precio))
print("el IGV del producto es:",igv)
print("el Precio Final del producto es:S/"+str(precio_final))
print("FIN DEL PROGRAMA")
