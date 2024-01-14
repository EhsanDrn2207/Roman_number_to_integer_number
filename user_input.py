class InvalidStringInput(Exception):
    pass

def user_input():
    valid_letters = ["I", "X" , "C", "M", "V", "L", "D"]
    while True:
        try:
            user_input = input("Enter a romance number: ")
            for i in user_input:
                if i.upper() not in user_input:
                    raise InvalidStringInput
                
            return user_input.upper()

        except InvalidStringInput:
            print("Your input is invalid. Plaese try again")

        