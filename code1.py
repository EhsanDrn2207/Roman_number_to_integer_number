def dict_romance_intiger(roman_letter):
    
    dict_nums = {"I" : 1, "X" : 10, "C" : 100, "M" : 1000, "V" : 5,  "L" : 50, "D" : 500, }
    return dict_nums[roman_letter]
    
def process(roman_letter : str) -> int:
    int_number = 0
    i = 0
    n = len(roman_letter)
    
    while True:
        try:
            num1, num2 = int(dict_romance_intiger(roman_letter[i])), int(dict_romance_intiger(roman_letter[i+1]))
            
        except IndexError:
            if (int(dict_romance_intiger(roman_letter[i]))) < (int(dict_romance_intiger(roman_letter[i-1]))):
                int_number += (int(dict_romance_intiger(roman_letter[i])))
                break
        
        if num1 > num2 or num1 == num2:
            int_number += num1
            i += 1

        else:
            num = num2 - num1
            int_number += num
            i += 2

        if i >= n:
            break
        
    return int_number

print(process("MCMXCIV"))