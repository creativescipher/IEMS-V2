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
            font=theme.TITLE_FONT
        ).pack(
            anchor="w",
            padx=25,
            pady=(20, 20)
        )

        self.report_frame = ctk.CTkFrame(self)

        self.report_frame.pack(
            fill="x",
            padx=25,
            pady=10
        )

        self.income_label = ctk.CTkLabel(
            self.report_frame,
            text=""
        )
        self.income_label.pack(
            anchor="w",
            padx=20,
            pady=10
        )

        self.expenditure_label = ctk.CTkLabel(
            self.report_frame,
            text=""
        )
        self.expenditure_label.pack(
            anchor="w",
            padx=20,
            pady=10
        )

        self.balance_label = ctk.CTkLabel(
            self.report_frame,
            text=""
        )
        self.balance_label.pack(
            anchor="w",
            padx=20,
            pady=10
        )

        self.income_count_label = ctk.CTkLabel(
            self.report_frame,
            text=""
        )
        self.income_count_label.pack(
            anchor="w",
            padx=20,
            pady=10
        )

        self.expenditure_count_label = ctk.CTkLabel(
            self.report_frame,
            text=""
        )
        self.expenditure_count_label.pack(
            anchor="w",
            padx=20,
            pady=10
        )

        ctk.CTkButton(
            self,
            text="Refresh Report",
            command=self.load_report
        ).pack(
            pady=10
        )

        ctk.CTkButton(
            self,
            text="Export Income CSV",
            command=self.export_income
        ).pack(
            pady=10
        )

        ctk.CTkButton(
            self,
            text="Export Expenditure CSV",
            command=self.export_expenditure
        ).pack(
            pady=10
        )

    # ==============================================

    def load_report(self):

        report = ReportService.get_summary()

        self.income_label.configure(
            text=f"Total Income: ₦{report['total_income']:,.2f}"
        )

        self.expenditure_label.configure(
            text=f"Total Expenditure: ₦{report['total_expenditure']:,.2f}"
        )

        self.balance_label.configure(
            text=f"Current Balance: ₦{report['balance']:,.2f}"
        )

        self.income_count_label.configure(
            text=f"Income Records: {report['income_count']}"
        )

        self.expenditure_count_label.configure(
            text=f"Expenditure Records: {report['expenditure_count']}"
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