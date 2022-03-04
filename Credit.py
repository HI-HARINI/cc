from tkinter import*
from PIL import ImageTk, Image
import random
root=Tk()
root.geometry("600x600")
inputbox=Entry(root)
inputbox.place(relx=0.5,rely=0.5,anchor=CENTER)
img=ImageTk.PhotoImage(Image.open("cc.jpg"))
label1=Label(root,image=img,)
label1.place(relx=0.5, rely=0.8,anchor=CENTER)
def authentication():
    try:
        getinput=int(inputbox.get())
    except(ValueError):
        messagebox.showinfo("Message","Credit Card is not excepted please insert a valid pin");
button1=Button(root,text="Check Credit Card",command=authentication)
button1.place(relx=0.5, rely=0.4,anchor=CENTER)

root.mainloop()