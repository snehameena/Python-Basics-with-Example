## Find Sum of numbers in specific range dynamically
def sum_of_digits(x,y):
    sum = 0
    for i in range (x,y):
        sum = sum+i
    print("Total Sum:",sum)
        
        

sum_of_digits(1,26)
sum_of_digits(50,76)