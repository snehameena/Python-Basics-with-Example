## use of seek() in file handling
file = open("SeekDemo.txt","w+")
file.write("Oh!God!Save!Me!")
file.seek(3)  #(offset,whence)
print(file.tell()) ## tell() tells which position the pointer is upto
print(file.readline())