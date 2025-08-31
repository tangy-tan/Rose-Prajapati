#ask the user for message
greeting = input("Enter a message: ") 

#convert into lowercase
lower_greeting = greeting.lower()        

#if the first word in the greeting string start with 'hello', set output to 0
if lower_greeting.startswith("hello"):          
    output = 0
    
#if the first letter in the greeting string starts with letter 'h', set output to 20
elif lower_greeting[0] == 'h':  
    output = 20

#set output to 100
else:                           
    output = 100      

#display the output
print("Output: $", output)