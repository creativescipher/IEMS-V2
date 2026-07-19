import customtkinter as ctk

from config import theme
from services.session import Session
from services.auth_service import AuthService


class Header(ctk.CTkFrame):

    def __init__(self, master, logout_callback):
        super().__init__(
            master,
            height=70,
            fg_color=theme.HEADER,
            corner_radius=0
        )

        self.pack_propagate(False)

        title = ctk.CTkLabel(
            self,
            text=theme.APP_TITLE,
            font=theme.TITLE_FONT,
            text_color=theme.TEXT
        )

        title.pack(side="left", padx=20)

        right = ctk.CTkFrame(self, fg_color="transparent")
        right.pack(side="right", padx=20)

        ctk.CTkLabel(
            right,
            text=f"{Session.full_name()} ({Session.role()})",
            font=theme.BODY_FONT
        ).pack(side="left", padx=15)

        ctk.CTkButton(
            right,
            text="Logout",
            width=100,
            fg_color=theme.DANGER,
            hover_color="#dc2626",
            command=logout_callback
        ).pack(side="left")