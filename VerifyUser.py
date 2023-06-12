print("Hello User")
attempts=0
while attempts <3:
    
 subbu=input("Enter your name: ")
 if subbu.lower()=='subhash':
     inp=input("Are you real?(Y/N) ")
     if inp.lower()=="y":
         print("Ok, I trust ya")
         break
     else:
         print("Sorry, no messing up here")
 else:
     print("We don't allow anyone but Subhash here")
     attempts +=1
if attempts==3:
    print("Maximum attempts exceeded. Get hella outta here!")
     
