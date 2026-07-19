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
            font=theme.TITLE_FONT
        ).pack(
            anchor="w",
            padx=25,
            pady=(20, 20)
        )

        cards = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        cards.pack(
            padx=20,
            pady=10,
            fill="both",
            expand=True
        )

        cards.grid_columnconfigure((0, 1), weight=1)
        cards.grid_rowconfigure((0, 1), weight=1)

        self.income_card = self.create_card(
            cards,
            "Total Income"
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
            "Total Expenditure"
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
            "Net Balance"
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
            "Records"
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
            width=180,
            command=self.load_dashboard
        ).pack(
            pady=20
        )

    # ==================================================

    def create_card(self, master, title):

        card = ctk.CTkFrame(
            master,
            corner_radius=12,
            height=140
        )

        card.pack_propagate(False)

        ctk.CTkLabel(
            card,
            text=title,
            font=("Segoe UI", 16, "bold")
        ).pack(
            pady=(20, 10)
        )

        value = ctk.CTkLabel(
            card,
            text="",
            font=("Segoe UI", 22)
        )

        value.pack()

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
            text=(
                f"Income: {data['income_count']}\n"
                f"Expense: {data['expenditure_count']}"
            )
        )