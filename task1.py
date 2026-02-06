def Chatbot_respose(user_input):

    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return "Hello! How may I help you today?"

    elif "how are you?" in user_input:
        return "I'm doing great! Thanks for asking. How are you?"

    elif "your name" in user_input or "who are you?" in user_input:
        return "I am Python-scripted simple rule based chatbot. I am crreated for Codsoft internship task by Bhakti Dhore"

    elif "weather" in user_input:
        return "I can't check live weather, but I hope that the weather is nice where you are!"

    elif "how do u work?" in user_input:
        return "I look for specific keywords in your message and then match them to my 'if-else' logic"
    
    elif "CodSoft" in user_input:
        return "Codsoft is a famous platform that provide internship opportunities"

    elif "exit" in user_input or "bye" in user_input:
        return  "Goodbye! I hope you day as wondeful as you."

    else:
        return "Sorry, I didnt understand that, Can you rephrase."

print("Chatbot is ready ! Type 'exit' to stop\n")

while True:
    user_text = input("\nYou:")
    if user_text.lower() == 'exit':
        print ("Chatbot: Goodbye!")
        break

    print("\nChatbot:", Chatbot_respose(user_text))     
    
    
    
    