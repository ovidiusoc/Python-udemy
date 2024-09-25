from tkinter import *


def miles_to_km():
    miles = '0'
    miles = miles_input.get()
    miles_value = float(miles)
    km = round(miles_value * 1.6, 2)
    result_label.config(text=f"{km}")


# # start of program
window = Tk()
window.title("Km to Miles converter")
window.config(padx=50, pady=50)

# label
miles_label = Label(text="Miles", font=("Ariel", 20))
miles_label.grid(row=0, column=2)

km_label = Label(text="KM", font=("Ariel", 20))
km_label.grid(row=1, column=2)

equal_label = Label(text="Is equal to", font=("Ariel", 20))
equal_label.grid(row=1, column=0)

result_label = Label(text="0", font=("Ariel", 20))
result_label.grid(row=1, column=1)


# button
my_button = Button(text="Calculate", command=miles_to_km)
my_button.grid(row=2, column=1)


# entry
miles_input = Entry(width=10)
miles_input.grid(row=0, column=1)


window.mainloop()
# end pf program

