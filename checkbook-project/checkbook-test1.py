
import os 
import subprocess


checkbook_options = ('1', '2', '3', '4')

def main():
    options()
    
def user_choice():
    print("What would you like to do?\n1) View current balance\n"
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

def options():
    opt = True
    while opt:
        user = user_choice()
        if user == '1':
            print("\nCurrent balance\n")
            return view_curt_bal()
        elif user == '2':
            print("Record a debit (withdraw)\n")
            break
        elif user == '3':
            print("Record a credit (deposit)\n")
            break
        elif user == '4':
            print("Exit\n")
            break
    return opt

def view_curt_bal():
    with open('current_balance.txt') as cb:
        current_balance = cb.read()
        print(current_balance)
        return user_choice()
    