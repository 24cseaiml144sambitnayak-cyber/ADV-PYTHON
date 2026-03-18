from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("Nayak Industries")
root.iconbitmap("pixel3.ico")

# -------- Full Screen --------
root.state("zoomed")

# -------- Get Screen Size --------
width = root.winfo_screenwidth()
height = root.winfo_screenheight()

# -------- Background Image --------
bg_img = Image.open("background.jpg")
bg_img = bg_img.resize((width, height))
bg = ImageTk.PhotoImage(bg_img)

bg_label = Label(root, image=bg)
bg_label.place(x=0, y=0)

# -------- Login Frame --------
frame = Frame(root, bg="white", padx=40, pady=40)
frame.place(relx=0.5, rely=0.5, anchor=CENTER)

# -------- Logo Image --------
img = Image.open("star.png")
resize_img = img.resize((120,80))
img = ImageTk.PhotoImage(resize_img)

img_label = Label(frame, image=img, bg="white")
img_label.pack(pady=10)

# -------- Title --------
text_label = Label(frame, text="Nayak Industries",
                   font=('Arial',22,'bold'), bg="white")
text_label.pack(pady=10)

# -------- Email --------
email_label = Label(frame, text="Email",
                    font=('Arial',14,'bold'), bg="white")
email_label.pack(pady=(15,5))

email_entry = Entry(frame, font=('Arial',14), width=25)
email_entry.pack(pady=5)

# -------- Password --------
password_label = Label(frame, text="Password",
                       font=('Arial',14,'bold'), bg="white")
password_label.pack(pady=(15,5))

password_entry = Entry(frame, font=('Arial',14), show="*", width=25)
password_entry.pack(pady=5)

# -------- Login Button --------
login_btn = Button(frame, text="Login",
                   font=('Arial',14,'bold'),
                   bg="orange", fg="white", width=15)
login_btn.pack(pady=20)

root.mainloop()