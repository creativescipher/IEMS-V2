import customtkinter as ctk
from tkinter import messagebox

from services.user_service import UserService


class UserDialog(ctk.CTkToplevel):

    def __init__(self, parent, refresh_callback):

        super().__init__(parent)

        self.refresh_callback = refresh_callback

        self.title("Add User")
        self.geometry("400x420")
        self.resizable(False, False)

        self.grab_set()

        ctk.CTkLabel(
            self,
            text="Add New User",
            font=("Segoe UI", 22, "bold")
        ).pack(pady=(20, 20))

        # ---------------- Username ----------------

        ctk.CTkLabel(
            self,
            text="Username"
        ).pack(anchor="w", padx=30)

        self.username = ctk.CTkEntry(
            self,
            width=300
        )

        self.username.pack(pady=8)

        # ---------------- Full Name ----------------

        ctk.CTkLabel(
            self,
            text="Full Name"
        ).pack(anchor="w", padx=30)

        self.full_name = ctk.CTkEntry(
            self,
            width=300
        )

        self.full_name.pack(pady=8)

        # ---------------- Password ----------------

        ctk.CTkLabel(
            self,
            text="Password"
        ).pack(anchor="w", padx=30)

        self.password = ctk.CTkEntry(
            self,
            width=300,
            show="*"
        )

        self.password.pack(pady=8)

        # ---------------- Role ----------------

        ctk.CTkLabel(
            self,
            text="Role"
        ).pack(anchor="w", padx=30)

        self.role = ctk.CTkComboBox(
            self,
            width=300,
            values=[
                "Admin",
                "Staff"
            ]
        )

        self.role.set("Staff")

        self.role.pack(pady=8)

        # ---------------- Buttons ----------------

        buttons = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        buttons.pack(pady=25)

        ctk.CTkButton(
            buttons,
            text="Save",
            width=120,
            command=self.save
        ).pack(
            side="left",
            padx=8
        )

        ctk.CTkButton(
            buttons,
            text="Cancel",
            width=120,
            fg_color="gray",
            command=self.destroy
        ).pack(
            side="left",
            padx=8
        )

    # ==================================================

    def save(self):

        username = self.username.get().strip()
        full_name = self.full_name.get().strip()
        password = self.password.get()
        role = self.role.get()

        if not username or not full_name or not password:

            messagebox.showerror(
                "Error",
                "All fields are required."
            )

            return

        try:

            UserService.add(
                username,
                password,
                full_name,
                role
            )

            messagebox.showinfo(
                "Success",
                "User added successfully."
            )

            self.refresh_callback()

            self.destroy()

        except Exception as e:

            messagebox.showerror(
                "Error",
                str(e)
            )