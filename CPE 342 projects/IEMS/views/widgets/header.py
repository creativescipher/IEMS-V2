import customtkinter as ctk
from config import theme
from services.session import Session


class Header(ctk.CTkFrame):
    def __init__(self, master, logout_callback):
        super().__init__(
            master,
            height=80,
            fg_color=theme.HEADER,
            corner_radius=0
        )
        self.pack_propagate(False)
        # ==================================================
        # LEFT SIDE
        # ==================================================
        left = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )
        left.pack(
            side="left",
            padx=25,
            pady=10
        )
        ctk.CTkLabel(
            left,
            text="Income & Expenditure Management System",
            font=("Segoe UI Semibold", 22),
            text_color=theme.TEXT
        ).pack(anchor="w")
        ctk.CTkLabel(
            left,
            text="Manage your business finances efficiently",
            font=("Segoe UI", 12),
            text_color=theme.TEXT_LIGHT
        ).pack(anchor="w")
        # ==================================================
        # RIGHT SIDE
        # ==================================================
        right = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )
        right.pack(
            side="right",
            padx=25
        )

        # ---- Theme toggle button (new) ----
        self.mode_button = ctk.CTkButton(
            right,
            text="🌙" if theme.current_mode() == "Light" else "☀",
            width=40,
            height=40,
            corner_radius=10,
            fg_color=theme.BACKGROUND,
            hover_color=theme.BORDER,
            text_color=theme.TEXT,
            command=self.toggle_theme
        )
        self.mode_button.pack(side="left", padx=(0, 15))

        user_card = ctk.CTkFrame(
            right,
            corner_radius=12,
            fg_color=theme.BACKGROUND
        )
        user_card.pack(
            side="left",
            padx=(0, 15)
        )
        ctk.CTkLabel(
            user_card,
            text=Session.full_name(),
            font=("Segoe UI Semibold", 13),
            text_color=theme.TEXT
        ).pack(
            padx=15,
            pady=(8, 0)
        )
        ctk.CTkLabel(
            user_card,
            text=Session.role(),
            font=("Segoe UI", 11),
            text_color=theme.TEXT_LIGHT
        ).pack(
            padx=15,
            pady=(0, 8)
        )
        ctk.CTkButton(
            right,
            text="Logout",
            width=110,
            height=40,
            corner_radius=10,
            fg_color=theme.DANGER,
            hover_color="#DC2626",
            command=logout_callback
        ).pack(side="left")

    # ==================================================

    def toggle_theme(self):
        new_mode = theme.toggle_mode()

        self.mode_button.configure(
            text="🌙" if new_mode == "Light" else "☀"
        )