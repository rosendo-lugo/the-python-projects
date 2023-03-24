# Checkbook options.
# 1) View current balance
# 2) Record a debit (withdraw)
# 3) Record a credit (deposit)
# 4) Exit
checkbook_options = ('1', '2', '3', '4')


def main():
    options()

    # User account options.
    def user_choice():

        print("What would you like to do?\n1) View current balance\n"
        "2) Record a debit (withdraw)\n3) Record a credit (deposit)\n4) Exit\n")

        user = None
        while user in checkbook_options:
            user = int(input('Enter a choice: '))
        return user
    
    # Find the correct choice
    def options():
        money = True
        while money:
            user = user_choice()
            if user != checkbook_options:
                print("Your choice is: ", user)
                print("Invalid choice: ", user)
            if user == '1':
                print("View current balance\n")
                break
            elif user == '2':
                print("Record a debit (withdraw)\n")
                break
            elif user == '3':
                print("Record a credit (deposit)\n")
                break
            elif user == '4':
                print("Exit\n")
                break
        return money
    
    main()