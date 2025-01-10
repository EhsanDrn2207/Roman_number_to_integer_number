from tkinter import Tk, ttk

root = Tk()

disply_lbl = ttk.Label(
    master = root,
    background="#4D4D4D",
    foreground="white",
    )
    


disply_lbl.grid(row=0, column=0, columnspan=5, sticky=('e', 'w', 'n', 's'))


def dict_roman_intiger(roman_letter : str) -> int:
    
    dict_nums = {"I" : 1, "X" : 10, "C" : 100, "M" : 1000, "V" : 5,  "L" : 50, "D" : 500, }
    return dict_nums[roman_letter]

def attach_number(roman_number : str):
    
    if roman_number in ["I", "X", "C", "M", "V", "L", "D"]:
        disply_lbl['text'] += roman_number
        
    elif roman_number == "Clear":
        disply_lbl["text"] = ""
        
    else:
        current = disply_lbl['text']
    
        int_number = 0
        i = 0
        n = len(current)
        
        if n == 1:
            disply_lbl["text"] = str(dict_roman_intiger(current))
            
        else:
            while True:
                try:
                    num1, num2 = int(dict_roman_intiger(current[i])), int(dict_roman_intiger(current[i+1]))
                    
                except IndexError:
                    if (int(dict_roman_intiger(current[i]))) < (int(dict_roman_intiger(current[i-1]))):
                        int_number += (int(dict_roman_intiger(current[i])))
                        break
                    
                except KeyError:
                    disply_lbl['text'] =  "000"
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
        
roman_buttons_featurs = [
    
    {
        "text": "I",
        "position": (1,1),
        "command" : lambda : attach_number("I")
    },

    {
        "text": "X",
        "position": (1,2),
        "command" : lambda : attach_number("X")
    },
    
    {
        "text": "C",
        "position": (1,3),
        "command" : lambda : attach_number("C")
    },

    {
        "text": "M",
        "position": (3,2),
        "command" : lambda : attach_number("M")
    },
    
    {
        "text": "V",
        "position": (2,1),
        "command" : lambda : attach_number("V")
    },
    
    {
        "text": "L",
        "position": (2,2),
        "command" : lambda : attach_number("L")
    },
    
    {
        "text": "D",
        "position": (2,3),
        "command" : lambda : attach_number("D")
    },
    
    {
        "text": "Clear",
        "position": (3,1),
        "command" : lambda : attach_number("Clear")
    },
    
    {
        "text": "Enter",
        "position": (3,3),
        "command" : lambda : attach_number("Enter")
    },
    
]

buttons_list = []

for btn_object in roman_buttons_featurs:
    btn_obj = ttk.Button(
        master=root,
        text=btn_object['text'],
        command=btn_object['command'],
    )
    row, column = btn_object['position']
    btn_obj.grid(row=row, column=column)

def bind_key():
    root.bind("<q>", quit)
    root.bind("<Return>", lambda n : attach_number("Enter"))
    root.bind("<C>", lambda n : attach_number("Clear"))
    root.bind("<i>", lambda n: attach_number("I"))
    root.bind("<v>", lambda n: attach_number("V"))
    root.bind("<x>", lambda n: attach_number("X"))
    root.bind("<l>", lambda n: attach_number("L"))
    root.bind("<c>", lambda n: attach_number("C"))
    root.bind("<d>", lambda n: attach_number("D"))
    root.bind("<m>", lambda n: attach_number("M"))
    
bind_key()
root.mainloop()
