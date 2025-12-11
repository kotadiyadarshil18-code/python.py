print("Welcome to the Data Analyzer and Transformer Program")

print("Main menu")

arr=[]

while True:

    print("1. Input data")
    print("2. Display Data summary")
    print("3. Calculate Factorial")
    print("4. Filter data by threshold")
    print("5. Sort data ")
    print("6. Display dataset statistics")
    print("7. Exit program")

    print()

    choice=int(input("Enter your choice from above:"))

    if choice == 1:
       
        data=input("Enter data for a 1D array (separated by spaces):")
        arr=list(map(int,data.split()))
        print(arr)

        print("Data has been stored successfully!")
        print()


    elif choice == 2:

        print("Data summary:")

        print(" - Total element",len(arr))
        print(" - Minimum number",min(arr))
        print(" - Maximum number",max(arr))
        print(" - Sum of all value",sum(arr))
        print(" - Average value",sum(arr)//len(arr))
        print()

    elif choice == 3:
        num=int(input("Enter a number to caluculate its factorial:"))
        def fact(n):
            if n == 0  or n == 1:
                return 1
            else:
                return n * fact(n-1)
        result=fact(num)
        print(f"Factorial of {num} is {result}")
        print()

    elif choice == 4:
        data = list(map(int,data.split()))
        num=int(input("Enter a threshold value to fiter out data above this value :"))

        filtered = list(filter(lambda x: x>=num,data))

        
        print("Filtered data:",filtered 
        )

    elif choice == 5:
        print("Choose sorting option:")

        print("1. Ascending")
        print("2. Descending")

        choice1=int(input("Enter your choice:"))

        if choice1 == 1:
            sorted_arr = sorted(arr)
            print("Sorted Data in Ascending order",sorted_arr)

        elif choice1 == 2:
            sorted_arr = sorted(arr,reverse=True)
            print("Sorted Data in Descending order",sorted_arr)

        else:
            print("invalid choice")

    elif choice == 6:

        print("\nDataset Statistics:")
        print("- Minimum value:", min(arr))
        print("- Maximum value:", max(arr))
        print("- Sum of all values:", sum(arr))
        print("- Average value:", sum(arr) / len(arr))

    elif choice == 7:

        print("Thank you for using the Data Analyzer and Transformer Program. Goodbye!")

        exit()

    else:
        print("Invalid choice")  



