op = input("Please choose a symbol: (+,-,*,/): ")
a =int (input("enter the first number: "))
b =int (input("enter the second number: "))
if op == ("+"):
    print(a+b)
if op == ("-"):
    print(a-b)
if op == ("*"):
    print(a*b)
if op == ("/"):
    if b== 0:
        print("Error")
    else:
        print(a/b)
