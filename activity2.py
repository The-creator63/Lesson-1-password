from tkinter import*

root = Tk()
root.title("Login Window")
root.geometry("450x300")
root.config(background = "#BCD8C1")

#creating the labels
user_name = Label(root,text = "Username").place(x = 40,y = 60)
password = Label(root,text = "Password").place(x = 40,y =100)

#creating the text boxes
user_input = Entry(root,width = 30).place(x = 120,y = 60)
pass_input = Entry(root,width = 30,show = "*").place(x = 120,y = 100)

#create the button
submit_btn = Button(root,text ="Submit").place(x = 90, y = 150)
root.mainloop()