import numpy as np

print("Welcome to the NumPy Analyzer!")
print("=" * 40)

arr = None

while True:
    print("\nChoose an option:")
    print("1. Create a NumPy Array")
    print("2. Perform Mathematical Operations")
    print("3. Combine or Split Arrays")
    print("4. Search, Sort, or Filter Arrays")
    print("5. Compute Aggregates and Statistics")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("\nSelect array type:")
        print("1. 1D Array")
        print("2. 2D Array")
        print("3. 3D Array")

        array_choice = int(input("Enter your choice: "))

        if array_choice == 1:
            arr = np.array(list(map(int, input("Enter elements: ").split())))

        elif array_choice == 2:
            rows = int(input("Rows: "))
            cols = int(input("Columns: "))
            elements = list(map(int, input(f"Enter {rows*cols} elements: ").split()))
            arr = np.array(elements).reshape(rows, cols)

        elif array_choice == 3:
            depth = int(input("Enter depth: "))
            rows = int(input("Enter rows: "))
            cols = int(input("Enter columns: "))
            elements = list(map(int, input(f"Enter {depth*rows*cols} elements: ").split()))
            arr = np.array(elements).reshape(depth, rows, cols)
            print("Array created:\n", arr)

        else:
            print("Invalid array type!")
            continue

        print("Array created:\n", arr)

    elif choice == 2:
        print("\nMath Operations:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")

        op = int(input("Enter choice: "))

        rows = int(input("Rows: "))
        cols = int(input("Columns: "))

        a = np.array(list(map(int, input("Enter first array: ").split()))).reshape(rows, cols)
        b = np.array(list(map(int, input("Enter second array: ").split()))).reshape(rows, cols)

        if op == 1:
            print("Result:\n", a + b)
        elif op == 2:
            print("Result:\n", a - b)
        elif op == 3:
            print("Result:\n", a * b)
        elif op == 4:
            if 0 in b:
                print("Error: Division by zero!")
            else:
                print("Result:\n", a / b)
        else:
            print("Invalid operation!")

    elif choice == 3:
        print("\n1. Combine Arrays")
        print("2. Split Array")

        op = int(input("Enter choice: "))

        if op == 1:
            rows = int(input("Rows: "))
            cols = int(input("Columns: "))

            a = np.array(list(map(int, input("Enter first array: ").split()))).reshape(rows, cols)
            b = np.array(list(map(int, input("Enter second array: ").split()))).reshape(rows, cols)

            print("\nVertical Stack:\n", np.vstack((a, b)))

        elif op == 2:
            arr = np.array(list(map(int, input("Enter elements: ").split())))
            parts = int(input("How many parts to split: "))
            print("Split arrays:", np.split(arr, parts))

    elif choice == 4:
        if arr is None:
            print("Create an array first!")
            continue

        print("\n1. Search")
        print("2. Sort")
        print("3. Filter")

        sub = int(input("Enter choice: "))

        if sub == 1:
            val = int(input("Enter value to search: "))
            found = False

            if len(arr.shape) == 1:
                for i in range(len(arr)):
                    if arr[i] == val:
                        print(f"{val} found at index {i}")
                        found = True

            elif len(arr.shape) == 2:
                for i in range(arr.shape[0]):
                    for j in range(arr.shape[1]):
                        if arr[i][j] == val:
                            print(f"{val} found at row {i}, column {j}")
                            found = True

            if not found:
                print(f"{val} not found")

        elif sub == 2:
            print("Original Array:\n", arr)
            if len(arr.shape) == 1:
                print("Sorted Array:", np.sort(arr))
            elif len(arr.shape) == 2:
                print("Sorted Array:\n", np.sort(arr, axis=1))

        elif sub == 3:
            x = int(input("Show values greater than: "))
            print("Filtered values:", arr[arr > x])

    elif choice == 5:
        if arr is None:
            print("Please create an array first!")
            continue

        print("\nChoose an aggregate/statistical operation:")
        print("1. Sum")
        print("2. Mean")
        print("3. Median")
        print("4. Standard Deviation")
        print("5. Variance")

        stat_choice = int(input("Enter your choice: "))

        print("\nOriginal Array:")
        print(arr)

        if stat_choice == 1:
            print("Sum of Array:", np.sum(arr))
        elif stat_choice == 2:
            print("Mean of Array:", np.mean(arr))
        elif stat_choice == 3:
            print("Median of Array:", np.median(arr))
        elif stat_choice == 4:
            print("Standard Deviation:", np.std(arr))
        elif stat_choice == 5:
            print("Variance:", np.var(arr))
        else:
            print("Invalid statistical choice!")

    elif choice == 6:
        print("Thank you for using NumPy Analyzer!")
        break

    else:
        print("Invalid menu choice!")
