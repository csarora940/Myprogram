#WAP Make a command-based chatbot using Functions

def chatbot_res(user):

    user= input("Enter command: ")
    if user=="hello":
        return "Hi, are you"
    elif user=="What your name":
        return "I'm a Chandu champion chatbot."
    elif user=="how are you":
        return "I'm doing well, thank you for asking!"
    elif user=="bye":
        return "Goodbye! Have a great day!"
    else:
        return "Sorry, I don't understand that command. Please try again."

    
user= chatbot_res("hello")
print("chatbot_res:-", user)
user= chatbot_res("What your name")
print("chatbot_res:-", user)
user= chatbot_res("I'm a Chandu champion chatbot.")
print("chatbot_res:-", user)
user= chatbot_res("bye")
print("chatbot_res:-", user)

    
