def teilbar(x,y):
    if y == 0:
        print("Es ist nicht möglich durch 0 zu teilen!")
    
    elif x==y:
        print("X und Y sind gleich")
        
    else: 
        if x%y==0:
            print("X ist durch Y teilbar")
        
        else: 
            print("X ist nicht durch Y teilbar")
    
teilbar(4,2)
