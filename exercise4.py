quad_zahl = []  #leere Liste erstellen

for k in range (1,11): #in diesem Bereich 
    
    if k % 2 == 0:  #wenn die Zahl durch 2 teilbar ist, bzw grade ist
        
        quad_zahl.append(k) #Liste durch Zahl erweitern 
    else: quad_zahl.append(k**2)  #Wenn nicht(also ungrade) die Zahl*2 nehmen 
    
print (quad_zahl)

#quad_zahl_1 = [k ** 2 if k % 2 != 0 else k for k in range (1,11)]
quad_zahl_1 = [k if k % 2 == 0 else k**2 for k in range (1,11)]

print (quad_zahl_1)