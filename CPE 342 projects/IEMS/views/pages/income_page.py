import customtkinter as ctk
from tkinter import messagebox

from config import theme
from services.income_service import IncomeService


class IncomePage(ctk.CTkFrame):

    def __init__(self, master):

        super().__init__(
            master,
            fg_color=theme.BACKGROUND
        )

        self.build_ui()
        self.load_data()

    # ==================================================

    def build_ui(self):

        title = ctk.CTkLabel(
            self,
            text="Income Management",
            font=theme.TITLE_FONT
        )

        title.pack(
            anchor="w",
            padx=25,
            pady=(20, 10)
        )

        toolbar = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        toolbar.pack(
            fill="x",
            padx=20,
            pady=10
        )

        ctk.CTkButton(
            toolbar,
            text="+ Add Income",
            width=140,
            command=self.add_income
        ).pack(side="left")

        self.search_entry = ctk.CTkEntry(
            toolbar,
            width=250,
            placeholder_text="Search..."
        )

        self.search_entry.pack(side="right")

        table = ctk.CTkFrame(self)

        table.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=(10, 20)
        )

        headers = [
            "ID",
            "Category",
            "Amount",
            "Description",
            "Date"
        ]

        header_frame = ctk.CTkFrame(table)

        header_frame.pack(fill="x")

        for text in headers:

            ctk.CTkLabel(
                header_frame,
                text=text,
                width=130,
                anchor="w",
                font=("Segoe UI", 12, "bold")
            ).pack(
                side="left",
                padx=5,
                pady=10
            )

        ctk.CTkLabel(
            header_frame,
            text="Action",
            width=90,
            font=("Segoe UI", 12, "bold")
        ).pack(side="right", padx=10)

        self.body = ctk.CTkScrollableFrame(table)

        self.body.pack(
            fill="both",
            expand=True
        )

    # ==================================================

    def load_data(self):

        for widget in self.body.winfo_children():
            widget.destroy()

        rows = IncomeService.get_all()

        if not rows:

            ctk.CTkLabel(
                self.body,
                text="No income records found."
            ).pack(pady=30)

            return

        for row in rows:

            record = ctk.CTkFrame(self.body)

            record.pack(
                fill="x",
                padx=5,
                pady=2
            )

            values = [

                row["id"],
                row["name"],
                f"₦{row['amount']:,.2f}",
                row["description"],
                row["transaction_date"]

            ]

            for value in values:

                ctk.CTkLabel(
                    record,
                    text=value,
                    width=130,
                    anchor="w"
                ).pack(
                    side="left",
                    padx=5,
                    pady=8
                )

            ctk.CTkButton(
                record,
                text="Delete",
                width=80,
                fg_color="#d9534f",
                hover_color="#c9302c",
                command=lambda income_id=row["id"]: self.delete_income(income_id)
            ).pack(
                side="right",
                padx=10
            )

    # ==================================================

    def add_income(self):

        from views.dialogs.income_dialog import IncomeDialog

        IncomeDialog(
            self,
            self.load_data
        )

    # ==================================================

    def delete_income(self, income_id):

        if not messagebox.askyesno(
            "Delete Income",
            "Are you sure you want to delete this income record?"
        ):
            return

        IncomeService.delete(income_id)

        messagebox.showinfo(
            "Success",
            "Income deleted successfully."
        )

        self.load_data()