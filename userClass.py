
class User:
    def __init__(self,userName:str,userPassword:str) -> None:
        """
        """
        self.userName = userName
        self.password = userPassword
    # GETTERS
    @property
    def userName(self):
        """
        Setter returns the user usrName
        :return: user usrName
        """
        return self.__userName
    
    @property
    def password(self):
        """
        Setter returns the user password
        :return: user password
        """
        return self.__password 
    
    # SETTERS
    @userName.setter
    def userName(self, userName: str):
        """
        Setter sets user userName
        :param userName: A value to set the userName
        :return: None
        """
        if not isinstance(userName,str):
            raise ValueError("user userName must be String")

        self.__userName = userName
        
    @password.setter
    def password(self, password: str):
        """
        Setter sets user password
        :param password: A value to set the password
        :return: None
        """
        if not isinstance(password,str):
            raise ValueError("user password must be String")

        self.__password = password
        
    def __str__(self) -> str:
        """
        Method returns a string that displays the user attributes value in the specific format
        :return:
        """
        return f"""user info:
        name: {self.userName}
                """