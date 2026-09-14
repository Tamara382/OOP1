mylist = [1,2,3,4,5,6,7,8,9,10]


while 1:
    print ("print 1 to add an element to the list")
    print ("print 2 to remove an element from the list")
    print ("print 3 to replace an element in the list")
    print ("print 4 to sort the list")
    print ("print 5 to exit")
    choice = input("enter your choice:")
    if choice=="1":
        mylist.append(int(input("enter the number to add:")))
        print(mylist)
    elif choice=="2":
        mylist.remove(int(input("enter the number to remove:")))
        print (mylist)
    elif choice=="3":
        index=mylist.index(int(input("enter the number to replace:")))
        mylist[index]=int(input("enter the new value:"))
        print(mylist)
    elif choice=="4":
        mylist.sort()
        print(mylist)
    else:
        break
