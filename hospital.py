print("Welcome To The Hospital Project\n")


class Hospital:
    def __init__(self, Private, Government, Army, Corona):
        self.Private = Private
        self.Government = Government
        self.Army = Army
        self.Corona = Corona

    def Walk(self):
        return "I am Coming to the Hospital"

    def Gov(self, passport):
        if passport == 'True':
            return "You can enter the Hospital"

        else:
            return "You can't enter the Hospital,please take your COVID-19 passport"

    def Arm(self):
        try:
            references = str(input("If you have any army references, please type TRUE : "))
            assert references == 'TRUE'
            return "You can enter to the Hospital!"
        except:
            return "You don't have any army references. Go to the other Hospitals"

    def Sick(self, temperature):
        if temperature >= 37:
            return "We will come to take you from your home"
        else:
            return "Please approach yourself to our Hospital"