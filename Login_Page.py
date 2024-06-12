from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
def handle_login():
    email=email_input.get()
    password=password_input.get()
    print(email,password)
    if email=="abc@gmail.com" and password=="1234":
        messagebox.showinfo("Wohoooooo! \nU0001F600","Login successfull")
    else:
        messagebox.showerror("oops! \nU0001F62A","Incorrect User email or password")
root=Tk()
root.title('Login Page')
root.iconbitmap('book_2_icon.png')
root.minsize(600, 600)
root.configure(background='#FFD1DC')

img=Image.open('readings_logo.png')
resize_image=img.resize((100, 100), Image.Resampling.LANCZOS) 
img=ImageTk.PhotoImage(resize_image)

panel=Label(root,image=img,bg='#FFD1DC')
panel.pack(pady=30)

text_label=Label(root,text='Welcome to Readings Bookshop', fg='black', bg='#FFD1DC')
text_label.pack()
text_label.config(font=('Times New Roman', 15))

email_label=Label(root,text="Enter your Email", fg='black', bg='#FFD1DC')
email_label.pack(pady=(28,5))
email_label.config(font=('Times new roman', 10))

email_input=Entry(root,width=50,)
email_input.pack(ipady=6,pady=(1,15))

password_label=Label(root,text="Enter your password", fg="black", bg="#FFD1DC")
password_label.pack(pady=(30,6))
password_label.config(font=('Times new roman', 10))

password_input=Entry(root,width=50,show='*')
password_input.pack(ipady=6,pady=(1,15))

login_btn=Button(root,text='Login',fg='black', bg='white',command=handle_login)
login_btn.pack(pady=(10,10))

root.mainloop()


