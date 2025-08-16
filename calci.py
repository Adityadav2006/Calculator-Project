from tkinter import *
button_values= [["AC", "+/-", "%", "÷"],["7", "8", "9", "×"],["4", "5", "6", "-"],["1", "2", "3", "+"],
                 ["0", ".", "√", "="]]

right = ["÷", "×", "-", "+", "="]
top = ["AC", "+/-", "%"]

row_count = len(button_values)
column_count = len(button_values[0]) 

light_gray = "#D4D4D2"
black = "#1C1C1C"
dark_gray = "#505050"
orange = "#FF9500"
white = "white"

x=Tk()
x.title("Calcultor")

frame = Frame(x)
l=Label(frame,text="0", bg=black,fg=white,anchor="e",width=column_count)
l.grid(row=0,column=0,columnspan=column_count)

for row in range(row_count):
    for column in range(column_count):
        value=button_values[row][column]
        button=Button(frame, text=value,width=column_count-1,command=lambda value=value:clicked(value))
        button.grid(row=row+1, column=column)
frame.pack()

a="0"
operator=None
b=None
def clear():
    global a,b,operator
    a="0"
    operator=None
    b=None
def remove_decimal(n):
    if n%1==0:
        n=int(n)
    return str(n)
def clicked(value):
    global a,b,operator
    if value in right:
        if value=="=":
            if a is not None and operator is not None:
                b=l["text"]
                n1=float(a)
                n2=float(b)

                if operator=="+":
                    l["text"]=remove_decimal(n1+n2)
                elif operator=="-":
                    l["text"]=remove_decimal(n1-n2)
                elif operator=="*":
                    l["text"]=remove_decimal(n1*n2)
                elif operator=="/":
                    l["text"]=remove_decimal(n1/n2)
                clear()
        elif value in "+-×÷":
            if operator is None:
                a= l["text"]
                l["text"]="0"
                b= "0"
            operator = value
        
    elif value in top:
        if value == "AC":
            clear()
            l["text"] = "0"

        elif value == "+/-":
            result = float(l["text"]) * -1
            l["text"] = remove_decimal(result)

        elif value == "%":
            result = float(l["text"]) / 100
            l["text"] = remove_decimal(result)           
        
    else:
        if value == ".":
            if value not in l["text"]:
                l["text"] += value

        elif value in "0123456789":
            if l["text"] == "0":
               l["text"] = value #replace 0
            else:
                l["text"] += value    


x.mainloop()