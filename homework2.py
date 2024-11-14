def buchstaben_ändern(string, buchstabe):
    string_lower = string.lower() #alle charactere in Kleinbuchstaben ändern 
    
    for v in "aeiou":
        new_sentence = [] #leere liste anlegen 
        
        for char in string_lower: # für jeden character in 'string_lower'
            if char == buchstabe: #wenn der character dem ausgewählten buchstaben entspricht 
                new_sentence.append(v) # soll er durch den Vokal erweitert werden 
            else: 
                new_sentence.append(char) #wenn nicht, soll um den ursprünglichen character erweitert werden 
                
        print("".join(new_sentence)) #die einzelnen buschatben zusammen führen 
        
buchstaben_ändern("wie geht es Ihnen ?", "e")
