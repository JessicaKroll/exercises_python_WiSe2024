#Lösung von ChatGPT
def vokon_zählen(x):
    vokale_liste = list("aeiou")
        
    vokale = 0 
    konsonanten = 0 
    
    for buchstabe in x.lower():
        if buchstabe.isalpha ():
            if buchstabe in vokale_liste:
                vokale += 1
            else:
                konsonanten += 1
                
    return f"  es gibt {vokale} Vokale und {konsonanten} Konsonanten."

print (vokon_zählen("HI,&%/ BerliN!!"))

#Lösung vom Prof 
def vokon_zählen2(x):
    vokale = "aeiou"
    x_lower = x.lower()
    
    buchstaben = [i for i in x_lower if i.isalpha()]
    vokale = [i for i in buchstaben if i in vokale]
    
    #return [len(buchstaben),len(vokale)]

#print(vokon_zählen2("HI,&%/ BerliN!!"))

    print(f" Es gibt {len(vokale)} Vokale und {len(buchstaben)-len(vokale)} Konsonanten")
    
vokon_zählen2("HI,&%/ BerliN!!")
*
        
