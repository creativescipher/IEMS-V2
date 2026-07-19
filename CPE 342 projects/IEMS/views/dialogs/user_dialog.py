import customtkinter as ctk
from tkinter import messagebox

from config import theme
from services.user_service import UserService


class UserDialog(ctk.CTkToplevel):

    def __init__(self, parent, refresh_callback):

        super().__init__(parent)

        self.refresh_callback = refresh_callback

        self.title("Add User")
        self.geometry("400x460")
        self.resizable(False, False)
        self.configure(fg_color=theme.BACKGROUND)

        self.grab_set()

        ctk.CTkLabel(
            self,
            text="Add New User",
            font=theme.SUBTITLE_FONT,
            text_color=theme.TEXT
        ).pack(pady=(25, 20))

        # ---------------- Username ----------------

        ctk.CTkLabel(
            self,
            text="Username",
            font=theme.BODY_FONT,
            text_color=theme.TEXT
        ).pack(anchor="w", padx=30)

        self.username = ctk.CTkEntry(
            self,
            width=300,
            height=38,
            corner_radius=10
        )

        self.username.pack(pady=(4, 12))

        # ---------------- Full Name ----------------

        ctk.CTkLabel(
            self,
            text="Full Name",
            font=theme.BODY_FONT,
            text_color=theme.TEXT
        ).pack(anchor="w", padx=30)

        self.full_name = ctk.CTkEntry(
            self,
            width=300,
            height=38,
            corner_radius=10
        )

        self.full_name.pack(pady=(4, 12))

        # ---------------- Password ----------------

        ctk.CTkLabel(
            self,
            text="Password",
            font=theme.BODY_FONT,
            text_color=theme.TEXT
        ).pack(anchor="w", padx=30)

        self.password = ctk.CTkEntry(
            self,
            width=300,
            height=38,
            corner_radius=10,
            show="*"
        )

        self.password.pack(pady=(4, 12))

        # ---------------- Role ----------------

        ctk.CTkLabel(
            self,
            text="Role",
            font=theme.BODY_FONT,
            text_color=theme.TEXT
        ).pack(anchor="w", padx=30)

        self.role = ctk.CTkComboBox(
            self,
            width=300,
            height=38,
            corner_radius=10,
            values=[
                "Admin",
                "Staff"
            ]
        )

        self.role.set("Staff")

        self.role.pack(pady=(4, 12))

        # ---------------- Buttons ----------------

        buttons = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        buttons.pack(pady=25)

        ctk.CTkButton(
            buttons,
            text="Save",
            width=130,
            height=40,
            corner_radius=10,
            fg_color=theme.PRIMARY,
            hover_color=theme.PRIMARY_HOVER,
            font=theme.BODY_FONT,
            command=self.save
        ).pack(
            side="left",
            padx=8
        )

        ctk.CTkButton(
            buttons,
            text="Cancel",
            width=130,
            height=40,
            corner_radius=10,
            fg_color="transparent",
            hover_color=theme.BORDER,
            border_width=1,
            border_color=theme.BORDER,
            text_color=theme.TEXT,
            font=theme.BODY_FONT,
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