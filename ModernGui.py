from tkinter import *
import customtkinter

customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("500x350")

def login():
    print("Login " + entry1.get())

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20,padx=60,fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="Logn")
label.pack(pady=12,padx=10)

entry1 = customtkinter.CTkEntry(master=frame,placeholder_text="UserName")
entry1.pack(pady=12,padx=10)

entry2 = customtkinter.CTkEntry(master=frame,placeholder_text="Password", show="*")
entry2.pack(pady=12,padx=10)

button = customtkinter.CTkButton(master=frame, text="Login", command=login)
button.pack(pady=12,padx=10)

checkbox= customtkinter.CTkCheckBox(master=frame, text="remember me")
checkbox.pack(pady=12,padx=10)

root.mainloop()