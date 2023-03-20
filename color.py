from tkinter import *
import random

root=Tk()
root.title("encapsulation")
root.geometry("500x400")
root.config(bg="white")
cn=Label(root,font=("Ariel",40),bg="white")
cn.place(relx=0.5,rely=0.3,anchor=CENTER)

class g:
    def __init__(self):
        self.__score=0
    def up(self):
        self.text=["BLACK","PINK","YELLOW","ORANGE","RED"]
        self.random=random.randint(0,5)
        self.color=["black","pink","yellow","orange","red"]
        self.r=random.randint(0,5)
        cn["text"]=self.text[self.random]
        cn["fg"]=self.text[self.r]
        
obj=g()
btn = Button(root, text="START" ,command=obj.up, bg="dark olive green", fg="black", relief=FLAT, padx=10, pady=1, font=("Arial",15))
btn.place(relx=0.5,rely=0.4,anchor=CENTER)
root.mainloop()