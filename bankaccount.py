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

John_acc = BankAccount("John",10000)
John_acc.deposit(5000)
John_acc.withdraw(3000)
John_acc.get_balance()

Bob_acc = BankAccount("Bob",5000)

Bob_acc.withdraw(5000)
Bob_acc.get_balance()
Bob_acc.withdraw(500)

            
while True:
    choice = input()
    if choice == 1:
        name = input("Please enter account name:")
        name_acc = BankAccount(name, 0)
    
    elif choice == 2:
        

    