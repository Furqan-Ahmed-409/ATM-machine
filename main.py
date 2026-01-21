print("Welcome to the ATM machine")
correct_pin=int(12345)
attempts_limit=3
balance=0
def deposit(amount):
    global balance
    balance+=amount
    print(f"Deposited: {amount}. New balance: {balance}")
def withdraw(amount):
    global balance
    if amount>balance:
        print("Insufficient funds")
    else:
        balance-=amount
        print(f"Withdraw: {amount}. New balance: {balance}")
def checkbalance():
    print(f"You have {balance} in your account")
for attempt in range(attempts_limit):
    entered_pin=int(input("Please enter your PIN: "))
    if entered_pin==correct_pin:
        print("Welcome to your account")
        while True:
            function=str(input("Type deposit for deposit: \nType withdraw for withdraw: \nType checkbalance to withdraw balance: \n").lower())
            if function=="deposit":
                amount=int(input("Enter amount: "))
                deposit(amount)
            elif function=="withdraw":
                amount=int(input("Enter amount: "))
                withdraw(amount)
            elif function=="checkbalance":
                checkbalance()
            else:
                print("Incorrect option")
    else:
        print(f"Incorrect PIN, {attempts_limit-(attempt+1)} attempts left")
else:
    print("Too many attempts. please enter your PIN")
