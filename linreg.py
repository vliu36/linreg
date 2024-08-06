from math import isnan

# Creates a formula for the linear regression line using least squares method
# Returns a tuple (a, b) for the linear form y = ax + b
def linreg(xList=[], yList=[]):
    sumXY = 0
    sumXsq = 0
    sumX = 0
    sumY = 0
    n = min(len(xList), len(yList))
    if type(xList) is not list and type(yList) is not list:
        raise TypeError
    
    for i in range(n):
        if (xList[i] is None or yList[i] is None) or (isnan(xList[i]) or isnan(yList[i])):
            continue
        else:
            sumXY += xList[i] * yList[i]
            sumXsq += xList[i]**2
            sumX += xList[i]
            sumY += yList[i]
    if sumX >= n:
        mult = sumX / n
        a = (sumXY - (sumY * mult)) / (sumXsq - (sumX * mult))
    else:
        mult = n / sumX
        a = (sumY - (sumXY * mult)) / (sumX - (sumXsq * mult))
    b = (sumY - (a * sumX)) / n

    return (a, b)
    
    

    
    


    
