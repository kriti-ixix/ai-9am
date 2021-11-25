filename = input("Enter a filename: ") + ".txt"

choice = input("Do you want to read the file or write to the file? (r/w) ")

if (choice=='r'):
    myFile = open(filename, 'r')
    rChoice = int(input("1. Read the whole file\n2.Read only one line\nYour choice: "))
    
    if (rChoice==1):
        print("")
        print(myFile.read())
        
    elif (rChoice==2):
        line = "Note " + input("Which note do you want to read? ")
        
        for x in myFile:
            if line in x:
                print(x)
    
    else:
        print("Invalid choice")
    
    myFile.close()
    
elif (choice=='w'):
    myFile = open(filename, 'w')
    notes = int(input("How many notes do you want to write? "))
    
    for i in range(notes):
        myLine = "Note " + str(i+1) + ": " + input("Enter the note: ") + "\n"
        myFile.write(myLine)
        
    myFile.close()
    
else:
    print("Invalid option")
