import customtkinter as ctk
from tkinter import messagebox

from config import theme


class SettingsPage(ctk.CTkFrame):

    def __init__(self, master):

        super().__init__(
            master,
            fg_color=theme.BACKGROUND
        )

        self.build_ui()

    # ==================================================

    def build_ui(self):

        ctk.CTkLabel(
            self,
            text="Settings",
            font=theme.TITLE_FONT
        ).pack(
            anchor="w",
            padx=25,
            pady=(20, 15)
        )

        card = ctk.CTkFrame(
            self,
            corner_radius=12
        )

        card.pack(
            padx=25,
            pady=10,
            fill="x"
        )

        # ---------------- Company ----------------

        ctk.CTkLabel(
            card,
            text="Company Name"
        ).pack(
            anchor="w",
            padx=20,
            pady=(20, 5)
        )

        self.company = ctk.CTkEntry(
            card,
            width=350
        )

        self.company.insert(
            0,
            "Seven-Up Bottling Company"
        )

        self.company.pack(
            padx=20,
            pady=(0, 15)
        )

        # ---------------- Currency ----------------

        ctk.CTkLabel(
            card,
            text="Currency"
        ).pack(
            anchor="w",
            padx=20,
            pady=(0, 5)
        )

        self.currency = ctk.CTkComboBox(
            card,
            values=[
                "₦ Nigerian Naira",
                "$ US Dollar",
                "£ British Pound",
                "€ Euro"
            ],
            width=250
        )

        self.currency.set("₦ Nigerian Naira")

        self.currency.pack(
            padx=20,
            pady=(0, 15)
        )

        # ---------------- Appearance ----------------

        ctk.CTkLabel(
            card,
            text="Appearance"
        ).pack(
            anchor="w",
            padx=20,
            pady=(0, 5)
        )

        self.mode = ctk.CTkComboBox(
            card,
            values=[
                "Light",
                "Dark"
            ],
            width=250
        )

        self.mode.set("Light")

        self.mode.pack(
            padx=20,
            pady=(0, 25)
        )

        # ---------------- Save ----------------

        ctk.CTkButton(
            self,
            text="Save Settings",
            width=180,
            command=self.save_settings
        ).pack(
            pady=20
        )

    # ==================================================

    def save_settings(self):

        messagebox.showinfo(
            "Success",
            "Settings saved successfully."
        )