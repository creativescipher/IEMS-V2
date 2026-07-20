import customtkinter as ctk

from config import theme
from views.widgets.toast import show_success


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
            font=theme.TITLE_FONT,
            text_color=theme.TEXT
        ).pack(
            anchor="w",
            padx=25,
            pady=(20, 15)
        )

        card = ctk.CTkFrame(
            self,
            fg_color=theme.CARD,
            corner_radius=18,
            border_width=1,
            border_color=theme.BORDER
        )

        card.pack(
            padx=25,
            pady=10,
            fill="x"
        )

        # ---------------- Company ----------------

        ctk.CTkLabel(
            card,
            text="Company Name",
            font=theme.BODY_FONT,
            text_color=theme.TEXT
        ).pack(
            anchor="w",
            padx=20,
            pady=(20, 5)
        )

        self.company = ctk.CTkEntry(
            card,
            width=350,
            height=38,
            corner_radius=10
        )

        self.company.insert(0, "Seven-Up Bottling Company")

        self.company.pack(
            anchor="w",
            padx=20,
            pady=(0, 15)
        )

        # ---------------- Appearance ----------------

        ctk.CTkLabel(
            card,
            text="Appearance",
            font=theme.BODY_FONT,
            text_color=theme.TEXT
        ).pack(
            anchor="w",
            padx=20,
            pady=(0, 5)
        )

        self.mode = ctk.CTkComboBox(
            card,
            values=["Light", "Dark"],
            width=250,
            height=38,
            corner_radius=10
        )

        self.mode.set(theme.current_mode())

        self.mode.pack(
            anchor="w",
            padx=20,
            pady=(0, 25)
        )

        # ---------------- Save ----------------

        ctk.CTkButton(
            self,
            text="Save Settings",
            width=180,
            height=40,
            corner_radius=10,
            fg_color=theme.PRIMARY,
            hover_color=theme.PRIMARY_HOVER,
            command=self.save_settings
        ).pack(
            anchor="w",
            padx=25,
            pady=20
        )

    # ==================================================

    def save_settings(self):

        theme.set_mode(self.mode.get())

        show_success(self, "Settings saved successfully.")