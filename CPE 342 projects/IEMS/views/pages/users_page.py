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
            font=theme.TITLE_FONT,
            text_color=theme.TEXT
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
            height=38,
            corner_radius=10,
            fg_color=theme.PRIMARY,
            hover_color=theme.PRIMARY_HOVER,
            command=self.add_user
        ).pack(side="left")

        # ==================================================
        # Table container
        # ==================================================

        table = ctk.CTkFrame(
            self,
            fg_color=theme.CARD,
            corner_radius=18,
            border_width=1,
            border_color=theme.BORDER
        )

        table.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=(5, 20)
        )

        headers = [
            ("Username", 140),
            ("Full Name", 180),
            ("Role", 120),
            ("Status", 110)
        ]

        header_frame = ctk.CTkFrame(
            table,
            fg_color="transparent"
        )

        header_frame.pack(
            fill="x",
            padx=15,
            pady=(15, 5)
        )

        for text, width in headers:

            ctk.CTkLabel(
                header_frame,
                text=text,
                width=width,
                anchor="w",
                font=theme.SMALL_FONT,
                text_color=theme.TEXT_LIGHT
            ).pack(
                side="left",
                padx=5
            )

        ctk.CTkLabel(
            header_frame,
            text="Action",
            width=90,
            anchor="e",
            font=theme.SMALL_FONT,
            text_color=theme.TEXT_LIGHT
        ).pack(side="right", padx=5)

        self.body = ctk.CTkScrollableFrame(
            table,
            fg_color="transparent"
        )

        self.body.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=(0, 15)
        )

    # ==================================================

    def load_data(self):

        for widget in self.body.winfo_children():
            widget.destroy()

        users = UserService.get_all()

        if not users:

            ctk.CTkLabel(
                self.body,
                text="No users found.",
                text_color=theme.TEXT_LIGHT
            ).pack(pady=30)

            return

        for index, user in enumerate(users):

            row_color = theme.CARD if index % 2 == 0 else theme.BACKGROUND

            row = ctk.CTkFrame(
                self.body,
                fg_color=row_color,
                corner_radius=12,
                height=56
            )

            row.pack(
                fill="x",
                padx=5,
                pady=3
            )

            row.pack_propagate(False)

            accent = theme.SUCCESS if user["is_active"] else theme.TEXT_LIGHT

            ctk.CTkFrame(
                row,
                width=4,
                fg_color=accent,
                corner_radius=4
            ).pack(
                side="left",
                fill="y",
                padx=(8, 10),
                pady=10
            )

            values = [
                (user["username"], 140),
                (user["full_name"], 180),
                (user["role"], 120)
            ]

            for text, width in values:

                ctk.CTkLabel(
                    row,
                    text=text,
                    width=width,
                    anchor="w",
                    font=theme.BODY_FONT,
                    text_color=theme.TEXT
                ).pack(
                    side="left",
                    padx=5
                )

            # ---- Status pill ----

            status_text = "Active" if user["is_active"] else "Inactive"
            status_color = theme.SUCCESS if user["is_active"] else theme.DANGER

            status_pill = ctk.CTkFrame(
                row,
                fg_color=status_color,
                corner_radius=10,
                width=90,
                height=28
            )

            status_pill.pack(
                side="left",
                padx=5
            )

            status_pill.pack_propagate(False)

            ctk.CTkLabel(
                status_pill,
                text=status_text,
                font=theme.SMALL_FONT,
                text_color="white"
            ).pack(expand=True)

            # ---- Action button ----

            if user["is_active"]:

                ctk.CTkButton(
                    row,
                    text="Disable",
                    width=90,
                    height=32,
                    corner_radius=8,
                    fg_color=theme.DANGER,
                    hover_color="#DC2626",
                    font=theme.SMALL_FONT,
                    command=lambda uid=user["id"]: self.disable(uid)
                ).pack(
                    side="right",
                    padx=10
                )

            else:

                ctk.CTkButton(
                    row,
                    text="Enable",
                    width=90,
                    height=32,
                    corner_radius=8,
                    fg_color=theme.SUCCESS,
                    hover_color="#16A34A",
                    font=theme.SMALL_FONT,
                    command=lambda uid=user["id"]: self.enable(uid)
                ).pack(
                    side="right",
                    padx=10
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