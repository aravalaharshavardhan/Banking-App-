import datetime
import mysql.connector 
now = datetime.datetime.now()

def setup_database():
    mydb = mysql.connector.connect(
        host="localhost",
        user="harsha",
        password="harsha",
        database="bank_app"
    )
    mycursor = mydb.cursor()
    










class BankAccount:
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance
        self.transactions = []
    
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

print("Main Menu")
print("Press the numbers for the following actions")
print("1. Create new account")
print("2. Deposit amount")
print("3. Withdraw amount")
print("4. View Balance")
print("5. View Statement")
print("6. Quit main menu")

while True:
    choice = int(input())
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
            accounts[index].transactions.append("You have succesfully deposited {} into {}'s account on {}".format(damount,index,now))
            print(f"You have succesfully deposited {damount} into {index}'s account.")
        else:
            print("Enter a valid account name.")
        continue
    
    elif choice ==3:
        wamount = int(input("How much would you like to withdraw?"))
        index = input("Whose account do you want to withdraw from?(Give account name) ")
        if index in accounts:
            accounts[index].withdraw(wamount)
            accounts[index].transactions.append("You have successfully withdrawed {} from {}'s account on {}".format(wamount,index,now))
            print(f"You have successfully withdrawed {wamount} from {index}'s account.")
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
        index = input("Which account statement would you like to see? ")
        if index in accounts:
            for transaction in accounts[index].transactions:
                print (transaction)
        else:
            print("Enter a valid account name.")
        continue
    
    elif choice == 6:
        break


    