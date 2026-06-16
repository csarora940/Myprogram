#5. WAP Create a robot direction controller (left/right/up/down)
"""
class Robot:
    def __init__(self):
        self.direction = "up"

    def turn_left(self):
        if self.direction == "up":
            self.direction = "left"
        elif self.direction == "left":
            self.direction = "down"
        elif self.direction == "down":
            self.direction = "right"
        elif self.direction == "right":
            self.direction = "up"

    def turn_right(self):
        if self.direction == "up":
            self.direction = "right"
        elif self.direction == "right":
            self.direction = "down"
        elif self.direction == "down":
            self.direction = "left"
        elif self.direction == "left":
            self.direction = "up"

    def move_forward(self):
        print(f"Moving forward in direction: {self.direction}")
# Example usage
robot = Robot()
robot.move_forward()  # Moving forward in direction: up
robot.turn_right()
robot.move_forward()  # Moving forward in direction: right
robot.turn_left()
robot.move_forward()  # Moving forward in direction: up
robot.turn_left()
robot.move_forward()  # Moving forward in direction: left
robot.turn_left()
robot.move_forward()  # Moving forward in direction: down
robot.turn_right()
robot.move_forward()  # Moving forward in direction: left
"""

#6. WAP Make a season checker from month number using switch case statement
"""
month= int(input("Enter month number (1-12): "))
match month:
    case 12 | 1 | 2:
        print("It's Winter")
    case 3 | 4 | 5:
        print("It's Spring")
    case 6 | 7 | 8:
        print("It's Summer")
    case 9 | 10 | 11:
        print("It's Fall") 
    case _:
        print("Invalid month number")"""

#6. WAP Make a season checker from month number using switch case statement using if-else statement
"""
month = int(input("Enter month number (1-12): "))
if month in [12, 1, 2]:
    print("It's Winter")
elif month in [3, 4, 5]:
    print("It's Spring")
elif month in [6, 7, 8]:
    print("It's Summer")
elif month in [9, 10, 11]:
    print("It's Fall")
else:
    print("Invalid month number")"""
    
#WAP Create a bank transaction menu using match case statement: 1. Credit money 2.Debit money 3. Check balance 4. Mini statement 5.Exit
"""
balance = 1000
mini_statement = []
while True:
    print("\nBank Transaction Menu:")
    print("1. Credit money")
    print("2. Debit money")
    print("3. Check balance")
    print("4. Mini statement")
    print("5. Exit")
    
    choice = int(input("Enter your choice (1-5): "))
    
    match choice:
        case 1:
            amount = float(input("Enter amount to credit: "))
            balance += amount
            mini_statement.append(f"Credited: {amount}")
            print(f"Amount credited successfully. New balance: {balance}")
        case 2:
            amount = float(input("Enter amount to debit: "))
            if amount > balance:
                print("Insufficient funds.")
            else:
                balance -= amount
                mini_statement.append(f"Debited: {amount}")
                print(f"Amount debited successfully. New balance: {balance}")
        case 3:
            print(f"Current balance: {balance}")
        case 4:
            print("Mini Statement:")
            for transaction in mini_statement:
                print(transaction)
        case 5:
            print("Exiting the program. Thank you for banking with us!")
            break
        case _:
            print("Invalid choice. Please enter a number between 1 and 5.")
            """

#WAP Make a command-based chatbot using Match/switch case statement:
"""
chatbot_responses = {
    "hello": "Hi there! How can I assist you today?",
    "how are you": "I'm doing well, thank you for asking!",
    "what is your name": "I'm a Chandu champion chatbot.",
    "bye": "Goodbye! Have a great day!"
}
while True:    
    user_input = input("You: ").lower()
    if user_input in chatbot_responses:
        print(f"Chatbot: {chatbot_responses[user_input]}")
        if user_input == "bye":
            break
"""

#WAP Make a command-based chatbot using functions and if-else statements:
"""
def chatbot_response (user_input):
    user_input = input("Enter command: ").lower()
    if user_input == "hello":
        return "Hi there! How can I assist you today?"
    elif user_input == "how are you":
        return "I'm doing well, thank you for asking!"
    elif user_input == "what is your name":
        return "I'm a Chandu champion chatbot."
    elif user_input == "bye":
        return "Goodbye! Have a great day!"
    else:
        return "Sorry, I don't understand that command. Please try again."
user=chatbot_response("hello")
print(f"Chatbot: {user}")
user=chatbot_response("how are you")
print(f"Chatbot: {user}")
user=chatbot_response("what is your name")
print(f"Chatbot: {user}")
user=chatbot_response("bye")
print(f"Chatbot: {user}")
"""
#using while loop to keep the chatbot running until the user says "bye":
"""
while True:
    user_input = input("You: ")
    response = chatbot_response(user_input)
    print(f"Chatbot: {response}")
    if user_input.lower() == "bye":
        break
"""
#9. WAP Create a marksheet grading system using match/switch case statement:
"""
Marks = int(input("Enter marks (0-100): "))
match Marks:
    case Marks if Marks >= 90:
        print("Grade: A")
    case Marks if Marks >= 80:
        print("Grade: B")
    case Marks if Marks >= 70:
        print("Grade: C")
    case Marks if Marks >= 60:
        print("Grade: D")
    case Marks if Marks >= 0:
        print("Grade: F")
    case _:
        print("Invalid marks. Please enter a number between 0 and 100.")
        """

#10. Make a railway reservation menu using match case including
#1. Journey from-to 2. DAte of journey 3. quota (Gen/spec abled / sen citi) 4. class - SL/AC/gen 5. Passenger details (Name:Age:gender)
#6. Birth - Lower/middle/ upper/ Side lower/ side upper
"""
From=input("Enter journey from: ")
To=input("Enter journey to: ")
Date=input("Enter date of journey (DD/MM/YYYY): ")
Quota=input("Enter quota (Gen/spec abled / sen citi): ")
Class=input("Enter class (SL/AC/gen): ")
Name=input("Enter passenger name: ")
Age=int(input("Enter passenger age: "))
birth=input("Enter birth preference (Lower/middle/ upper/ Side lower/ side upper): ")
print("\nRailway Reservation Details:")
print(f"Journey: {From} to {To}")
print(f"Date of Journey: {Date}")
print(f"Quota: {Quota}")
print(f"Class: {Class}")
print(f"Passenger Name: {Name}")
print(f"Passenger Age: {Age}")
print(f"Birth Preference: {birth}")
"""
