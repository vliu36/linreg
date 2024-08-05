import pandas as pd

def main():
    readFile()
    while True:
        choice = menu()
        if choice == "VIEW":
            print(dataset)
        elif choice == "LINREG":
            print("========================== ALL NUMERICAL COLUMNS ==========================")
            validColumns = dataset.select_dtypes(include="number").columns.tolist()
            print(validColumns)
            print()
            yCol = input("Select the y-axis: ")
            xCol = input("Select the x-axis: ")
            try:
                if yCol in validColumns and xCol in validColumns:
                    print(dataset[[yCol, xCol]])
                else:
                    raise KeyError
            except KeyError:
                print("Input column is invalid, please try again.")
                continue
            else:
                if input("Proceed with this selection (y/n)? ") != 'y':
                    continue
            # TODO
            break
        elif choice == "NEW":
            readFile()
        elif choice == "EXIT":
            print("Goodbye.")
            break
        else:
            print("Invalid option, please try again.")
            continue


def menu():
    print("================================= MENU =================================")
    print("VIEW - Preview dataset")
    print("LINREG - Plot linear regression line")
    print("NEW - Choose another dataset")
    print("EXIT - Exit the program")
    print()
    choice = input("Make a selection: ").upper()
    return choice

def readFile():
    global dataset
    try:
        dataset = pd.read_csv(input("Enter .csv file address: "))
    except FileNotFoundError:
        print("ERROR: File not found, please try again.")
        readFile()

try:
    main()
except:
    print("Unknown error occurred, please try again.")