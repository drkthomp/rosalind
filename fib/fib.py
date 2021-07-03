
fib_cases = [1,1]

def fib(n, k):
    """Calculates the growth of a population of rabbits"""
    if n <= len(fib_cases): # if we already know the answer
        return fib_cases[n-1] # return it
    # otherwise we calculate it from previous ones
    # 1 month reproductive age + one month gestation
    case = fib(n-1,k) + (k * fib(n-2,k))
    # and remember the answer
    fib_cases.append(case)
    return case

months, pairs = map(int,input().split())
print(fib(months,pairs))
