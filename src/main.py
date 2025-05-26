print("Welcome to KongChat!")
while True:
    msg = input("You: ")
    if msg == "/quit":
        print("Goodbye!")
        break
    else:
        print("KongBot: I received your message.")
