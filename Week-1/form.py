def form():
    name=input("Enter yout name:")
    age=input("Enter your age:")
    height=float(input("Enter your height:"))
    country=input("Enter your country:")
    name_upper=name.upper()
    country_upper=country.upper()
    height=round(height,2)
    nickname=(name[0:2].upper()+name[-2:].upper())
    return f"Hello {name_upper}\n You are {age} years old.\n Your height is {height} feet.\n You are from {country_upper}. \n Your nickname is {nickname}."
print(form())
