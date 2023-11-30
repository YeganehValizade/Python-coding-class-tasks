a = input("Please tell me the first side amount: ")
b = input("next, the second side:")
c = input("finally, the last amount: ")
if (a+b>c) and (a+c>b) and (b+c>a):
    print("Congratulations! your triangle creation was successful!")
else :
    print("Oops! you can't make a triangle with these numbers. please try again!")
