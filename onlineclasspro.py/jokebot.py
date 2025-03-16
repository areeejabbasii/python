
prompt: str = "what do you want"
joke: str = "Here is a joke for you! Sana is heading to the grocery."
sorry: str = "Sorry, I'm only telling jokes."

def main():
    user_input = input(prompt).strip().lower()  # Take user input properly
    if "joke" in user_input:
        print(joke)
    else:
        print(sorry)
main()
