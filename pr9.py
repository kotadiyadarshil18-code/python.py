import pandas as pd
import matplotlib.pyplot as plt

print("=========== Data Analysis & Visualization Program ===========")

df = None
last_plot = None

while True:
    print("\nPlease select an option:")
    print("1. Load Dataset")
    print("2. Explore Data")
    print("3. Data Manipulation")
    print("4. Handle Missing Data")
    print("5. Descriptive Statistics")
    print("6. Data Visualization")
    print("7. Save Visualization")
    print("8. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        try:
            file = input("Enter CSV file name: ")
            df = pd.read_csv(file)
            print("Dataset Loaded Successfully!")
            print(df.head())
        except:
            print("Error loading file!")

    elif choice == "2":
        if df is None:
            print("Please load dataset first!")
        else:
            print("\n1. First 5 rows")
            print("2. Last 5 rows")
            print("3. Column names")
            print("4. Data types")
            print("5. Info")

            ch = input("Enter choice: ")

            if ch == "1":
                print(df.head())
            elif ch == "2":
                print(df.tail())
            elif ch == "3":
                print(df.columns)
            elif ch == "4":
                print(df.dtypes)
            elif ch == "5":
                print(df.info())
            else:
                print("Invalid choice!")

    elif choice == "3":
        if df is None:
            print("Please load dataset first!")
        else:
            print("\n== Data Manipulation ==")
            print("1. Mathematical Operations on Column")
            print("2. Combine (Merge) Another CSV")
            print("3. Split Data by Column Value")

            op = input("Choose operation: ")

            if op == "1":
                col = input("Enter numeric column (e.g. Sales): ")
                if col in df.columns:
                    print("a. Add 10")
                    print("b. Subtract 10")
                    print("c. Multiply by 2")
                    print("d. Divide by 2")

                    ch = input("Choose: ")

                    if ch == "a":
                        df[col] = df[col] + 10
                    elif ch == "b":
                        df[col] = df[col] - 10
                    elif ch == "c":
                        df[col] = df[col] * 2
                    elif ch == "d":
                        df[col] = df[col] / 2
                    else:
                        print("Invalid option!")

                    print("Updated Data:")
                    print(df[[col]].head())
                else:
                    print("Column not found!")

            elif op == "2":
                try:
                    file2 = input("Enter second CSV file: ")
                    df2 = pd.read_csv(file2)

                    print("First file columns:", list(df.columns))
                    print("Second file columns:", list(df2.columns))

                    key = input("Enter common column to merge: ")

                    if key in df.columns and key in df2.columns:
                        df = pd.merge(df, df2, on=key)
                        print("Merged Successfully!")
                        print(df.head())
                    else:
                        print("Common column not found!")
                except:
                    print("Error merging files!")

            elif op == "3":
                col = input("Enter column to split by (Region/Product): ")
                if col in df.columns:
                    print("Available values:", df[col].unique())
                    val = input("Enter value: ")

                    new_df = df[df[col] == val]
                    print("Filtered Data:")
                    print(new_df.head())

                    save = input("Save to CSV? (y/n): ")
                    if save.lower() == "y":
                        name = input("Enter file name: ")
                        new_df.to_csv(name, index=False)
                        print("File saved!")
                else:
                    print("Column not found!")

            else:
                print("Invalid choice!")

    elif choice == "4":
        if df is None:
            print("Please load dataset first!")
        else:
            while True:
                print("\n1. Show missing rows")
                print("2. Fill with mean")
                print("3. Drop missing rows")
                print("4. Replace with value")
                print("5. Back")

                sub = input("Enter choice: ")

                if sub == "1":
                    print(df[df.isnull().any(axis=1)])
                elif sub == "2":
                    df = df.apply(lambda c: c.fillna(c.mean()) if c.dtype != 'object' else c)
                    print("Filled with mean!")
                elif sub == "3":
                    df.dropna(inplace=True)
                    print("Rows dropped!")
                elif sub == "4":
                    v = input("Enter value: ")
                    df.fillna(v, inplace=True)
                    print("Replaced!")
                elif sub == "5":
                    break
                else:
                    print("Invalid choice!")

    elif choice == "5":
        if df is None:
            print("Please load dataset first!")
        else:
            print(df.describe())

    elif choice == "6":
        if df is None:
            print("Please load dataset first!")
        else:
            print("\n1. Bar Plot")
            print("2. Line Plot")
            print("3. Scatter Plot")
            print("4. Pie Chart")
            print("5. Histogram")
            print("6. Stack Plot")

            ch = input("Enter choice: ")
            plt.figure()

            if ch == "1":
                col = input("Column: ")
                if col in df.columns:
                    df[col].value_counts().plot(kind='bar')
            elif ch == "2":
                col = input("Column: ")
                if col in df.columns:
                    df[col].plot()
            elif ch == "3":
                x = input("X column: ")
                y = input("Y column: ")
                if x in df.columns and y in df.columns:
                    plt.scatter(df[x], df[y])
                    plt.xlabel(x); plt.ylabel(y)
            elif ch == "4":
                col = input("Column: ")
                if col in df.columns:
                    df[col].value_counts().plot(kind='pie', autopct='%1.1f%%')
                    plt.ylabel("")
            elif ch == "5":
                col = input("Column: ")
                if col in df.columns:
                    df[col].plot(kind='hist')
            elif ch == "6":
                print("Columns:", list(df.columns))
                cols = input("Enter columns comma separated: ").split(",")
                cols = [c.strip() for c in cols if c.strip() in df.columns]
                if len(cols) >= 2:
                    plt.stackplot(range(len(df)), *[df[c] for c in cols], labels=cols)
                    plt.legend()
            else:
                print("Invalid!")

            plt.show()
            last_plot = plt

    elif choice == "7":
        if last_plot is None:
            print("No graph to save!")
        else:
            name = input("Enter image name (graph.png): ")
            plt.savefig(name)
            print("Saved successfully!")

    elif choice == "8":
        print("Program Ended. Thank you!")
        break

    else: 
        print("Invalid choice. Please try again")
