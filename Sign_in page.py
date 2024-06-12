from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

# Dictionary to store user credentials
user_credentials = {}

# Function to handle login
def handle_login():
    email = email_input.get()
    password = password_input.get()
    if email in user_credentials and user_credentials[email] == password:
        messagebox.showinfo("Wohoooooo!", "Login successful")
    else:
        messagebox.showerror("oops!", "Incorrect User email or password")

# Function to handle signup
def handle_signup():
    signup_window = Toplevel(root)
    signup_window.title("Sign Up")
    signup_window.configure(background='#FFD1DC')
    signup_window.geometry('400x300')

    Label(signup_window, text="Enter your Email", fg='black', bg='#FFD1DC').pack(pady=(20, 5))
    signup_email_input = Entry(signup_window, width=50)
    signup_email_input.pack(ipady=6, pady=(1, 15))

    Label(signup_window, text="Enter your Password", fg='black', bg='#FFD1DC').pack(pady=(20, 5))
    signup_password_input = Entry(signup_window, width=50, show='*')
    signup_password_input.pack(ipady=6, pady=(1, 15))

    def save_signup():
        email = signup_email_input.get()
        password = signup_password_input.get()
        if email and password:
            user_credentials[email] = password
            messagebox.showinfo("Success", "Signup successful!")
            signup_window.destroy()
        else:
            messagebox.showerror("Error", "Please enter both email and password")

    Button(signup_window, text='Sign Up', fg='black', bg='white', command=save_signup).pack(pady=10)

# Function to open login page
def open_login():
    global email_input  # Declare email_input as global
    global password_input  # Declare password_input as global

    login_window = Toplevel(root)
    login_window.title("Login Page")
    login_window.configure(background='#FFD1DC')
    login_window.geometry('400x300')

    img = Image.open('readings_logo.png')
    resize_image = img.resize((100, 100), Image.Resampling.LANCZOS)
    img = ImageTk.PhotoImage(resize_image)

    panel = Label(login_window, image=img, bg='#FFD1DC')
    panel.image = img  # To prevent garbage collection
    panel.pack(pady=10)

    Label(login_window, text='Welcome to Readings Bookshop', fg='black', bg='#FFD1DC').pack()
    Label(login_window, text="Enter your Email", fg='black', bg='#FFD1DC').pack(pady=(28, 5))

    email_input = Entry(login_window, width=50)
    email_input.pack(ipady=6, pady=(1, 15))

    Label(login_window, text="Enter your Password", fg="black", bg="#FFD1DC").pack(pady=(28, 5))

    password_input = Entry(login_window, width=50, show='*')
    password_input.pack(ipady=6, pady=(1, 15))

    Button(login_window, text='Login', fg='black', bg='white', command=handle_login).pack(pady=(10, 10))

# Main window setup
root = Tk()
root.title('Welcome Page')
root.iconbitmap('book_2_icon.png')
root.minsize(600, 600)
root.configure(background='#FFD1DC')

Label(root, text="Welcome to the Readings Bookshop", fg='black', bg='#FFD1DC', font=('Times New Roman', 20)).pack(pady=30)

Button(root, text='Sign In', fg='black', bg='white', command=open_login, font=('Times New Roman', 15)).pack(pady=20)
Button(root, text='Sign Up', fg='black', bg='white', command=handle_signup, font=('Times New Roman', 15)).pack(pady=20)

root.mainloop()

