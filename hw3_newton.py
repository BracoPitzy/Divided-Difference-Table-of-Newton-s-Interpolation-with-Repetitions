import numpy as np
import math

def inputdata():
    n = int(input())
    x = list(map(lambda x: float(x), input().split()))
    y = list(map(lambda x:float(x),input().split()))
    x = np.array(x)
    y = np.array(y)
    return x, y
    
def outputdata(s):
    for item in s:
        formatted_number = "{:.4f}".format(item)
        print(formatted_number, end=' ')
        
def count_duplicates(numbers):
    counts = {}
    for num in numbers:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1
        
    order = []
    for value in counts.values():
        order.append(value)
    
    return order

def DividedDiffWithRepetitions(x, y):
    #to calculate the divided differences table with repetitions.
    #您需要在此完成您的代码.
    
    return coeff

[x,y]=inputdata()
a_s = np.diagonal(DividedDiffWithRepetitions(x, y))
outputdata(a_s)