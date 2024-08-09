import datetime
import os

password = '1234'
account = '0826539274'
balance = 0


input_password = input('Enter your password: ')
input_account = input('Enter your account number: ')

if input_account == account and input_password == password:
    print('Login Successfully')

    while True:
        choice = input("Enter 'd for deposit\n'w for withdrawal\n'b' to check balance\n't' for transaction history\n'q' to quit:\n")

        if choice == 'd':
            amount = float(input('Enter the amount to deposit: '))
            balance = balance + amount
            timestamp = datetime.datetime.now()
            with open("transaction.txt", 'a') as file:
                file.writelines(f"Deposited {amount} at {timestamp}\n")
                print(f"Deposited {amount} succesfully")




        elif choice == 'w':
            amount = float(input('Enter the amount to withdraw: '))
            if amount > balance:
                print('Insufficiant funds')
            else:
                balance = balance - amount
                timestamp = datetime.datetime.now()
                with open('transaction.txt', 'a') as file:
                    file.writelines(f"Withdrew {amount} at {timestamp}. New Balance is {balance}\n")
                print(f"Withdrew {amount} successfully")
                
                
        elif choice == 'b':
            print(f"Account Balance: {balance}")




        elif choice == 't':
            if os.path.exists("C:/Users/Gabriel/Documents/Daniel/transaction.txt"):
                with open("C:/Users/Gabriel/Documents/Daniel/transaction.txt", 'r') as file:
                    content = file.readlines()
                    print(content)
            else:
                print(f"The file does not exist because you havent made any transaction yet")
        elif choice == 'q':
            print('Quitting the program')
            break 

        else:
            print('Invalid choice. Please try again')
else:
    print('Invalid account number or password')



