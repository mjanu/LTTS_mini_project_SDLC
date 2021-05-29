import random
def game1(comp,me):
    if comp==me:
        return None
        
    elif comp=='s':
        if me=='w':
            return False
        elif me=='g':
            return True

    elif comp=='w':
        if me=='s':
            return True
        elif me=='g':
            return False

    elif comp=='g':
        if me=='s':
            return False
        elif me=='w':
            return True
                       
                        
x=random.randint(1,3)
if x==1:
    comp='s'
elif x==2:
    comp='w'
elif x==3:
    comp='g'

me=input("enter your turn")    
print(f"computer choose {comp}")
print(f"I choose {me}")

var1=game1(comp,me) 

if var1==None:
    print("its a tie")
elif var1:
    print("you win")
else:
    print("comp win")          

