while True:
    print("1. Generate a patten")
    print("2. Analyze a range of number")
    print("3. Exit")

    choice=int(input("Choise a number from above:"))

    if choice == 1:
        rows=int(input("Enter the rows"))

        for i in range (1,rows+1):
            print("*"*i)

    elif choice == 2:
        start_num=int(input("Enter the number from where you want to start:"))
        end_num=int(input("Enter the number from  where you want end"))
        total=0

        for n in range(start_num,end_num + 1):
            if n % 2 == 0:
                print("Number is even",n)
            else:
                print("Number is odd",n)
 
            total += n

            print(f"Total sum of number from {start_num} to {end_num} are",total)

    elif choice == 3:
        print("Goodby")

        exit()

    else:
        print("Invaled choice",choice)
    



 