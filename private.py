from Hospitals.hospital import Hospital


class PrivateHospital(Hospital):

    def __init__(self, location, RoomCount, ClientCount, DoctorCount):
        self.location = location
        self.RoomCount = RoomCount
        self.ClientCount = ClientCount
        self.DoctorCount = DoctorCount

    def ShowInfo(self):
        return """
            WELCOME TO THE BAKU MEDICAL PLAZA!

            Location : {}

            Total Room Count : {}

            Total Doctor Count : {}

            Total Patient Count : {}

        """.format(self.location, self.RoomCount, self.ClientCount, self.DoctorCount)
