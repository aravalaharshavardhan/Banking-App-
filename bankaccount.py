import datetime
import mysql.connector 
from config import DB_CONFIG
now = datetime.datetime.now()

def setup_database():
    mydb = mysql.connector.connect(**DB_CONFIG)
    mycursor = mydb.cursor()

    accounts_table = """CREATE TABLE IF NOT EXISTS accounts(
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    balance DECIMAL(10,2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP);"""

    mycursor.execute(accounts_table)

    transactions_table = """CREATE TABLE IF NOT EXISTS transactions(
    id INT AUTO_INCREMENT PRIMARY KEY,
    account_id INT,
    type VARCHAR(20),
    amount DECIMAL(10,2),
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    description VARCHAR(255),
    FOREIGN KEY(account_id) REFERENCES accounts(id));"""

    mycursor.execute(transactions_table)
    mydb.commit()
    mycursor.close()
    mydb.close()

    print("Tables created successfully.")

setup_database()

def create_account(name, initial_balance):
    mydb = mysql.connector.connect(**DB_CONFIG)
    mycursor = mydb.cursor()
    insert_acc = "INSERT INTO accounts(name,balance) VALUES(%s,%s)"
    values = (name, initial_balance)
    mycursor.execute(insert_acc,values)
    new_id = mycursor.lastrowid
    mydb.commit()
    mycursor.close()
    mydb.close()

    return new_id
account_id = create_account("Harsha",1000)
print(account_id)

                    
def get_account_balance(account_id):
    mydb = mysql.connector.connect(**DB_CONFIG)
    mycursor = mydb.cursor()
    balance_return = "SELECT balance FROM accounts WHERE ID = %s"
    value = (account_id,)
    mycursor.execute(balance_return,value)
    result = mycursor.fetchone()
    mycursor.close()
    mydb.close()
    if result is not None:
        return result[0]
    else:
        return None
    
    







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


    