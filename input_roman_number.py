class InvalidStringInputError(Exception): # Invalid user's input
    pass

def user_input():
    valid_letters = ["I", "X" , "C", "M", "V", "L", "D"] # roman letters
    while True:
        try:
            user_input = input("Enter a romance number: ")
            for i in user_input:
                if i.upper() not in valid_letters:
                    raise InvalidStringInputError
                
            return user_input.upper()

        except InvalidStringInputError: # Error handling
            print("Your input is invalid. Plaese try again")

        