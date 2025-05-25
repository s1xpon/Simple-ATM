users = {
    "4169738872364932": {"pin": "2783", "amount": 3830},
    "4169038528424821": {"pin": "9283", "amount": 8293}
}
administrator = {
    "username": "admin",
    "password": "11235813"
}
cash_banknotes = {
    500: 25,
    200: 10,
    100: 49,
    50: 15,
    20: 76,
    10: 89,
    5: 92,
    1: 154
}
user_logged_in = False
admin_logged_in = False

def atm_user_login():
    global user_logged_in
    global card_number  
    card_number = input("Enter card number: ")
    if card_number in users:
        card_pin = input(f"Enter PIN code for card {card_number}: ")
        if card_pin == users[card_number]["pin"]:
            print("Successfully logged in.")
            user_logged_in = True
        else:
            print("Incorrect PIN!")
    else:
        print("Card number not found.")

def admin_login():
    global admin_logged_in
    admin_user = input("Enter admin username: ")
    
    if admin_user == administrator["username"]:
        admin_pass = input(f"Enter password for {admin_user}: ")
        if admin_pass == administrator["password"]:
            print("Logged in as admin.")
            admin_logged_in = True
        else:
            print("Incorrect password!")
            exit()
    else: 
        print("Incorrect username!")
        exit()

    if admin_logged_in:
        print("1 - Add new user")
        print("2 - View user information")
        print("3 - Delete a user account")
        admin_menu = int(input("Choose one of the options above: "))

        if admin_menu == 1:
            new_user_card = input("Enter new user's card number: ")
            new_user_pin = input("Set a 4-digit PIN for the card: ")

            if len(new_user_card) != 16:
                print("Invalid card number. Operation canceled.")
            elif len(new_user_pin) != 4:
                print("Invalid PIN. Operation canceled.")
            else:
                add_balance = int(input("Do you want to add balance? (1-Yes, 2-No): "))
                if add_balance == 1:
                    new_amount = int(input("How much do you want to add?: "))
                    if new_amount <= 0:
                        print("Invalid amount entered.")
                        print("Default balance will be set to 0.")
                        users.update({
                            new_user_card: {"pin": new_user_pin, "amount": 0}
                        })
                    else:
                        users.update({
                            new_user_card: {"pin": new_user_pin, "amount": new_amount}
                        })
                else:
                    users.update({
                        new_user_card: {"pin": new_user_pin, "amount": 0}
                    })
                print("New user added successfully!")
                print(users[new_user_card])

        elif admin_menu == 2:
            print(users.items())

        elif admin_menu == 3:
            delete_user = input("Enter the card number of the user to delete: ")
            if delete_user in users:
                del users[delete_user]
                print("User deleted successfully!")
            else:
                print("User not found!")
                exit()
        else:
            print("Enter a valid option!")

select_login = int(input("Who do you want to login as? 1 - Admin, 2 - User: "))
if select_login == 1:
    print("Logging in as admin...")
    admin_login()
elif select_login == 2:
    print("Logging in as user...")
    atm_user_login()
else:
    print("Please enter a valid choice!")
    exit()

if user_logged_in:
    print("1 - Add money to card")
    print("2 - Withdraw money from card")
    print("3 - Check card balance")
    print("4 - Cancel operation")
    selection = int(input("Which operation do you want to perform?: "))

    if selection == 1:
        enter_amount = int(input("How much money do you want to add?: "))
        if enter_amount <= 0:
            print("Enter an amount greater than 0!")
        else:
            users[card_number]["amount"] += enter_amount
            print("Money added to your account.")
            print(f"Current balance: {users[card_number]['amount']} USD")

    elif selection == 2:
        requested_amount = int(input("Enter amount to withdraw: "))
        if requested_amount > users[card_number]["amount"]:
            print("Insufficient balance!")
        elif requested_amount <= 0:
            print("Enter a valid amount!")
        else:
            remaining_amount = requested_amount
            cash_to_give = {}
            for cash in sorted(cash_banknotes.keys(), reverse=True):
                needed = remaining_amount // cash
                available = min(needed, cash_banknotes[cash])
                if available > 0:
                    cash_to_give[cash] = available
                    remaining_amount -= cash * available
            if remaining_amount == 0:
                print("Cash dispensed successfully:")
                users[card_number]["amount"] -= requested_amount
                for cash, count in cash_to_give.items():
                    print(f"{cash} USD - {count} pieces")
            else:
                print("ATM does not have the appropriate denominations!")

    elif selection == 3:
        print(f"Balance: {users[card_number]['amount']} USD")

    elif selection == 4:
        print("Operation cancelled.")
        exit()
    else:
        print("Enter a valid selection!")