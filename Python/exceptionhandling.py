while True:
    try:
        x=int(input("enter a number"))
        y=20/x
        print(y)
        break
    except ValueError:
        print("only integers are allowed")
    except ArithmeticError:
        print("not allowed")
        
