import customtkinter as ctk
from tkinter import messagebox

from config import theme
from services.session import Session
from services.user_service import UserService


class UsersPage(ctk.CTkFrame):

    def __init__(self, master):

        super().__init__(
            master,
            fg_color=theme.BACKGROUND
        )

        self.build_ui()
        self.load_data()

    # ==================================================

    def build_ui(self):

        ctk.CTkLabel(
            self,
            text="User Management",
            font=theme.TITLE_FONT
        ).pack(
            anchor="w",
            padx=25,
            pady=(20, 15)
        )

        toolbar = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        toolbar.pack(
            fill="x",
            padx=20,
            pady=(0, 10)
        )

        ctk.CTkButton(
            toolbar,
            text="+ Add User",
            width=140,
            command=self.add_user
        ).pack(side="left")

        table = ctk.CTkFrame(self)

        table.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=(5, 20)
        )

        header = ctk.CTkFrame(table)

        header.pack(fill="x")

        headers = [
            "Username",
            "Full Name",
            "Role",
            "Status",
            "Action"
        ]

        for text in headers:

            ctk.CTkLabel(
                header,
                text=text,
                width=140,
                anchor="w",
                font=("Segoe UI", 12, "bold")
            ).pack(
                side="left",
                padx=5,
                pady=10
            )

        self.body = ctk.CTkScrollableFrame(table)

        self.body.pack(
            fill="both",
            expand=True
        )

    # ==================================================

    def load_data(self):

        for widget in self.body.winfo_children():
            widget.destroy()

        users = UserService.get_all()

        if not users:

            ctk.CTkLabel(
                self.body,
                text="No users found."
            ).pack(pady=30)

            return

        for user in users:

            row = ctk.CTkFrame(self.body)

            row.pack(
                fill="x",
                padx=5,
                pady=3
            )

            status = "Active" if user["is_active"] else "Inactive"

            values = [
                user["username"],
                user["full_name"],
                user["role"],
                status
            ]

            for value in values:

                ctk.CTkLabel(
                    row,
                    text=value,
                    width=140,
                    anchor="w"
                ).pack(
                    side="left",
                    padx=5,
                    pady=8
                )

            if user["is_active"]:

                ctk.CTkButton(
                    row,
                    text="Disable",
                    width=90,
                    fg_color="#d9534f",
                    hover_color="#c9302c",
                    command=lambda uid=user["id"]: self.disable(uid)
                ).pack(
                    side="left",
                    padx=5
                )

            else:

                ctk.CTkButton(
                    row,
                    text="Enable",
                    width=90,
                    command=lambda uid=user["id"]: self.enable(uid)
                ).pack(
                    side="left",
                    padx=5
                )

    # ==================================================

    def enable(self, user_id):

        UserService.activate(user_id)

        self.load_data()

    # ==================================================

    def disable(self, user_id):

        current_user = Session.get_user()

        if current_user and current_user["id"] == user_id:

            messagebox.showwarning(
                "Not Allowed",
                "You cannot disable your own account."
            )

            return

        if not messagebox.askyesno(
            "Confirm",
            "Disable this user?"
        ):
            return

        UserService.deactivate(user_id)

        self.load_data()

    # ==================================================

    def add_user(self):

        from views.dialogs.user_dialog import UserDialog

        UserDialog(
            self,
            self.load_data
        )