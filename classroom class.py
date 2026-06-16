"""
class classroom:
    def __init__ (self, name, year, course ):
        self.name= input("Name")
        self.year= int(input("joining yr ="))
        self.course= input("course =")
    def greet(self):
        print(f"Hello i'm {self.name}, joining yr {self.year},doing {self.course}")
    def shekhar(self):
        print(f"Hello i'm {self.name}, joining yr {self.year},doing {self.course}")
    def shiv(self):
        print(f"Hello i'm {self.name}, joining yr {self.year},doing {self.course}")
    def nilu(self):
        print(f"Hello i'm {self.name}, joining yr {self.year},doing {self.course}")
    def khan(self):
        print(f"Hello i'm {self.name}, joining yr {self.year},doing {self.course}")


p1=classroom ( name= any, year= any, course= any)
p1.greet()
p1=classroom ( name= any, year= any, course= any)
p1.shekhar()
p1=classroom ( name= any, year= any, course= any)
p1.shiv()
p1=classroom ( name= any, year= any, course= any)
p1.nilu()
p1=classroom ( name= any, year= any, course= any)
p1.khan()

p1=classroom("Chander", 2026, "python")
p1.greet()
p2=classroom ( name=any, year =any, course=any)
p2.shekhar()
p2=classroom ( name=any, year =any, course=any)
p2.shekhar()
p2=classroom ( name=any, year =any, course=any)
p2.shekhar()
"""

#10. Make a railway reservation menu using class case including
#1. Journey from-to 2. DAte of journey 3. quota (Gen/spec abled / sen citi) 4. class - SL/AC/gen 5. Passenger details (Name:Age:gender)
#6. Birth - Lower/middle/ upper/ Side lower/ side upper

class RailwayReservation:
    def __init__(self, from_location, to_location, date_of_journey, quota, travel_class, passenger_details, berth_preference):
        self.from_location = from_location
        self.to_location = to_location
        self.date_of_journey = date_of_journey
        self.quota = quota
        self.travel_class = travel_class
        self.passenger_details = passenger_details
        self.berth_preference = berth_preference

    def display_reservation(self):
        print(f"Journey: {self.from_location} to {self.to_location}")
        print(f"Date of Journey: {self.date_of_journey}")
        print(f"Quota: {self.quota}")
        print(f"Class: {self.travel_class}")
        print(f"Passenger Details: {self.passenger_details}")
        print(f"Berth Preference: {self.berth_preference}")
from_location = input("Enter journey from: ")
to_location = input("Enter journey to: ")
date_of_journey = input("Enter date of journey (DD/MM/YYYY): ")
quota = input("Enter quota (Gen/spec abled / sen citi): ")
travel_class = input("Enter class (SL/AC/gen): ")
name = input("Enter passenger name: ")
age = int(input("Enter passenger age: "))
gender = input("Enter passenger gender: ")
passenger_details = f"Name: {name}, Age: {age}, Gender: {gender}"
berth_preference = input("Enter berth preference (Lower/middle/ upper/ Side lower/ side upper): ") 
reservation = RailwayReservation(from_location, to_location, date_of_journey, quota, travel_class, passenger_details, berth_preference)
reservation.display_reservation()
