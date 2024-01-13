def dict_romance_intiger(roman_letter):
    dict_nums = {
        "I" : 1,
        "X" : 10,
        "C" : 100,
        "M" : 1000,
        "V" : 5,
        "L" : 50,
        "D" : 500,
    }
    
    return dict_nums[roman_letter]
    
def process(roman_num : str) -> int:
    int_number = 0
    roman_list = list()
    for j in roman_num:
        roman_list.append(j)


    for i in range(len(roman_list)):
        try:
            num1, num2 = int(dict_romance_intiger(roman_list[i])), int(dict_romance_intiger(roman_list[i+1]))
            if num1 > num2 or num1 == num2:
                int_number = int_number + num1
                
            else:
                num1 = num2 - num1
                int_number += num1
                                
        except IndexError:
            num1, num2 = int(dict_romance_intiger(roman_list[i])), int(dict_romance_intiger(roman_list[i-1]))
            if num1 > num2:
                pass
            else:
                int_number = int_number + 1
    
    
    return int_number, roman_list

print(process("MCMXCIV"))