import customtkinter as ctk
from tkinter import messagebox

from config import theme
from services.expenditure_service import ExpenditureService


class ExpenditurePage(ctk.CTkFrame):

    def __init__(self, master):

        super().__init__(
            master,
            fg_color=theme.BACKGROUND
        )

        self.all_rows = []

        self.build_ui()
        self.load_data()

    # ==================================================

    def build_ui(self):

        ctk.CTkLabel(
            self,
            text="Expenditure Management",
            font=theme.TITLE_FONT,
            text_color=theme.TEXT
        ).pack(
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
            text="+ Add Expenditure",
            width=160,
            height=38,
            corner_radius=10,
            fg_color=theme.PRIMARY,
            hover_color=theme.PRIMARY_HOVER,
            command=self.add_expenditure
        ).pack(side="left")

        self.search_entry = ctk.CTkEntry(
            toolbar,
            width=250,
            height=38,
            corner_radius=10,
            placeholder_text="Search..."
        )

        self.search_entry.pack(side="right")

        self.search_entry.bind("<KeyRelease>", lambda e: self.filter_data())

        # ==================================================
        # Table container
        # ==================================================

        table = ctk.CTkFrame(
            self,
            fg_color=theme.CARD,
            corner_radius=18,
            border_width=1,
            border_color=theme.BORDER
        )

        table.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=(10, 20)
        )

        headers = [
            ("ID", 60),
            ("Category", 160),
            ("Amount", 140),
            ("Description", 260),
            ("Date", 140)
        ]

        header_frame = ctk.CTkFrame(
            table,
            fg_color="transparent"
        )

        header_frame.pack(
            fill="x",
            padx=15,
            pady=(15, 5)
        )

        for text, width in headers:

            ctk.CTkLabel(
                header_frame,
                text=text,
                width=width,
                anchor="w",
                font=theme.SMALL_FONT,
                text_color=theme.TEXT_LIGHT
            ).pack(
                side="left",
                padx=5
            )

        ctk.CTkLabel(
            header_frame,
            text="Action",
            width=90,
            anchor="e",
            font=theme.SMALL_FONT,
            text_color=theme.TEXT_LIGHT
        ).pack(side="right", padx=5)

        self.body = ctk.CTkScrollableFrame(
            table,
            fg_color="transparent"
        )

        self.body.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=(0, 15)
        )

    # ==================================================

    def load_data(self):

        self.all_rows = ExpenditureService.get_all()
        self.render_rows(self.all_rows)

    # ==================================================

    def filter_data(self):

        query = self.search_entry.get().strip().lower()

        if not query:
            self.render_rows(self.all_rows)
            return

        filtered = [
            row for row in self.all_rows
            if query in row["name"].lower()
            or query in (row["description"] or "").lower()
        ]

        self.render_rows(filtered)

    # ==================================================

    def render_rows(self, rows):

        for widget in self.body.winfo_children():
            widget.destroy()

        if not rows:

            ctk.CTkLabel(
                self.body,
                text="No expenditure records found.",
                text_color=theme.TEXT_LIGHT
            ).pack(pady=30)

            return

        for index, row in enumerate(rows):

            row_color = theme.CARD if index % 2 == 0 else theme.BACKGROUND

            record = ctk.CTkFrame(
                self.body,
                fg_color=row_color,
                corner_radius=12,
                height=52
            )

            record.pack(
                fill="x",
                padx=5,
                pady=3
            )

            record.pack_propagate(False)

            ctk.CTkFrame(
                record,
                width=4,
                fg_color=theme.DANGER,
                corner_radius=4
            ).pack(
                side="left",
                fill="y",
                padx=(8, 10),
                pady=8
            )

            values = [
                (str(row["id"]), 60),
                (row["name"], 160),
                (f"₦{row['amount']:,.2f}", 140),
                (row["description"], 260),
                (row["transaction_date"], 140)
            ]

            for text, width in values:

                ctk.CTkLabel(
                    record,
                    text=text,
                    width=width,
                    anchor="w",
                    font=theme.BODY_FONT,
                    text_color=theme.TEXT
                ).pack(
                    side="left",
                    padx=5
                )

            ctk.CTkButton(
                record,
                text="Delete",
                width=80,
                height=32,
                corner_radius=8,
                fg_color=theme.DANGER,
                hover_color="#DC2626",
                font=theme.SMALL_FONT,
                command=lambda expenditure_id=row["id"]: self.delete_expenditure(expenditure_id)
            ).pack(
                side="right",
                padx=10
            )

    # ==================================================

    def add_expenditure(self):

        from views.dialogs.expenditure_dialog import ExpenditureDialog

        ExpenditureDialog(
            self,
            self.load_data
        )

    # ==================================================

    def delete_expenditure(self, expenditure_id):

        if not messagebox.askyesno(
            "Delete Expenditure",
            "Are you sure you want to delete this expenditure record?"
        ):
            return

        ExpenditureService.delete(expenditure_id)

        messagebox.showinfo(
            "Success",
            "Expenditure deleted successfully."
        )

        self.load_data()