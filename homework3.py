import matplotlib.pyplot as plt

def buchstaben_häufigheit (x):
    mein_d = {} # {} weil ist ein dictionary 
    
    for b in x.lower():
        if b.isalpha(): # wenn das Element ein Buschstabe ist 
            if b not in mein_d:# Falls der Buchstabe noch nicht in unserer dictionary ist 
                mein_d[b]= 1 # 1 weil erster Eintrag
            else: #wenn Buchstabe schon existiert 
                mein_d[b] += 1 # 1 addieren 
    
    mein_d_sorted = dict(sorted(mein_d.items()))
    
    return mein_d_sorted

bh_dict1 = buchstaben_häufigheit(x = "123Wie geht es Ihnen%$?")
bh_dict2 = buchstaben_häufigheit(x = "Hallo, Berlin!")

plt.bar(bh_dict1.keys(), bh_dict1.values())
plt.bar(bh_dict2.keys(), bh_dict2.values())

