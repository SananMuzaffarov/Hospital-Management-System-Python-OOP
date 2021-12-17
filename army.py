import Hospital


class ArmyHospital(Hospital):

    def __init__(self, Location, RoomCount, ClientCount, DoctorCount):
        self.Location = Location
        self.RoomCount = RoomCount
        self.ClientCount = ClientCount
        self.DoctorCount = DoctorCount

    def ShowInfo(self):
        return """
            WELCOME TO THE ARMY HOSPITAL!

            Location : {}

            Total Room Count : {}

            Total Doctor Count : {}

            Total Patient Count : {}

            """.format(self.Location, self.RoomCount, self.ClientCount, self.DoctorCount)
