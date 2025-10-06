from pip import *
from tkinter import *

root=Tk()
root.title('SIMPLE CALCULATOR')

heading = Label(root, text="<-----USER INPUT", fg="black", justify='left')
heading.grid(row=0, column=3, columnspan=2)

enter_text =Entry(root, fg='black',justify="center", width=40, borderwidth=2 )
enter_text.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def button_Click(number):
    current = enter_text.get() 
    enter_text.delete(0, END)
    enter_text.insert(0, str(current) + str(number))
    return

def clear_button():
    enter_text.delete(0, END)

#def function_button():
    #first_number = enter_text.get()
    #global f_num
    #f_num = int(first_number)
    #enter_text.delete(0,END)

def button_equal():
    second_number = enter_text.get()
    enter_text.delete(0,END)
    try:
        if math == "addition":
            enter_text.insert(END, f_num + float(second_number))
        elif math == "subtraction":
            enter_text.insert(END, f_num - float(second_number))
        elif math == "multiplication":
            enter_text.insert(END, f_num * float(second_number))
        elif math == "division":
            if float(second_number) == 0:
                    enter_text.insert(END, "Error: Division by Zero")
            else:
                enter_text.insert(END, f_num / float(second_number))
    except ValueError:
        enter_text.insert(END, "Invalid Input")

def button_add():
    first_number = enter_text.get()
    global f_num
    global math
    math = "addition"
    f_num = float(first_number)
    enter_text.delete(0, END)

def button_subtract():
    first_number = enter_text.get()
    global f_num
    global math
    math = "subtraction"
    f_num = float(first_number)
    enter_text.delete(0, END)

def button_divide():
    first_number = enter_text.get()
    global f_num
    global math
    math = "division"
    f_num = float(first_number)
    enter_text.delete(0, END)

def button_multiply():
    first_number = enter_text.get()
    global f_num
    global math
    math = "multiplication"
    f_num = float(first_number)
    enter_text.delete(0, END)

#Define button
button_1 = Button(root, bg="grey", text="1", padx=40, pady=20,command=lambda: button_Click(1))   
button_2 = Button(root, bg="grey", text="2", padx=40, pady=20,command=lambda: button_Click(2))
button_3 = Button(root, bg="grey", text="3", padx=40, pady=20,command=lambda: button_Click(3))
button_4 = Button(root, bg="grey", text="4", padx=40, pady=20,command=lambda: button_Click(4))
button_5 = Button(root, bg="grey", text="5", padx=40, pady=20,command=lambda: button_Click(5))
button_6 = Button(root, bg="grey", text="6", padx=40, pady=20,command=lambda: button_Click(6))
button_7 = Button(root, bg="grey", text="7", padx=40, pady=20,command=lambda: button_Click(7))
button_8 = Button(root, bg="grey", text="8", padx=40, pady=20,command=lambda: button_Click(8))
button_9 = Button(root, bg="grey", text="9", padx=40, pady=20,command=lambda: button_Click(9))
button_0 = Button(root, bg="grey", text="0", padx=40, pady=20,command=lambda: button_Click(0))
button_dot = Button(root, bg="grey",text=".", padx=41, pady=20,command=lambda: button_Click(".")) 
button_CE = Button(root, bg="grey", text="CE", padx=36, pady=20,command=clear_button) 

#CREATING FUNCTION BUTTON
button_plus = Button(root, bg="grey", text="+", padx=31, pady=20,command=button_add)
button_subtract1 = Button(root, bg="grey", text="-", padx=30, pady=20,command=button_subtract)
button_divide1 = Button(root, bg="grey", text="/", padx=30, pady=20,command=button_divide)
button_multiply1 = Button(root,bg="grey", text="*", padx=31, pady=20,command=button_multiply)
button_equall = Button(root,bg="grey", text="=", padx=30, pady=20,command=button_equal)
button_clear = Button(root, bg="grey",text="Clear", padx=20, pady=20,command= clear_button)
button_credit = Button(root, bg= 'brown', text="First Tkinker project by Ella \n Created 2024 ^_^", pady=13)

#put button on the screen
button_1.grid(row=4,column=0)
button_2.grid(row=4,column=1)
button_3.grid(row=4,column=2)

button_4.grid(row=3,column=0)
button_5.grid(row=3,column=1)
button_6.grid(row=3,column=2)

button_7.grid(row=2,column=0)
button_8.grid(row=2,column=1)
button_9.grid(row=2,column=2)

button_0.grid(row=5,column=1)
button_CE.grid(row=5,column=0)
button_dot.grid(row=5,column=2)

button_plus.grid(row=2,column=3)
button_subtract1.grid(row=2,column=4)
button_multiply1.grid(row=3,column=3)
button_divide1.grid(row=3,column=4)
button_clear.grid(row=4,column=3)
button_equall.grid(row=4,column=4)
button_credit.grid(row=5, column=3, columnspan=2)

root.mainloop()

'''
fg='foreground'
bg="background"
'''