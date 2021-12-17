class Surgery:
    def __init__(self, Room_Num, Total_Client, Doctor_Count):
        self.Room_Num = Room_Num
        self.Total_Client = Total_Client
        self.Doctor_Count = Doctor_Count

    def SurgeryInfo(self):
        return """
                Welcome to Surgery branch!

                Room Number : {}

                Total Number of Clients : {}

                Doctor Count : {}

                """.format(self.Room_Num, self.Total_Client, self.Doctor_Count)


class Robotic:
    def __init__(self, type1):
        self.type1 = type1

    def Surgery1(self):
        return """

                This is the Robotic Surgery.

                """.format(self.type1)


class Oral:
    def __init__(self, type2):
        self.type2 = type2

    def Surgery2(self):
        return """

                This is the Oral Surgery

                """.format(self.type2)
