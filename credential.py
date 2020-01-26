class credential:
    """
    Class that generates new instances of users
    """
    credentials_list  = []

    def __init__(self,credential_name,user_name,password,email):
        self.credential_name = credential_name
        self.user_name = user_name
        self.password = password
        self.email = email

    