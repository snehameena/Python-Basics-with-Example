file = open("Numbers.txt","r")
total_num = file.readline() ## Reads the first line of total number of integers
sum = 0
for i in range(int(total_num)):
    sum = sum + int(file.readline())

print(sum)
file.close()