from Hospitals.hospital import Hospital


class GovernmentHospital(Hospital):

    def __init__(self, Location, RoomCount, ClientCount, DoctorCount):
        self.Location = Location
        self.RoomCount = RoomCount
        self.ClientCount = ClientCount
        self.DoctorCount = DoctorCount

    def ShowInfo(self):
        return """
            WELCOME TO THE BAKU GOVERNMENT HOSPITAL!

            Location : {}

            Total Room Count : {}

            Total Doctor Count : {}

            Total Patient Count : {}

            """.format(self.Location, self.RoomCount, self.ClientCount, self.DoctorCount)
