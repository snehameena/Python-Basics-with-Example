## Writing nos from 1 to 10 in Numbers.txt file
## While writing nos. the "int" has to be converted into "str" format

file = open("Number.txt","w")
for i in range(0,11):
    y = str(i)
    file.write(y+" ")
    
file.close()