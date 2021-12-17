import charachter
import ophthalmology
import pediatrics
import army
import corona
import private
import government
import client
import cardiology
import oncology
import physiotherapy
import gynecology
import burncenter
import diabetes
import orthopedics
import pathology
import surgery
import rehabilitation
import transfusion
import traumatology
import urology
import stomatology
import ClientMoney
import neonatology

print("Please choose that who you are, Doctor or Client,if you are doctor, please type 1.")
person = charachter.Person()
doctor = charachter.Doctor()
Input4 = int(input("Select Doctor or Person: "))
if Input4 == 1:
    print(doctor.char())
else:
    print(person.char())

print("-------------------------------------------------------------------------------")

Sinan = client.Client()
Sinan.register("SananM", "123!", "smuzefferov1@gmail.com", "0503961514")
Sinan.login("SananM", "123!")
Private = private.PrivateHospital("Baku", 120, 30, 10)
Government = government.GovernmentHospital("Baku", 200, 50, 90)
Army = army.ArmyHospital("Baku", 30, 20, 30)
Corona = corona.CoronaHospital("Baku", 1500, 1000, 200)
print("""
   Choose Hospital where you wanna go!
   
   Baku Private Hospital - 1
   Baku Government Hospital - 2
   Army Hospital - 3
   New Corona Hospital - 4
""")

Input = int(input("Select Hospital: "))
if Input == 1:
    print(Private.ShowInfo())
    print(Private.Walk())
elif Input == 2:
    print(Government.ShowInfo())
    print(Government.Gov(input("Hello Please When you come to our Hospital, take your COVID-19 Passport.If you have "
                               "Passport,type True:")))
elif Input == 3:
    print(Army.ShowInfo())
    print(Army.Arm())
elif Input == 4:
    print(Corona.ShowInfo())
    print(Corona.Sick(int(input("Write your instant Temperature:"))))

print("-------------------------------------------------------------------------------")

c = cardiology.Cardiology(1, 10, 3)
o = oncology.Oncology(10, 5, 1)
p = physiotherapy.Physiotherapy(22, 10, 5)
g = gynecology.Gynecology(5, 2, 2)
b = burncenter.BurnCenter(13, 10, 5)
d = diabetes.Diabetes(20, 20, 1)
ort = orthopedics.Orthopedics(54, 4, 2)
path = pathology.Pathology(31, 4, 3)
s = surgery.Surgery(100, 1, 10)
r = rehabilitation.Rehabilitation(45, 20, 10)
u = urology.Urology(67, 3, 4)
sto = stomatology.Stomatology(23, 1, 2)
sur1 = surgery.Oral("Type of Oral")
sur2 = surgery.Robotic("Type of Robotic")
sto1 = stomatology.Dental("Dental Stomatology option")
sto2 = stomatology.Briquettes("Briquettes Stomatology option")

print("""
Select the Branch which you want:

Cardiology branch - 1
Oncology branch - 2
Physiotherapy branch - 3
Gynecology branch - 4
Burn Branch - 5
Diabetes Branch - 6
Orthopedics Branch - 7
Pathology Branch - 8
Surgery Branch - 9
Rehabilitation Branch - 10
Urology Branch - 11
Stomatology Branch - 12
""")

Input1 = int(input("Select branch: "))
if Input1 == 1:
    print(c.CardiologyInfo())
elif Input1 == 2:
    print(o.OncologyInfo())
elif Input1 == 3:
    print(p.PhysiotherapyInfo())
elif Input1 == 4:
    print(g.GynecologyInfo())
elif Input1 == 5:
    print(b.BurnInfo())
elif Input1 == 6:
    print(d.DiabetesInfo())
elif Input1 == 7:
    print(ort.OrthopedicsInfo())
elif Input1 == 8:
    print(path.PathologyInfo())
elif Input1 == 9:
    print(s.SurgeryInfo())
    input2 = int(input("Choose the type of Surgery,for Oral Surgery type 1, for Robotic surgery type 2: "))
    if input2 == 1:
        print(sur1.Surgery2())
    elif input2 == 2:
        print(sur2.Surgery1())
elif Input1 == 10:
    print(r.RehabInfo())
elif Input1 == 11:
    print(u.UrologyInfo())
elif Input1 == 12:
    print(sto.StomatologyInfo())
    input5 = int(input("Choose option for Stomatology service,for Dental Services type 1, for Briquettes service "
                       "type 2: "))
    if input5 == 1:
        print(sto1.Operation1())
    elif input5 == 2:
        print(sto2.Operation2())

print("""
Look at your Pocket for money.If you don't have enough money, you can't use our Branches and Hospital Services! Our
Services' price begin 100$
""")

Input3 = int(input("Enter Your Money : "))
print(ClientMoney.Clientmoney(Input3).get_your_money())
print(ClientMoney.Clientmoney(Input3).set_your_money())
print(ClientMoney.Clientmoney(Input3).giveCampaign())
if Input3 >= 100:
    tr = transfusion.Transfusion(101, 0, 2)
    tra = traumatology.Traumatology(102, 1, 1)
    oph = ophthalmology.Ophthalmology(202, 0, 3)
    pe = pediatrics.Pediatrics(99, 2, 4)
    neo = neonatology.Neonatology(103, 1, 5)

    print("""
Select the extra Branch for our Campaign. This one is will be free:

Transfusion branch - 1
Traumatology branch - 2
Ophthalmology branch - 3
Pediatrics branch - 4
Neonatology branch - 5

""")

    Input7 = int(input("Select the extra branch for our campaign :"))
    if Input7 == 1:
        print(tr.TransfusionInfo())
    elif Input7 == 2:
        print(tra.TraumaInfo())
    elif Input7 == 3:
        print(oph.OphthInfo())
    elif Input7 == 4:
        print(pe.PediatricsInfo())
    elif Input7 == 5:
        print(neo.NeoInfo())
else:
    print("You can't use our Hospital's Campaign!")
