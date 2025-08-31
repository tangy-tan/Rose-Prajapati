#asks the user to enter a num
num=int(input("enter the number:"))

#check if the number is positive and even
if num>0 and num%2==0:
    print("The number is a positive even number.")

 #If the number is positive and odd
elif num>0 and num%2!=0:
    print("The number is a positive odd number.")

#If the number is negative and even
elif num<0 and num%2==0:
    print("The number is a negative even number.")

#If the number is negative and odd 
elif num<0 and num%2!=0:
    print("The number is a negative odd number.")
    
#If the number is zero
else:
    print("The number is zero.")
