import matplotlib.pyplot as plt
# gegebne Werte
r = 0.5
a = 1
n = 100

s_n = [] #leere Liste erstellen 
summe = 0 #Anfangswert

for zahl in range (0,n): #solange die zahl in der Range n ist soll...
    term = a*(r**zahl) #Formel anwenden und als neuen Term speichern 
    summe += term #den anfangwert um den term erweitern (addieren)
    s_n.append(summe)
    
 
print (s_n)
plt.plot(s_n)