import datetime
import mysql.connector 
from realconfig import DB_CONFIG
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
    
def update_account_balance(account_id,new_balance):
     
     mydb = mysql.connector.connect(**DB_CONFIG)
     mycursor = mydb.cursor()
     sql = "UPDATE accounts SET balance = %s WHERE id = %s"
     value = (new_balance,account_id)
     mycursor.execute(sql,value)
     mydb.commit()
     mycursor.close()
     mydb.close()


def account_exists(account_id):

    mydb = mysql.connector.connect(**DB_CONFIG)
    mycursor = mydb.cursor()
    sql = "SELECT COUNT(*) FROM accounts WHERE id = %s"
    value = (account_id,)
    mycursor.execute(sql,value)
    result =mycursor.fetchone()
    count = result[0]
    mycursor.close()
    mydb.close()
    if count == 1:
        return True
    else:
        return False
    
def log_transaction(account_id,trans_type,amount,description):

    mydb = mysql.connector.connect(**DB_CONFIG)
    mycursor = mydb.cursor()
    sql = "INSERT INTO transactions(account_id,type,amount,description) VALUES(%s,%s,%s,%s)"
    params = (account_id,trans_type,amount,description)
    mycursor.execute(sql,params) 
    mydb.commit()
    mycursor.close()
    mydb.close()

def get_account_statement(account_id):
    mydb = mysql.connector.connect(**DB_CONFIG)
    mycursor = mydb.cursor()
    sql = "SELECT * FROM transactions WHERE account_id = %s ORDER BY timestamp DESC"
    value = (account_id,)
    mycursor.execute(sql,value)
    result = mycursor.fetchall()
    mycursor.close()
    mydb.close()
    return result







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
        new_id = create_account(name,i_amount)
        print(f"Your account has been sucessfully created. Your account ID is {new_id}.")
        continue
    
    elif choice == 2:
        index = input("Whose account do you want to deposit in?(Give account ID) ")
        if account_exists(index):
            damount = int(input("How much would you like to deposit?"))
            if damount > 0:
                new_amount = get_account_balance(index) + damount
                update_account_balance(index,new_amount)
                log_transaction(index,"DEPOSIT",damount,f"Deposited ₹{damount}. ")
                print(f"You have succesfully deposited {damount} into {index}'s account.")
        else:
            print("Enter a valid account name.")
        continue
    
    elif choice ==3:
        wamount = int(input("How much would you like to withdraw?"))
        index = input("Whose account do you want to withdraw from?(Give account ID) ")
        if account_exists(index):
            if wamount <= get_account_balance(index):
                newamount = get_account_balance(index) - wamount
                update_account_balance(index,newamount)
                log_transaction(index,"WITHDRAW",wamount,f"Withdrawed ₹{wamount}.")
                print(f"You have successfully withdrawed {wamount} from {index}'s account.")
        else:
            print("Enter a valid account name.")
        continue
    
    elif choice == 4:
        index = input("Which account balance would you like to see? ")
        if account_exists(index):
            get_account_balance(index)
        else:
            print("Enter a valid account name.")
        continue
    
    elif choice == 5:
        index = input("Which account statement would you like to see? ")
        if account_exists(index):
            transactions = get_account_statement(index)
            for transaction in transactions:
                print(f"{transaction[5]};Type:{transaction[2]},Timestamp:{transaction[4]}")
        else:
            print("Enter a valid account name.")
        continue
    
    elif choice == 6:
        break


    