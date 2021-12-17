class Client:

    def __init__(self, username=None, password=None, email=None, phone_number=None):
        self.username = username
        self.password = password
        self.email = email
        self.phone_number = phone_number

    def login(self, entered_username, entered_password):
        if entered_username == self.username and entered_password == self.password:
            print("Logged in successfully for : \n", self.username)

        else:
            print("Username or password is incorrect")

    def register(self, username, password, email, phone_number):
        if username and password and email and phone_number:
            print("Registration successful for user : \n", username)
            self.username = username
            self.password = password
            self.email = email
            self.phone_number = phone_number
        else:
            print("Unsuccessful")
