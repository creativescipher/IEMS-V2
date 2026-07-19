import customtkinter as ctk

from config import theme


class StatCard(ctk.CTkFrame):

    def __init__(self, master, title, value):

        super().__init__(
            master,
            width=250,
            height=120,
            fg_color=theme.CARD,
            border_width=1,
            border_color=theme.BORDER,
            corner_radius=12
        )

        self.pack_propagate(False)

        ctk.CTkLabel(
            self,
            text=title,
            font=theme.SMALL_FONT,
            text_color=theme.TEXT_LIGHT
        ).pack(anchor="w", padx=20, pady=(18, 5))

        self.value = ctk.CTkLabel(
            self,
            text=value,
            font=("Segoe UI", 26, "bold"),
            text_color=theme.TEXT
        )

        self.value.pack(anchor="w", padx=20)

    def set_value(self, value):
        self.value.configure(text=value)