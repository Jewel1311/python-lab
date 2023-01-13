from random import randint

class Bank:
    def __init__(self, acc_no, name, acc_type ):
        self.acc_no = acc_no
        self.name = name
        self.acc_type = acc_type
        self.balance = 0
    
    def display(self):
        print("***************************")
        print("Name : ", name)
        print("Account no : ", acc_no)
        print("Account type : ", acc_type)
        print("***************************")
    

    def view_balance(self):
        print("Balance = ", self.balance)

    def deposit(self):
        amt = int(input("Enter the amount to deposit : "))
        self.balance += amt
        self.view_balance()

    def withdraw(self):
        amt = int(input("Enter the amount to withdraw : "))
        if amt > self.balance:
            print("\nInsufficient balance")
            return

        self.balance -= amt
        print("\nRs ", amt, "withdrawn" )
        self.view_balance()

name = input("Enter the name : ")
acc_no = randint(11111, 99999)
acc_type = input("Enter the account type : ")

ob1 = Bank(acc_no, name, acc_type)
ob1.display()

while True:
    print("---------------------\n")
    print("1.Deposit\n2.Withdraw\n3.Exit")
    c = int(input("Enter choice : "))

    if c == 1:
        ob1.deposit()
    elif c == 2: 
        ob1.withdraw()
    elif c == 3:
        break
    else:
        print("Invalid Choice")
        
    