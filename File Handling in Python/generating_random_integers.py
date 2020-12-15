## Generate 50 random integeres and copy to file
from random import randint  ## package to generate random nos.
file = open("RandomIntegers.txt","w")
for i in range(0,51):
    _random_no = (randint(50, 250))
    file.write(str(_random_no)+"\n")  ##converting integer to string
    
file.close()
