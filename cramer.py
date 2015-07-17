# -*- coding: utf-8 -*-
print "Algoritmo Informatico per calcolo di soluzioni del sistema con Metodo di Cramer"
print "Attenzione: Con i sistemi fratti potrebbe non funzionare bene"
a1 = input("inserisci il coeff. di x: ")
b1 = input("inserisci il coeff. di y: ")
a2 = input("inserisci il coeff. di x': ")
b2 = input("inserisci il coeff. di y': ")
tn1 = input("inserisci il primo termine noto: ")
tn2 = input("inserisci il secondo termine noto: ")
determinante = a1*b2 - a2*b1
determinantex = tn1*b2 - tn2*b1
determinantey = a1*tn2 - a2*tn1
#determinante = determinante*1.0
#determinantex = determinantex*1.0
#determinantey = determinantey*1.0
if determinantex == int(determinantex):
	x = determinantex/determinante
else:
	x = str(determinantex) + "/" + str(determinante)
if determinantex == int(determinantex):
	y = str(determinantey) + "/" + str(determinante)
else:
	y = determinantey/determinante
print "La x è", x
print "La y è", y
