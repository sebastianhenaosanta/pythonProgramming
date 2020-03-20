my_list = [i for i in range(1,100)]

my_file = open("output.txt", "w")


for i in my_list:
    my_file.write(str(i)+"\n")
    
my_file.close()