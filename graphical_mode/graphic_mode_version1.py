import tkinter as tk

root = tk.Tk()
root.title("Roman Numeral Converter")
root.colormapwindows("")

disply_lbl = tk.Label(
    master= root,
    width=60,
    
)

def dict_roman_intiger(roman_letter):
    
    dict_nums = {"I" : 1, "X" : 10, "C" : 100, "M" : 1000, "V" : 5,  "L" : 50, "D" : 500, }
    return dict_nums[roman_letter]

def attach_number(roman_number):
    
    if roman_number in ["I", "X", "C", "M", "V", "L", "D"]:
        disply_lbl['text'] += roman_number
        
    elif roman_number == "Clean":
        disply_lbl["text"] = ""
        
    else:
        current = disply_lbl['text']
    
        int_number = 0
        i = 0
        n = len(current)
        
        while True:
            try:
                num1, num2 = int(dict_roman_intiger(current[i])), int(dict_roman_intiger(current[i+1]))
                
            except IndexError:
                if (int(dict_roman_intiger(current[i]))) < (int(dict_roman_intiger(current[i-1]))):
                    int_number += (int(dict_roman_intiger(current[i])))
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
            
        disply_lbl['text'] =  str(int_number) 

keyword_icon = [
    {
        "text": "I",
        "command": lambda: attach_number("I"),
        "value": 1,
    },
    
    {
        "text": "V",
        "command": lambda: attach_number("V"),
        "value": 5,
    },
    
    {
        "text": "X",
        "command": lambda: attach_number("X"),
        "value": 10,
    },
    
    {
        "text": "L",
        "command": lambda: attach_number("L"),
        "value": 50,
    },
    
    {
        "text": "C",
        "command": lambda: attach_number("C"),
        "value": 100,
    },
    
    {
        "text": "D",
        "command": lambda: attach_number("D"),
        "value": 500,
    }, 
    
    {
        "text": "M",
        "command": lambda: attach_number("M"),
        "value": 1000,
    },
       
        
    {
        "text": "Enter",
        "command": lambda: attach_number("Enter"),
        "value": 000,
    },
    
    {
        "text": "Clean",
        "command": lambda: attach_number("Clean"),
        "value": 000,
    }
]

button_list = []
value_list = []


for button in keyword_icon:
    keyword_btn = tk.Button(
        master=root,
        text = button['text'],
        width=3,
        height=3,
        command= button["command"]
    )
    
    button_list.append(keyword_btn)
    value_list.append(button['value'])

disply_lbl.grid(row=0, column=0, columnspan=3)


row_num, column_num = 1, 0
row_num2 , column_num2 = 2,0
row_num3 , column_num3 = 3,0

for button in zip(button_list, value_list):
    if 1 <= (button[1]) <= 10:
        button[0].grid(row=row_num, column=column_num, sticky=("E", "W", "N", "S"))
        column_num += 1
        
    elif 50 <= (button[1]) <= 500:
        button[0].grid(row=row_num2, column=column_num2, sticky=("E", "W", "N", "S"))
        column_num2 += 1

    else:
        button[0].grid(row=row_num3, column=column_num3, sticky=("E", "W", "N", "S"))
        column_num3 += 1

tk.mainloop()
