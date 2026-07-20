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

        # ---- Theme toggle button ----
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

        # ---- User card (now clickable — opens Change Password) ----
        user_card = ctk.CTkFrame(
            right,
            corner_radius=12,
            fg_color=theme.BACKGROUND
        )
        user_card.pack(
            side="left",
            padx=(0, 15)
        )

        name_label = ctk.CTkLabel(
            user_card,
            text=Session.full_name(),
            font=("Segoe UI Semibold", 13),
            text_color=theme.TEXT
        )
        name_label.pack(
            padx=15,
            pady=(8, 0)
        )

        role_label = ctk.CTkLabel(
            user_card,
            text=Session.role(),
            font=("Segoe UI", 11),
            text_color=theme.TEXT_LIGHT
        )
        role_label.pack(
            padx=15,
            pady=(0, 8)
        )

        for widget in (user_card, name_label, role_label):
            widget.bind("<Button-1>", lambda e: self.open_change_password())
            widget.configure(cursor="hand2")

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

    # ==================================================

    def open_change_password(self):

        from views.dialogs.change_password_dialog import ChangePasswordDialog

        ChangePasswordDialog(self.winfo_toplevel())