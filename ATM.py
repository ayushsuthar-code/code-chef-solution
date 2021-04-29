def atm(withdrawl_amount, initial_amount):
    amount=int(withdrawl_amount)
    balance=float(initial_amount)
    return amount
    
withdrawl_amount= int(input("amount to be withdrawl: "))
initial_amount= float(input("initial_amount: "))

if withdrawl_amount%5==0 and initial_amount > (withdrawl_amount + 0.50):
    print (initial_amount - (withdrawl_amount + 0.50))
else:
    print (initial_amount)
