import customtkinter as ctk

from config import theme


class UsersPage(ctk.CTkFrame):

    def __init__(self, master):

        super().__init__(master, fg_color=theme.BACKGROUND)

        ctk.CTkLabel(
            self,
            text="Income",
            font=theme.TITLE_FONT
        ).pack(padx=20, pady=20)