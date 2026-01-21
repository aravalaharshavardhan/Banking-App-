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

accounts = {}

        
while True:
    choice = int(input("Enter 1 for a new account, 2 for depositing, 3 for withdrawing, 4 for getting balance, 5 to quit menu"))
    if choice == 1:
        name = input("Please enter account name:")
        i_amount = int(input("Enter starting balance:"))
        name_acc = BankAccount(name,i_amount)
        accounts[name] = name_acc
        continue
    
    elif choice == 2:
        index = input("Whose account do you want to deposit in?(Give account name) ")
        if index in accounts:
            damount = int(input("How much would you like to deposit?"))
            accounts[index].deposit(damount)
        else:
            print("Enter a valid account name.")
        continue
    
    elif choice ==3:
        wamount = int(input("How much would you like to withdraw?"))
        index = input("Whose account do you want to withdraw from?(Give account name) ")
        if index in accounts:
            accounts[index].withdraw(wamount)
        else:
            print("Enter a valid account name.")
        continue
    
    elif choice == 4:
        index = input("Which account balance would you like to see? ")
        if index in accounts:
            accounts[index].get_balance()
        else:
            print("Enter a valid account name.")
        continue
    
    elif choice == 5:
        break


    