# Spataru Dionisie FAF-211
import time
import matplotlib.pyplot as plt
import sys
sys.setrecursionlimit(2000)

def fib_recursion(n):
    if n<=0:
        return 0
    elif n==1:
        return 1
    else:
        return fib_recursion(n-1)+fib_recursion(n-2)

def fib_iteration(n):
    a,b = 0,1
    for i in range(n):
        a,b = b,a+b
    return a

def fib_dynamic(n, memo = {}):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    elif n not in memo:
        memo[n] = fib_dynamic(n-1, memo) + fib_dynamic(n-2, memo)
    return memo[n]

def fib_matrix(n):
    if n<= 0:
        return 0
    elif n == 1:
        return 1
    else:
        fib_matrix_helper(n-1)

def fib_matrix_helper(n):
    if n == 0:
        return (0,1)
    else:
        a,b = fib_matrix_helper(n // 2)
        c = a * ((2 * b) - a)
        d = a * a + b * b
        if n % 2 == 0:
            return (c,d)
        else:
            return (d,c + d)

def fib_binet(n):
    golden_ratio = (1 + 5 ** 0.5) / 2
    return int((golden_ratio ** n - (1 - golden_ratio) ** n) / 5 ** 0.5)

def fibonacci_recursive_v2(n, prev_prev=0, prev=1):
    if n == 0:
        return prev_prev
    elif n == 1:
        return prev
    else:
        return fibonacci_recursive_v2(n-1, prev, prev_prev + prev)

def createGraph(n,fib):
    x = list(range(n))
    y = []
    t = []
    return_values = []
    return_time_values = []
    full_time = time.time()
    for i in range(n):
        start_time = time.time()
        value = fib(i)
        return_values.append(value)
        end_time = time.time()
        y.append(value)
        elapsed_time = end_time - start_time
        return_time_values.append(round(elapsed_time, 4))
        t.append(round(elapsed_time, 4))
    full_time_end = time.time()
    full_esp = full_time_end - full_time
    plt.plot(x, t)
    plt.xlabel("n")
    plt.ylabel("Time (seconds)")
    plt.title("Recursive_v2 graph")
    plt.show()
    return return_values, return_time_values, full_esp

start_time = time.time()
createGraph(1000,fibonacci_recursive_v2)
end_time = time.time()
total_time = end_time - start_time
print("Total time of execution: ", total_time, "seconds")
print(fibonacci_recursive_v2(1000))