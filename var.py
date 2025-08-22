a = 12
def modify_var():
    global a 
    print(f"Initial value: {a}")
    a = 17
    print(f"Changed value: {a}")
    b = 10
    print (b)

modify_var()