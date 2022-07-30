from userClass import *
from query_handler import *
from AES_encryption import *

class accountsHandler:
    @staticmethod
    def manage_account(user: User, query: QueryHandler) -> None:
        """
        Method manages a user by given information.
        If the current user already exists, its information is updated.
        A new account is added if it doesn't exist
        :param user: An object that contains all the necessary information
        :param query: A query to execute
        :return: None
        """
        
        query.execute_non_fetch(
            "INSERT INTO accounts(userName,password) VALUES(%s,%s) ON DUPLICATE KEY UPDATE userName=VALUES(userName),password=VALUES(password)",
            (user.userName, user.password))
        
    

    @staticmethod
    def isExists_account(user_name: str, user_password: str,aec:AESCipher, query: QueryHandler) -> None:
        """
        Method that checks if the user exists by checking the given user and password
        :param user: user An object that contains all the necessary information
        :param query: A query to execute
        :return: None
        """
        users = query.execute_fetch("SELECT userID,userName,password,regDate FROM accounts WHERE userName=%s", (user_name,))
        if not users :
            print("user doesn't exist", end="\n\n")
        else:
            print("\nuser exists :")
            for user in users:
                sqlPass = user['password']
                if user_password == str(aec.decrypt(sqlPass[1:])):
                    print("\tuserName: ",user['userName'],
                    "\n\tuserID: ",user['userID'],
                    "\n\tregDate: ",user['regDate'])
                else:
                    print("\tbut wrong password !!\n")
                print("=========================================")

    @staticmethod
    def display_all_accounts(query: QueryHandler) -> None:
        """
        Method that displays all existing accounts
        :param query: Query to execute
        :return: None
        """
        accounts = query.execute_fetch("SELECT userID,userName,DATE_FORMAT(regDate,%s) as DATE FROM accounts", ('%d/%m/%y',))        
        if not accounts:
            print("No accounts to display", end="\n\n")
        else:
            for account in accounts:  # Going through existing accounts
                print()
                for userID, userName in account.items():
                    # Displaying the objects fields' values
                    print(f"{userID}: {userName}")
                print()