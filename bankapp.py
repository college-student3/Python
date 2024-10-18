print("Central Bank Of India")
balance=0
def check_balance():
    print("Total balance of your account is:",balance)
def deposit_cash(amt):
    global balance
    balance=balance+amt
    print(amt,"Rs. Deposited!")
def withdraw_cash(amt):
    global balance
    balance=balance-amt
    if(amt>check_balance):
        print("balance is insufficent")
    else:
        print(amt,"Rs Withdrawn!")
while True:
    ch=int(input("\nEnter any choice:\n1.Deposited cash\n2.Withdrawn cash\n3.check balance\n"))
    match ch:
        case 1:
            d_amt=int(input("Enter amount to deposit:"))
            deposit_cash(d_amt)
        case 2:
            w_amt=int(input("Enter amount to withdraw:"))
            withdraw_cash(w_amt)
        case 3:
            check_balance()
        case _:
            print("Default Excuted")
            

        

