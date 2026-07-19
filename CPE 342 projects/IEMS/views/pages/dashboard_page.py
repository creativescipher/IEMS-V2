import customtkinter as ctk

from config import theme
from services.dashboard_service import DashboardService


class DashboardPage(ctk.CTkFrame):

    def __init__(self, master):

        super().__init__(
            master,
            fg_color=theme.BACKGROUND
        )

        self.build_ui()
        self.load_dashboard()

    # ==================================================

    def build_ui(self):

        ctk.CTkLabel(
            self,
            text="Dashboard",
            font=theme.TITLE_FONT,
            text_color=theme.TEXT
        ).pack(
            anchor="w",
            padx=25,
            pady=(20, 5)
        )

        ctk.CTkLabel(
            self,
            text="Business Overview",
            font=theme.BODY_FONT,
            text_color=theme.TEXT_LIGHT
        ).pack(
            anchor="w",
            padx=25,
            pady=(0, 20)
        )

        cards = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        cards.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=10
        )

        cards.grid_columnconfigure((0, 1), weight=1)
        cards.grid_rowconfigure((0, 1), weight=1)

        self.income_card = self.create_card(
            cards,
            "Total Income",
            "#22C55E"
        )

        self.income_card.grid(
            row=0,
            column=0,
            padx=10,
            pady=10,
            sticky="nsew"
        )

        self.expense_card = self.create_card(
            cards,
            "Total Expenditure",
            "#EF4444"
        )

        self.expense_card.grid(
            row=0,
            column=1,
            padx=10,
            pady=10,
            sticky="nsew"
        )

        self.balance_card = self.create_card(
            cards,
            "Net Balance",
            "#5B5FEF"
        )

        self.balance_card.grid(
            row=1,
            column=0,
            padx=10,
            pady=10,
            sticky="nsew"
        )

        self.records_card = self.create_card(
            cards,
            "Transactions",
            "#F59E0B"
        )

        self.records_card.grid(
            row=1,
            column=1,
            padx=10,
            pady=10,
            sticky="nsew"
        )

        ctk.CTkButton(
            self,
            text="Refresh Dashboard",
            width=200,
            height=42,
            corner_radius=10,
            fg_color=theme.PRIMARY,
            hover_color=theme.PRIMARY_HOVER,
            command=self.load_dashboard
        ).pack(
            pady=(10, 25)
        )

    # ==================================================

    def create_card(self, master, title, color):

        card = ctk.CTkFrame(
            master,
            fg_color=theme.CARD,
            corner_radius=18,
            border_width=1,
            border_color=theme.BORDER,
            height=165
        )

        card.pack_propagate(False)

        top = ctk.CTkFrame(
            card,
            fg_color="transparent"
        )

        top.pack(
            fill="x",
            padx=20,
            pady=(20, 10)
        )

        ctk.CTkFrame(
            top,
            width=10,
            height=40,
            fg_color=color,
            corner_radius=10
        ).pack(
            side="left",
            padx=(0, 10)
        )

        ctk.CTkLabel(
            top,
            text=title,
            font=theme.CARD_TITLE_FONT,
            text_color=theme.TEXT
        ).pack(
            side="left"
        )

        value = ctk.CTkLabel(
            card,
            text="0",
            font=theme.CARD_VALUE_FONT,
            text_color=theme.TEXT
        )

        value.pack(
            anchor="w",
            padx=25,
            pady=(5, 10)
        )

        card.value = value

        return card

    # ==================================================

    def load_dashboard(self):

        data = DashboardService.get_summary()

        self.income_card.value.configure(
            text=f"₦{data['income']:,.2f}"
        )

        self.expense_card.value.configure(
            text=f"₦{data['expenditure']:,.2f}"
        )

        self.balance_card.value.configure(
            text=f"₦{data['balance']:,.2f}"
        )

        self.records_card.value.configure(
            text=str(
                data["income_count"] +
                data["expenditure_count"]
            )
        )