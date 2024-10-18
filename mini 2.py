#ATM
balance=0
def check_balance():
    print("Toatal balance in your account is:",balance)
def deposite(amt):
    global  balance
    balance=balance+amt
    print(amt,"rs.deposited!")
def withdraw(amt):
    global  balance
    if (amt>balance):
        print("Balance is insufficient")
    else:
        balance=balance-amt
        print(amt,"rs.withdraw!")
while True:
    ch=int(input("\n\nEnter choice:\n1.Check balance\t2.Deposit\n3.Withdraw\t4.Exit\n"))
    if ch==1:
        check_balance()
    elif ch==2:
        d_amt=int(input("Enter amount to Deposit:"))
        deposite(d_amt)
    elif ch==3:
        w_amt=int(input("Enter amount to Withdraw:"))
        withdraw(w_amt)
    elif ch==4:
        print("Exiting...")
        break
    else:
        print("Invalid Choice!")
