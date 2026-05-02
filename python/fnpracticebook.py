def names(name ):
    l = ['ram','shyam','ghanshyam','murli','virat']
    print("Welcome to student name checker ")
    print ("Enter the name of the student (enter 'q' to exit)")
    if(name == 'q'):
            return 
    if name in l:
            print("THAT STUDENT is enrolled iN THE OLLEGE RBU")
    else : 
            print("no ,  that student is not in the class")
    print("GOOD BYE !!") 

names('q')