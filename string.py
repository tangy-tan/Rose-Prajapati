#string concatenation
print("hello"+"world")
print("hello","world!")

#string repetition:
laugh+"ha"
print(laugh*3)

#string indexing
name="Rachel green"
print(name[-6])

#string slicing to string methods
#fstring, float rounding using fstring
#print \
#ellaborate on assignment
print(name[2:5])
print(name[0:5:2])

#negative index slicing
print(name[-4:-1])
print(name[-1:-4:-1])
print(name[2:]) #print all after 2 index
print(name[:5])
print(name[::2])
print(name[::-2])

#string methods
print(name.upper())
print(name.lower())
print(name.title()) #suru ko letter capital garcha
print(name.isalpha()) #var ma bhako data sabai alphabet ho ki haina check garcha
print(name.isdigit())
print(len(name))
name=name.replace("green","Khan")
print(name)
print(name.startswith("l")) #checks if the var starts with l
print(name.endswith("n"))

#fstring
print(f"name is:{name}")
print("name is :",name)

h=2.2255
print(f"my height is: {h:.2f}")

#snakecase:var(merge two words with underscore)



