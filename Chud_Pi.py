import decimal
from math import factorial

import decimal
from tokenize import Comment


context = decimal.getcontext()

desired_precision = 1000000
context.prec = desired_precision


def chudnovsky_algorithm(iterations):
    decimal.getcontext().prec = iterations + 2
    
    C = 426880 * decimal.Decimal(10005).sqrt()
    K = int(6)
    M = decimal.Decimal(1)
    L = decimal.Decimal(13591409)
    X = decimal.Decimal(1)
    S = L
    
    for _ in range(1, iterations + 1):
        M *= int((K ** 3) / (factorial(K) ** 3))
        L += 545140134
        X *= -262537412640768000
        S += decimal.Decimal(M * L) / X
        K += 12
    
        return C / S

def new_func():
    iterations = 100000000 #Change Iterations for more/less decimal places. 
    return iterations

iterations = new_func() 

result = chudnovsky_algorithm(iterations)
print("Approximation of π using Chudnovsky algorithm:", result)
