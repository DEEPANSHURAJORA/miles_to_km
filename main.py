from tkinter import  *
def covert():
    m = float(miles.get())
    killometer = m*1.609
    result.config(text = f"{killometer}")
window = Tk()
window.title("MILES TO KM CONVERTER")
window.config(padx = 20,pady=20)

miles = Entry(width = 5)
miles.grid(column =1, row=0)

label = Label(text = "miles")
label.grid(column = 2,row =0)

equal = Label(text = "is equal to")
equal.grid(column = 0 ,row =1)

result = Label(text = "0")
result.grid(column =1,row =1)


km = Label(text = "km")
km.grid(column = 2,row =1)

calculate = Button(text = "calculate",command=covert)
calculate.grid(column = 1,row =2)





window.mainloop()