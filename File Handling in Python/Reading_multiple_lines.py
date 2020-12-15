## Reading multiple item in 1 line using split function()
## REad each line marks and calculate sum of each line marks and find which is greatest sum


file = open("grades.txt","r")
total_num_rows = file.readline()
marks = []
sum_large = 0
for i in range (int(total_num_rows)):
   marks = file.readline().split()
   print("the marks are:",marks)
   sum = 0
   
   for j in range(len(marks)):
       sum = sum + int(marks[j])
   if sum > sum_large:
       sum_large = sum
   print(sum)
   
print(sum_large)
file.close()
