## Solving a quadratic equation:
## equation : d = b.pow(2) - 4ac

def equation_solving(a,b,c):
    val = (b**2)- 4*a*c
    print("The solved val:",val)
    return val

def finding_roots(solved_val):
    if (solved_val>0):
        print("Equation has 2 real roots!!")
    elif(solved_val==0):
        print("Equation has one real root!!")
    else:
        print("Equation has 2 complex roots")



solved_val = equation_solving(1, 2, 3)
finding_roots(solved_val)