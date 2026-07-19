import customtkinter as ctk

from config import theme
from services.session import Session


class Sidebar(ctk.CTkFrame):

    def __init__(self, master, page_callback):

        super().__init__(
            master,
            width=230,
            fg_color=theme.SIDEBAR,
            corner_radius=0
        )

        self.pack_propagate(False)

        ctk.CTkLabel(
            self,
            text="IEMS",
            font=("Segoe UI", 28, "bold"),
            text_color="white"
        ).pack(pady=(30, 40))

        buttons = [
            ("Dashboard", "dashboard"),
            ("Income", "income"),
            ("Expenditure", "expenditure"),
            ("Reports", "reports"),
        ]

        if Session.is_admin():
            buttons.extend([
                ("Users", "users"),
                ("Settings", "settings")
            ])

        for text, page in buttons:

            ctk.CTkButton(
                self,
                text=text,
                width=180,
                height=45,
                fg_color="transparent",
                hover_color="#334155",
                anchor="w",
                command=lambda p=page: page_callback(p)
            ).pack(pady=5, padx=15)