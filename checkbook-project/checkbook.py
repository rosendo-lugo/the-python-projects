import os 
import subprocess



checkbook_options = ('1', '2', '3', '4')
def user_choice():
    print("\nWhat would you like to do?\n1) View current balance\n"
  "2) Record a debit (withdraw)\n3) Record a credit (deposit)\n4) Exit\n")
    user = input('Enter a choice: ')
    print('')
    print("Your choice is: ", user)

    while user not in checkbook_options:
        print("Invalid choice: ", user)
        print('')
#         print("What would you like to do?\n1) View current balance\n"
#       "2) Record a debit (withdraw)\n3) Record a credit (deposit)\n4) Exit\n")
        user = input('Enter a choice: ')
#         print('')
        print("\nYour choice is: ", user)
    return user

def view_curt_bal():
    with open('current_balance.txt') as cb:
        current_balance = cb.read()
        print(f'$',current_balance)

def debit():
    with open('current_balance.txt', 'r') as cb:
        current_balance = cb.read()
        current_balance.isdigit()

        current_balance = int(current_balance)

        #this is your current balance
        print('Current Balance')
        print(f'$',int(current_balance))

        user = input('Enter withdraw amount: $')

        while user.isdigit() == False:
            print("Invalid choice: ", user)
            print('')
            user = input('Enter withdraw amount: $')
            print('')
        user = float(user)

        new_balance = current_balance - user

        new_balance = str(new_balance)

        with open('current_balance.txt', 'w') as cb:
            cb.write(new_balance)
        #     print(current_balance)
            print(f'\nNew Balance: $', new_balance)


def credit():
    with open('current_balance.txt', 'r') as cb:
        current_balance = cb.read()
        current_balance.isdigit()

        current_balance = int(current_balance)

        #this is your current balance
        print('Current Balance')
        print(int(current_balance))

        user = input('Enter deposit amount: $')

        while user.isdigit() == False:
            print("Invalid choice: ", user)
            print('')
            user = input('Enter deposit amount: $')
            print('')
        user = int(user)

        new_balance = user + current_balance

        new_balance = str(new_balance)

        with open('current_balance.txt', 'w') as cb:
            cb.write(new_balance)
        #     print(current_balance)
            print(f'\nNew Balance: $', new_balance)


while True:
    user = user_choice()
    if user == '1':
        print("\nCurrent balance")
        view_curt_bal()
    elif user == '2':
        print("Record a credit (deposit)\n")
        debit()
    elif user == '3':
        print("Record a credit (deposit)\n")
        credit()
    elif user == '4':
        print('Thank you, have a great day!')   
        break