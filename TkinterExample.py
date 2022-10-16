from tkinter import *

root = Tk()
root.title('my first tkinter')
root.geometry("960x650")

################LABEL################

label1 = Label(root, text="Rzad 1", font=("Verdana", 15))
label1.grid(row=0,column=0)
label2 = Label(root, text="Rzad 2")
label2.grid(row=1,column=0)

################FRAME######################

frame = LabelFrame(root)
frame.grid(row=0, column=1, padx=25, pady=15, ipadx=60, ipady=30)
labelFrame = Label(frame, text="Rzad we framie", font=("Verdana", 15))
labelFrame.grid(row=0, column=0)

################BUTTON#######################

text = "with value set"

def print_button(text):
    print("This button works: " + text)


myButton = Button(root, text="Button1", command=lambda : print_button(text), fg="blue", bg="green", activebackground="orange")
myButton.grid(row=2, column=0)

################ENTRY#####################

entry = Entry(root, width=20, font=("Verdan", 12), justify="center", state="readonly")
entry.grid(row=0, column=2)
entry.configure(state="normal")
entry.insert(0, "23")
entry.configure(state="readonly")

print(entry.get())

#################CHECKBOX##################

varCheck = StringVar()
varCheck.set(ON)

checkBox = Checkbutton(root, text="switch", onvalue="on",
                       offvalue="off", variable=varCheck, command=lambda : print_button(varCheck.get()))
checkBox.grid(row=1, column=1)

################SLIDERS##################

def scaler(val):
    global  slider
    global sliderEntry
    sliderEntry.configure(state="normal")
    sliderEntry.delete(0, END)
    sliderEntry.insert(0, f"{10**(slider.get()/10):.2f}")
    sliderEntry.configure(state="readonly")

frameSliders = LabelFrame(root)
frameSliders.grid(row=0, column=3, padx=30, pady=30)

slider = Scale(frameSliders, from_=-20, to=20, orient="horizontal",
               width=20, length=200, showvalue=0, command=scaler)

slider.grid(row=0, column=0)

sliderEntry = Entry(frameSliders, width=5, font=("Verdan", 12), justify="center", state="readonly", borderwidth=5)
sliderEntry.grid(row=1, column=0)

sliderEntry.configure(state="normal")
sliderEntry.insert(0, 1.00)
sliderEntry.configure(state="readonly")

################RADIO##################
#https://youtu.be/0zrq2N2qAVo?t=2573

root.mainloop()

