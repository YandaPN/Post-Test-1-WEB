def fibonacci_search(arr, x):
    n = len(arr)
    fib2 = 0  # fib(n-2)
    fib1 = 1  # fib(n-1)
    fib = fib2 + fib1  # fib(n)
    
    while fib < n:
        fib2 = fib1
        fib1 = fib
        fib = fib2 + fib1
    
    offset = -1
    
    while fib > 1:
        i = min(offset+fib2, n-1)
        if arr[i] < x:
            fib = fib1
            fib1 = fib2
            fib2 = fib - fib1
            offset = i
        elif arr[i] > x:
            fib = fib2
            fib1 = fib1 - fib2
            fib2 = fib - fib1
        else:
            return i
    
    if fib1 == 1 and arr[offset+1] == x:
        return offset+1
    
    return -1


var = ["Arsel", "Avivah", "Daiva", ["Wahyu", "Wibi"]]
x = "Wahyu"

for i in range(len(var)):
    if type(var[i]) == list:
        index = fibonacci_search(var[i], x)
        if index != -1:
            print(f"{x} ada index {i} pada kolom {index}")
