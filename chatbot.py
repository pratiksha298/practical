def chatbot():
    print("Chatbot: Hi! I am your simple chatbot. Ask me anything!")
    print("Type 'exit' to end the chat.")
    
    while True:
        user_input = input("You: ").lower()
        
        if user_input == "exit":
            print("Chatbot: Goodbye! Have a great day!")
            break
        elif "hello" in user_input or "hi" in user_input:
            print("Chatbot: Hello! How can I help you today?")
        elif "your name" in user_input:
            print("Chatbot: I am a simple chatbot created by you!")
        elif "how are you" in user_input:
            print("Chatbot: I'm just a program, but I'm functioning perfectly!")
        elif "thank you" in user_input:
            print("Chatbot: You're welcome! Anything else?")
        else:
            print("Chatbot: Sorry, I didn't understand that. Can you please rephrase?")


chatbot()