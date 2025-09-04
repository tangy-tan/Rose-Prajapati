#while loop
i=0
while i<5:
    print(i)
    i+=1 #i=i+1,i++
    
#infinite loop
#-while True:
#-  print("")

name=""
while name!="Rose":
    name= input("Enter your name: ")

#foor loop : 
string1 = "Happy Life"
for char in string1:
    print(char)

#range():create iterable
print(list(range(10)))

for i in range(10,2,-1):
    print(i)

#break=loop stops 

while True:
    name = input("Enter your name: ")
    if name=="rose" :
        break

#continue= skip the loop
for i in range(0,10):
    if i%2==0: #even
        continue
    else:
        print(i)


