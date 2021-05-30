
def game1(comp,me):
    if comp==me:
        return 3
        
    elif comp==4:
        if me==5:
            return 1
        elif me==6:
            return(2)

    elif comp==5:
        if me==4:
            return(2)
        elif me==6:
            return(1)

    elif comp==6:
        if me==4:
           return(1)
        elif me==5:
            return(2)
                       
                        
x=game1(4,5)

if x ==1:
    print('true')