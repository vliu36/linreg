# linreg
Python project that calculates and plots linear regression 

## Getting Started
Clone this repository to your local machine:
1. Start the program by running `main.py`
2. Enter the file location of your `.csv` file
3. From there, a menu of options will appear:<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Enter **VIEW** to view an abbreviated form of the selected dataset.<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Enter **LINREG** to calculate and graph a linear regression line.<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Enter **NEW** to select another dataset.<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Enter **EXIT** to exit the program.<br />

To proceed with calculating the linear regression line, enter LINREG, then:
1. Input the x and y variables (case-sensitive)
2. The program will display a preview of the selected variables, enter ‘y’ to proceed or ‘n’ to return to the menu
3. The program will then return the equation for the line of best fit, as well as the coefficient of determination (r^2)
4. Enter ‘y’ to view the a graph of the dataset or ‘n’ to exit the program

## Key Libraries Used
[Pandas](https://pandas.pydata.org/): A powerful data analysis and manipulation tool.

[Matplotlib Pylot](https://matplotlib.org/stable/tutorials/pyplot.html): A collection of functions that allows for plotting and the visualization of data.

## Sample Datasets
A directory of sample datasets are provided in `datasets\`. They were sourced from [MainakRepositor's Datasets](https://github.com/MainakRepositor/Datasets/tree/master).

## Additional Information
`main.py` contains helper functions that handle reading files and the prompts shown on the command line.
`linreg.py` contains two functions: `linreg()` and `eval()`.

`linreg()` takes in two lists (x, y) and returns a tuple (a, b) that corresponds to the linear form y = ax + b pf the linear regression line.
`eval()` takes in two lists (x, y) and a tuple (a, b) and returns r^2 as a float



