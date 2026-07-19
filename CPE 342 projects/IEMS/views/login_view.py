import customtkinter as ctk
from tkinter import messagebox

from services.auth_service import AuthService


class LoginView(ctk.CTk):

    def __init__(self):
        super().__init__()

        ctk.set_appearance_mode("Light")
        ctk.set_default_color_theme("blue")

        self.title("Income & Expenditure Management System")
        self.geometry("500x420")
        self.resizable(False, False)

        title = ctk.CTkLabel(
            self,
            text="Income & Expenditure\nManagement System",
            font=("Segoe UI", 24, "bold")
        )
        title.pack(pady=(40, 25))

        self.username = ctk.CTkEntry(
            self,
            width=300,
            placeholder_text="Username"
        )
        self.username.pack(pady=10)

        self.password = ctk.CTkEntry(
            self,
            width=300,
            placeholder_text="Password",
            show="*"
        )
        self.password.pack(pady=10)

        self.status = ctk.CTkLabel(
            self,
            text="",
            text_color="red"
        )
        self.status.pack()

        self.login_button = ctk.CTkButton(
            self,
            text="Login",
            width=220,
            command=self.login
        )
        self.login_button.pack(pady=25)

        self.bind("<Return>", lambda event: self.login())

    def login(self):

        username = self.username.get().strip()
        password = self.password.get()

        self.status.configure(text="")

        if not username or not password:
            self.status.configure(
                text="Please enter your username and password."
            )
            return

        self.login_button.configure(state="disabled")

        if AuthService.login(username, password):

            messagebox.showinfo(
                "Login Successful",
                f"Welcome, {username}!"
            )

            self.open_main()

        else:

            self.status.configure(
                text="Invalid username or password."
            )

            self.login_button.configure(state="normal")

    def open_main(self):

        from views.main_shell import MainShell

        # Hide the login window instead of destroying it
        self.withdraw()

        shell = MainShell()

        shell.mainloop()

        # If the shell closes, close the login window too
        self.destroy()