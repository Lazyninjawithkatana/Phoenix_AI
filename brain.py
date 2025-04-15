def phoenix_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return "Hello, my friend. Phoenix AI at your service 🔥"
    elif "who are you" in user_input:
        return "I'm Phoenix, your custom AI agent built with love and Python 💻"
    elif "bye" in user_input or "exit" in user_input:
        return "Goodbye. See you soon, warrior. 🔥"
    else:
        return "I'm still learning. Can you try asking me something simpler?"
