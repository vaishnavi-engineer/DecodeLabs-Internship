password = input("Enter your password: ")

length = len(password)

upper = False
number = False
symbol = False

for i in password:
    if i.isupper():
        upper = True
    elif i.isdigit():
        number = True
    elif not i.isalnum():
        symbol = True

if length < 8:
    print("Password Strength: Weak")

elif length >= 8 and ((upper and number) or (upper and symbol) or (number and symbol)):
    if upper and number and symbol:
        print("Password Strength: Strong")
    else:
        print("Password Strength: Medium")

else:
    print("Password Strength: Weak")