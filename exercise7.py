def buchstaben_zählen(text): #Funktion erstellen
    text_list = list(text)
    text_buchstaben = [i for i in text_list if i.isalpha()]
    text_buchstaben_len= len(text_buchstaben)
    return text_buchstaben_len
    #buchstaben = [char for char in text if char.isalpha()] #
   # return len(buchstaben)

print(buchstaben_zählen("Hallo, Berlin"))
print(buchstaben_zählen("Hallo, Berlin%$6!"))

