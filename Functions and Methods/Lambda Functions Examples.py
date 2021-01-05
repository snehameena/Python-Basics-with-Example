## Lambda Expressions:

## Normal way to cal area,    
def area(n):
    value = n**2
    print("area::",value)

area((2))

## Using lambda

val = lambda n:n**2
print(val(2))