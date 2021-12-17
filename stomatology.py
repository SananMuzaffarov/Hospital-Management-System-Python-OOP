class Stomatology:
    def __init__(self, Room_Num, Total_Client, Doctor_Count):
        self.Room_Num = Room_Num
        self.Total_Client = Total_Client
        self.Doctor_Count = Doctor_Count

    def StomatologyInfo(self):
        return """
                Welcome to Stomatology branch!

                Room Number : {}

                Total Number of Clients : {}

                Doctor Count : {}

                """.format(self.Room_Num, self.Total_Client, self.Doctor_Count)


class Dental:
    def __init__(self, option1):
        self.option1 = option1

    def Operation1(self):
        return """

                This service is for who comes for teeth pain or something else.

                """.format(self.option1)


class Briquettes:
    def __init__(self, option2):
        self.option2 = option2

    def Operation2(self):
        return """

                This service is for who wants to Briquettes for their teeth

                """.format(self.option2)
