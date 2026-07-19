import customtkinter as ctk

from config import theme
from services.session import Session


class Sidebar(ctk.CTkFrame):

    def __init__(self, master, page_callback):

        super().__init__(
            master,
            width=250,
            fg_color=theme.SIDEBAR,
            corner_radius=0
        )

        self.pack_propagate(False)

        # ==================================================
        # Logo
        # ==================================================

        logo_frame = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        logo_frame.pack(
            fill="x",
            pady=(30, 35)
        )

        ctk.CTkLabel(
            logo_frame,
            text="IEMS",
            font=("Segoe UI", 30, "bold"),
            text_color="white"
        ).pack()

        ctk.CTkLabel(
            logo_frame,
            text="Income Management",
            font=("Segoe UI", 12),
            text_color="#CBD5E1"
        ).pack()

        # ==================================================
        # Navigation
        # ==================================================

        nav = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        nav.pack(
            fill="both",
            expand=True,
            padx=15
        )

        buttons = [
            ("🏠  Dashboard", "dashboard"),
            ("💰  Income", "income"),
            ("💸  Expenditure", "expenditure"),
            ("📊  Reports", "reports"),
        ]

        if Session.is_admin():

            buttons.extend([
                ("👥  Users", "users"),
                ("⚙  Settings", "settings")
            ])

        for text, page in buttons:

            ctk.CTkButton(
                nav,
                text=text,
                height=46,
                corner_radius=12,
                fg_color="transparent",
                hover_color=theme.SIDEBAR_HOVER,
                text_color=theme.SIDEBAR_TEXT,
                font=("Segoe UI Semibold", 14),
                anchor="w",
                command=lambda p=page: page_callback(p)
            ).pack(
                fill="x",
                pady=5
            )

        # ==================================================
        # Footer
        # ==================================================

        footer = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        footer.pack(
            fill="x",
            padx=20,
            pady=(10, 20)
        )

        ctk.CTkLabel(
            footer,
            text="Version 1.0",
            text_color="#94A3B8",
            font=("Segoe UI", 11)
        ).pack()

        ctk.CTkLabel(
            footer,
            text="© 2026 IEMS",
            text_color="#64748B",
            font=("Segoe UI", 10)
        ).pack()