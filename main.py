from tkinter import *
def converter():
    km = round(float(mile_input.get()) * 1.609)
    my_label3.config(text=f"{km}")


window = Tk()
window.title("Mile - Kilometer Converter")
window.config(padx=20, pady=20)

# Mile's Input 1R
mile_input = Entry(width=10)
mile_input.grid(row=0, column=1)

my_label = Label(text="Miles")
my_label.grid(row=0, column=2)

# KM Output 2R
my_label2 = Label(text="is equal to")
my_label2.grid(row=1, column=0)

my_label3 = Label(text="0")
my_label3.grid(row=1, column=1)

my_label4 = Label(text="KM")
my_label4.grid(row=1, column=2)

# Button 3R
btn = Button(text="Calculate", command=converter)
btn.grid(row=2, column=1)



window.mainloop()