import matplotlib.pyplot as plt

def spar_funktion(AK, SR, i, lz):
    kapital = AK
    
    #Liste um jährliche Kapitalentwicklung zu speichern
    gesamt_kapital =[] 
    
    # for-Schleife für jedes Jahr der Laufzeit 
    for k in range(1,lz+1):
        kapital = SR + kapital *(1+i)
        gesamt_kapital.append(round(kapital, 2))
        
    return gesamt_kapital

#print(spar_funktion(AK=10000, 
#                    SR=1000, 
 #                   i=0.01, 
  #                  lz=10))

sparplan= spar_funktion(AK=10000, 
                    SR=1000, 
                    i=0.01, 
                    lz=10)
        
plt.bar(range(1,11),sparplan)  #Jahr 1 bis 11

    