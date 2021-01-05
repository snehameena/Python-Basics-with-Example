## Local and Global Scope:
    
## Local variable from local scope
a = 5
def var_scope(a):
    a = 10
    print(a)

var_scope(a)

## Global variable in local scope
def var_scope1(a):
    print(a)

var_scope1(a)

## Local scope referred globally
def var_scope2(a):
    b=10
    print("Locally val is:",b)
var_scope2(a)
#print("globally:",b)    

## Local value made global

i = 10
def local_to_global_var():
    global i
    i = 15
    print("Value of i:",i)

local_to_global_var()
print("Now value of i:",i)
