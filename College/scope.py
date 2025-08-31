#local scope : function bhitra declare garne variable
num_1=5 #global var (can only be read,cannot modify inside function)
def display_num():
    #num=9 #local var
    global num_1 #to modify global var
    num_1=3 #new local var
    return num_1

print(display_num())
print(num_1)


