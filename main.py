from query_handler import *
from accounts_handler import *
from ui_handler import *
from AES_encryption import *
from Diceware_hash import *

if __name__ == "__main__":
    path= "dice_ware.txt"
    db_name = "exercise_diceware"
    q = QueryHandler("localhost", db_name, "root", "")
    options_menu = ["Add a user", "Is existing user", "Display all accounts", "Exit"]
    p = accountsHandler()
    aec = AESCipher("1")
    
    while True:
        try:
            UIHandler.show_menu(options_menu)
            choice = input("your choice is : ")
            if choice == "1":  # Adding or updating an existing user
                randPass=buildPassword(path)
                p.manage_account(User(input("user name: "), str(aec.encrypt(randPass))), q)
                print(f"your pass is : {randPass}")
            elif choice == "2":  # finding an existing product
                p.isExists_account(input("user name: ") ,(input("password: ")),aec, q)
            elif choice == "3":  # Displaying all existing products
                p.display_all_accounts(q)
            elif choice == "4":  # Exiting the program
                print("Thank you for using our program. Exiting...")
                break
            else:  # If the choice is incorrect, asking for another one
                print(f"Wrong choice. your choice must be between 1 and {len(options_menu)}")
        except BaseException as b:
            print(b)
