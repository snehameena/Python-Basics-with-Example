## Fibonacci series
## formula:: find(n-1)+fib(n-2)

def fibonnaci_Series(n):
    if n ==0:
        return 1
    if n==1:
        return 1
    return fibonnaci_Series(n-1)+fibonnaci_Series(n-2)

print(fibonnaci_Series(8))