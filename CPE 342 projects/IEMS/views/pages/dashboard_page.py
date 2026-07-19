import customtkinter as ctk

from config import theme

from services.dashboard_service import DashboardService

from views.widgets.stat_card import StatCard


class DashboardPage(ctk.CTkFrame):

    def __init__(self, master):

        super().__init__(
            master,
            fg_color=theme.BACKGROUND
        )

        ctk.CTkLabel(
            self,
            text="Dashboard",
            font=theme.TITLE_FONT
        ).pack(
            anchor="w",
            padx=25,
            pady=(20,25)
        )

        cards = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        cards.pack(
            fill="x",
            padx=20
        )

        income = DashboardService.total_income()

        expenditure = DashboardService.total_expenditure()

        balance = DashboardService.balance()

        StatCard(
            cards,
            "Total Income",
            f"₦{income:,.2f}"
        ).pack(
            side="left",
            padx=10
        )

        StatCard(
            cards,
            "Total Expenditure",
            f"₦{expenditure:,.2f}"
        ).pack(
            side="left",
            padx=10
        )

        StatCard(
            cards,
            "Current Balance",
            f"₦{balance:,.2f}"
        ).pack(
            side="left",
            padx=10
        )