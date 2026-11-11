

print("========================================")
print("          WELCOME TO AI CHATBOT")
print("========================================")
print("Bot: Hello! I am your personal AI chatbot.")
print("Bot: Ask me anything or type 'bye' to exit.")
print("----------------------------------------")

while True:

    user_input = input("You: ").lower().strip()

    # Greetings
    if user_input in ["hi", "hello", "hey", "assalam o alaikum"]:
        print("Bot: Hello! Nice to meet you! 😊")

    # How are you?
    elif user_input in ["how are you", "how are you doing"]:
        print("Bot: I am doing great! Thanks for asking.")

    # Name
    elif user_input in ["what is your name", "your name"]:
        print("Bot: I am your personal AI chatbot.")

    # What is AI?
    elif user_input in ["what is ai", "define ai", "what is artificial intelligence"]:
        print("Bot: AI stands for Artificial Intelligence.")
        print("Bot: It is the ability of machines to perform tasks")
        print("Bot: that normally require human intelligence.")

    # Who created you?
    elif user_input in ["who created you", "who made you", "who is your creator"]:
        print("Bot: I am a rule-based chatbot created by you using Python!")
        print("Bot: ChatGPT, on the other hand, was created by OpenAI.")

    # What can you do?
    elif user_input in ["what can you do", "your features"]:
        print("Bot: I can answer basic questions, tell jokes")
        print("Bot: and share information about AI and programming.")

    # Are you human?
    elif user_input in ["are you human", "are you a robot"]:
        print("Bot: I am a computer program, not a human!")

    # What is Python?
    elif user_input in ["what is python", "define python"]:
        print("Bot: Python is a popular programming language.")
        print("Bot: It is used in AI, websites, automation and more.")

    # What is your purpose?
    elif user_input in ["what is your purpose", "your purpose"]:
        print("Bot: My purpose is to answer questions and help users.")

    # Tell a joke
    elif user_input in ["tell me a joke", "joke", "make me laugh"]:
        print("Bot: Why do programmers prefer dark mode?")
        print("Bot: Because light attracts bugs! 😂")

    # Another joke
    elif user_input in ["another joke", "one more joke"]:
        print("Bot: Why did the computer go to the doctor?")
        print("Bot: Because it had a virus! 😂")

    # What is coding?
    elif user_input in ["what is coding", "define coding"]:
        print("Bot: Coding is the process of writing instructions")
        print("Bot: that tell a computer what to do.")

    # Thank you
    elif user_input in ["thank you", "thanks"]:
        print("Bot: You're welcome! Happy to help. 😊")

    # Goodbye
    elif user_input in ["bye", "exit", "quit"]:
        print("Bot: Goodbye! Have a wonderful day. 👋")
        break

    # Unknown input
    else:
        print("Bot: Sorry, I don't understand that.")
        print("Bot: Try asking me something else!")

    print("----------------------------------------")
