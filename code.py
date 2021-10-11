# Health management system
# 3 clients - Mayank , Manan and Manav

def getdate():
    import datetime
    return datetime.datetime.now()

# Total 6 files
# Wrie a function that when executed akes as input client name
# One more function tio retrive exercise or food for any client

# This is program
import datetime
def gettime():
    return datetime.datetime.now()
def take(k):
    if k==1:
        c=int(input("Enter 1 for exersice and 2 for food"))
        if(c==1):
            value=input("Type here\n")
            with open("Mayank-ex.txt", "a") as op:
                op.write(str([str(gettime())])+":"+value+"\n")
            print("Successfully written")
        elif(c==2):
            value = input("Type harder\n")
            with open("Mayank-food.txt", "a") as op:
                op.write(str([str(gettime)])+":" + value + "\n")
            print('Succesfully written')
    elif(k==2):
            c = int(input("Enter 1 fr exersice and 2 for food"))
            if (c == 1):
                value = input("Type here\n")
                with open("Manan-ex.txt", "a") as op:
                    op.write(str([str(gettime)]) + ":" + value + "\n")
                    print('Succesfully written')
            elif (c ==2):
                value = input("Type harder\n")
                with open("Manan-food.txt", "a") as op:
                    op.write(str([str(gettime)]) + ":" + value + "\n")
                    print('Succesfully written')
    elif(k==3):
        c = int(input("Enter 1 fr exersice and 2 for food"))
        if (c == 1):
            value = input("Type here\n")
            with open("Manav-ex.txt", "a") as op:
                op.write(str([str(gettime)]) + ":" + value + "\n")
                print('Succesfully written')
        elif (c == 2):
            value = input("Type harder\n")
            with open("Manav-food.txt", "a") as op:
                op.write(str([str(gettime)]) + ":" + value + "\n")
                print('Succesfully written')
    else:
        print("Please enter validf input (1(Mayank),2(Manan),3(Manav)")
def retrive(k):
    if k==1:
        c=int(input("Enter 1 for exersise and 2 for food"))
        if (c==1):
            with open("Mayank-ex.txt") as op:
                for i in op:
                    print(i,end="")
        elif (c == 2):
            with open("Mayank-food.txt") as op:
                 for i in op:
                    print(i,end="")
        elif (k == 2):
            c = int(input("Enter 1 for exersice and 2 for food"))
            if (c == 1):
                with open("Manan-ex.txt") as op:
                    for i in op:
                        print(i, end="")
            elif (c == 2):
                with open("Manan-food.txt") as op:
                    for i in op:
                        print(i, end="")
        elif (k == 3):
            c = int(input("Enter 1 fr exersice and 2 for food"))
            if (c == 1):
                with open("Manav-ex.txt") as op:
                    for i in op:
                        print(i, end="")
            elif (c == 2):
                with open("Manav-food.txt") as op:
                    for i in op:
                        print(i, end="")
        else:
            print("Enter valid input(Mayank,Manan,Manav")
print("Health Management Sysytem")
a=int(input("Press 1 for the log the value and 2 for the retrive"))

if a==1:
    b = int(input("Press 1 for mayank 2 for manan and 3 for manav"))
    take(b)
else:
    b = int(input("Press 1 for mayank 2 dor manan and 3 for manav"))
    retrive(b)
