class BankAccount:
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance
    
    def deposit(self,amount):
        if amount >=0:
            self.balance += amount
        else:
            print("Please enter a valid number")

    def withdraw(self,amount):
        if self.balance>0 and self.balance >=amount:
            self.balance-=amount
        else:
            print("The requested funds are not available.")
    
    def get_balance(self):
        print(self.balance) 



        
while True:
    choice = int(input("Enter 1 for a new account, 2 for depositing, 3 for withdrawing, 4 for getting balance, 5 to quit menu"))
    if choice == 1:
        name = input("Please enter account name:")
        name_acc = BankAccount(name, 0)
        continue
    
    elif choice == 2:
        damount = int(input("How much would you like to deposit?"))
        name_acc.deposit(damount)
        continue
    
    elif choice ==3:
        wamount = int(input("How much would you like to withdraw?"))
        name_acc.withdraw(wamount)
        continue
    
    elif choice == 4:
        name_acc.get_balance()
        continue
    
    elif choice == 5:
        break


    