import pandas as pd
import matplotlib.pyplot as plt
from linreg import *

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
            equation = linreg(dataset[xCol].tolist(), dataset[yCol].tolist())
            print(f"The line of best fit is y = {equation[0]}x{" + " if equation[1] >= 0 else " - "}{abs(equation[1])}")
            determination = eval(dataset[xCol].tolist(), dataset[yCol].tolist(), equation)
            print(f"{determination * 100}% of the observed variation in {yCol} can be attributed to {xCol}.")
            if input("Plot (y/n)? ") != "y":
                break
            else:
                fig, ax = plt.subplots()
                ax.scatter(dataset[xCol].tolist(), dataset[yCol].tolist())
                xGen = [i for i in range(int(min(dataset[xCol].tolist())), int(max(dataset[xCol].tolist())) + 2)]
                ax.plot(xGen, list(map(lambda x : (equation[0] * x) + equation[1], xGen)), linewidth=2, color="r")
                ax.set_xlabel(xCol)
                ax.set_ylabel(yCol)
                plt.show()
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

# try:
main()
# except:
#     print("Unknown error occurred, please try again.")