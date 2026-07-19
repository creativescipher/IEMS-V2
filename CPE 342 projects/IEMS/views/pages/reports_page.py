import customtkinter as ctk

from config import theme
from services.report_service import ReportService


class ReportsPage(ctk.CTkFrame):

    def __init__(self, master):

        super().__init__(
            master,
            fg_color=theme.BACKGROUND
        )

        self.build_ui()
        self.load_report()

    # ==============================================

    def build_ui(self):

        ctk.CTkLabel(
            self,
            text="Reports",
            font=theme.TITLE_FONT,
            text_color=theme.TEXT
        ).pack(
            anchor="w",
            padx=25,
            pady=(20, 5)
        )

        ctk.CTkLabel(
            self,
            text="Summary of your business finances",
            font=theme.BODY_FONT,
            text_color=theme.TEXT_LIGHT
        ).pack(
            anchor="w",
            padx=25,
            pady=(0, 20)
        )

        # ==================================================
        # Stat cards
        # ==================================================

        cards = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        cards.pack(
            fill="x",
            padx=20,
            pady=10
        )

        cards.grid_columnconfigure((0, 1), weight=1)

        self.income_card = self.create_card(cards, "Total Income", theme.SUCCESS)
        self.income_card.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        self.expenditure_card = self.create_card(cards, "Total Expenditure", theme.DANGER)
        self.expenditure_card.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        self.balance_card = self.create_card(cards, "Current Balance", theme.PRIMARY)
        self.balance_card.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        self.records_card = self.create_card(cards, "Total Records", theme.WARNING)
        self.records_card.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")

        # ==================================================
        # Actions
        # ==================================================

        actions = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        actions.pack(
            pady=25
        )

        ctk.CTkButton(
            actions,
            text="Refresh Report",
            width=180,
            height=40,
            corner_radius=10,
            fg_color=theme.PRIMARY,
            hover_color=theme.PRIMARY_HOVER,
            command=self.load_report
        ).pack(side="left", padx=8)

        ctk.CTkButton(
            actions,
            text="Export Income CSV",
            width=180,
            height=40,
            corner_radius=10,
            fg_color=theme.SUCCESS,
            hover_color="#16A34A",
            command=self.export_income
        ).pack(side="left", padx=8)

        ctk.CTkButton(
            actions,
            text="Export Expenditure CSV",
            width=200,
            height=40,
            corner_radius=10,
            fg_color=theme.DANGER,
            hover_color="#DC2626",
            command=self.export_expenditure
        ).pack(side="left", padx=8)

    # ==============================================

    def create_card(self, master, title, color):

        card = ctk.CTkFrame(
            master,
            fg_color=theme.CARD,
            corner_radius=18,
            border_width=1,
            border_color=theme.BORDER,
            height=130
        )

        card.pack_propagate(False)

        top = ctk.CTkFrame(card, fg_color="transparent")
        top.pack(fill="x", padx=20, pady=(20, 5))

        ctk.CTkFrame(
            top, width=10, height=32, fg_color=color, corner_radius=8
        ).pack(side="left", padx=(0, 10))

        ctk.CTkLabel(
            top, text=title, font=theme.CARD_TITLE_FONT, text_color=theme.TEXT
        ).pack(side="left")

        value = ctk.CTkLabel(
            card, text="—", font=theme.CARD_VALUE_FONT, text_color=theme.TEXT
        )
        value.pack(anchor="w", padx=25, pady=(5, 10))

        card.value = value

        return card

    # ==============================================

    def load_report(self):

        report = ReportService.get_summary()

        self.income_card.value.configure(
            text=f"₦{report['total_income']:,.2f}"
        )

        self.expenditure_card.value.configure(
            text=f"₦{report['total_expenditure']:,.2f}"
        )

        self.balance_card.value.configure(
            text=f"₦{report['balance']:,.2f}"
        )

        self.records_card.value.configure(
            text=str(report["income_count"] + report["expenditure_count"])
        )

    # ==============================================

    def export_income(self):

        with open(
            "exports/income_report.csv",
            "w",
            encoding="utf-8"
        ) as file:

            file.write(
                "Income export generated successfully."
            )

    # ==============================================

    def export_expenditure(self):

        with open(
            "exports/expenditure_report.csv",
            "w",
            encoding="utf-8"
        ) as file:

            file.write(
                "Expenditure export generated successfully."
            )