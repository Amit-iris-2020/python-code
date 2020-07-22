def getdate():
    import datetime
    return datetime.datetime.now()

fun2=input("1 for written and 2 for view:")

if fun2=="1":
    fun1 = (input("Please enter \n  Harry: \n  Rohan: \n  Hamid:\n "))
    if (fun1 == "Harry"):
        d1 = (input("Please enter \n 1 for Harry food: \n 2 for Harry ex:\n "))
        if d1 == "1":
            a1 = open("harry food.txt", "a")
            h1 = a1.write((str(getdate())) + input())
            print("successfully writen")
        elif d1 == "2":
            a2 = open("harry ex.txt", "a")
            h2 = a2.write((str(getdate())) + input())
            print("successfully writen")
        else:
            print("You enter a wrong number")
    elif (fun1 == "Rohan"):
        d2 = input("Please enter \n 1 for Rohan food: \n 2 for Rohan ex:\n ")
        if d2 == "1":
            b1 = open("rohan food.txt", "a")
            r1 = b1.write((str(getdate())) + input())
            print("successfully writen")
        elif d2 == "2":
            b2 = open("rohan ex.txt", "a")
            r2 = b2.write((str(getdate())) + input())
            print("successfully writen")
        else:
            print("You enter a wrong number")
    elif (fun1 == "Hamid"):
        d3 = (input("Please enter \n 1 for Hamid food: \n 2 for Hamid ex:\n"))
        if d3 == "1":
            c1 = open("Hamid food.txt", "a")
            x1 = c1.write((str(getdate())) + input())
            print("successfully writen")
        elif d3 == "2":
            c2 = open("Hamid ex.txt", "a")
            x2 = c2.write((str(getdate())) + input())
            print("successfully writen")
        else:
            print("You enter a wrong number")
    else:
        print("Please enter correct petient name")


elif fun2=="2":
    fun1 = (input("Please enter \n  Harry: \n  Rohan: \n  Hamid:\n "))
    if fun1=="Harry":
        d1 = (input("Please enter \n 1 for Harry food: \n 2 for Harry ex:\n "))
        if d1 == "1":
            a1 = open("harry food.txt", )
            h1 = a1.readlines()
            print(h1)
        elif d1 == "2":
            a2 = open("harry ex.txt", )
            h2 = a2.readlines()
            print(h2)
        else:
            print("You enter a wrong number")
    elif (fun1 == "Rohan"):
        d2 = input("Please enter \n 1 for Rohan food: \n 2 for Rohan ex:\n ")
        if d2 == "1":
            b1 = open("rohan food.txt")
            r1 = b1.readlines()
            print(r1)
        elif d2 == "2":
            b2 = open("rohan ex.txt")
            r2 = b2.readlines()
            print(r2)
        else:
            print("You enter a wrong number")
    elif (fun1 == "Hamid"):
        d3 = (input("Please enter \n 1 for Hamid food: \n 2 for Hamid ex:\n"))
        if d3 == "1":
            c1 = open("Hamid food.txt")
            x1 = c1.readlines()
            print(x1)
        elif d3 == "2":
            c2 = open("Hamid ex.txt")
            x2 = c2.readlines()
            print(x2)
        else:
            print("You enter a wrong number")
    else:
        print("Please enter correct petient name")
else:
    print("you enter wrong number")

