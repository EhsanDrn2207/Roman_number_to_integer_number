from input_roman_number import user_input

def dict_romance_intiger(roman_letter):
    
    dict_nums = {"I" : 1, "X" : 10, "C" : 100, "M" : 1000, "V" : 5,  "L" : 50, "D" : 500, }
    return dict_nums[roman_letter]
    
def process(roman_letter : str) -> int:
    int_number = 0
    index = 0
    roman_letter_length = len(roman_letter)
    
    while True:
        try:
            # finding the equivalent of roman numbers
            num1, num2 = int(dict_romance_intiger(roman_letter[index])), int(dict_romance_intiger(roman_letter[index+1]))
            
        except IndexError:
            # for the last roman numbers
            if (int(dict_romance_intiger(roman_letter[index]))) < (int(dict_romance_intiger(roman_letter[index-1]))):
                int_number += (int(dict_romance_intiger(roman_letter[index])))
                break
        
        if num1 > num2 or num1 == num2:
            int_number += num1
            index += 1

        else:
            num = num2 - num1 # IV = 4, IX = 9, XC = 90 , ......
            int_number += num
            index += 2

        if index >= roman_letter_length:
            break
        
    return int_number

romance_number = user_input() # get roman number from user

with open("numbers.txt", 'a') as file:
    number = process(romance_number)
    print(number)
    file.write(str(number))
    file.write("\n---------------------------------\n")