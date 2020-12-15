## copying from one file to another, if the line starts with "Upper case" letter:
    
file = open("Demo_copy1.txt","r")
file1 = open("Demo_copy2.txt","w")
for i in file:
    if(i[0][0].isupper()):
        file1.write(i)

print("Execution success!!")
file1.close()
file.close()
    