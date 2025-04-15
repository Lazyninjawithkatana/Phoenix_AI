from brain import phoenix_response

def main():
    print("🧠 Phoenix AI initialized. Type 'exit' to stop.\n")

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Phoenix: " + phoenix_response("exit"))
            break
        response = phoenix_response(user_input)
        print("Phoenix:", response)

if __name__ == "__main__":
    main()
