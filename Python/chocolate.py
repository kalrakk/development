money=int(input("enter the money"))
amount=int(input("enter the price per choc"))
n=int(money/amount)
def wrapper_choc(n) :
    if(n<3) :
        return 0
    elif(n<5) :
        wrap_choc=int(n/3)
        return wrap_choc+wrapper_choc(wrap_choc)
    else :
        wrap_choc=int(n/5)*2
        return wrap_choc+wrapper_choc(wrap_choc+n%5)
print("total chocolates",n+wrapper_choc(n))
        
        
