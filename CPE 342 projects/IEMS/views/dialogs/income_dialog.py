import customtkinter as ctk
from tkinter import messagebox
from datetime import datetime

from config import theme
from database.connection import get_connection
from services.income_service import IncomeService
from services.session import Session
from views.widgets.toast import show_success, show_error


class IncomeDialog(ctk.CTkToplevel):

    def __init__(self, parent, refresh_callback):

        super().__init__(parent)

        self.refresh_callback = refresh_callback

        self.title("Add Income")
        self.geometry("420x520")
        self.resizable(False, False)
        self.configure(fg_color=theme.BACKGROUND)

        self.grab_set()

        ctk.CTkLabel(
            self,
            text="Add Income",
            font=theme.SUBTITLE_FONT,
            text_color=theme.TEXT
        ).pack(pady=(25, 20))

        # ---------------- Category ----------------

        ctk.CTkLabel(
            self,
            text="Category",
            font=theme.BODY_FONT,
            text_color=theme.TEXT
        ).pack(anchor="w", padx=30)

        self.category = ctk.CTkComboBox(
            self,
            width=300,
            height=38,
            corner_radius=10,
            values=self.load_categories()
        )

        self.category.pack(pady=(4, 12))

        # ---------------- Amount ----------------

        ctk.CTkLabel(
            self,
            text="Amount",
            font=theme.BODY_FONT,
            text_color=theme.TEXT
        ).pack(anchor="w", padx=30)

        self.amount = ctk.CTkEntry(
            self,
            width=300,
            height=38,
            corner_radius=10,
            placeholder_text="0.00"
        )

        self.amount.pack(pady=(4, 12))

        # ---------------- Description ----------------

        ctk.CTkLabel(
            self,
            text="Description",
            font=theme.BODY_FONT,
            text_color=theme.TEXT
        ).pack(anchor="w", padx=30)

        self.description = ctk.CTkEntry(
            self,
            width=300,
            height=38,
            corner_radius=10,
            placeholder_text="Description"
        )

        self.description.pack(pady=(4, 12))

        # ---------------- Date ----------------

        ctk.CTkLabel(
            self,
            text="Transaction Date",
            font=theme.BODY_FONT,
            text_color=theme.TEXT
        ).pack(anchor="w", padx=30)

        self.date = ctk.CTkEntry(
            self,
            width=300,
            height=38,
            corner_radius=10
        )

        self.date.insert(
            0,
            datetime.today().strftime("%Y-%m-%d")
        )

        self.date.pack(pady=(4, 12))

        # ---------------- Buttons ----------------

        buttons = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        buttons.pack(pady=(20, 25))

        ctk.CTkButton(
            buttons,
            text="Save",
            width=130,
            height=40,
            corner_radius=10,
            fg_color=theme.PRIMARY,
            hover_color=theme.PRIMARY_HOVER,
            font=theme.BODY_FONT,
            command=self.save
        ).pack(side="left", padx=8)

        ctk.CTkButton(
            buttons,
            text="Cancel",
            width=130,
            height=40,
            corner_radius=10,
            fg_color="transparent",
            hover_color=theme.BORDER,
            border_width=1,
            border_color=theme.BORDER,
            text_color=theme.TEXT,
            font=theme.BODY_FONT,
            command=self.destroy
        ).pack(side="left", padx=8)

    # ======================================================

    def load_categories(self):

        conn = get_connection()

        cursor = conn.cursor()

        cursor.execute("""
            SELECT name
            FROM categories
            WHERE type='Income'
            ORDER BY name
        """)

        rows = cursor.fetchall()

        conn.close()

        return [row["name"] for row in rows]

    # ======================================================

    def save(self):

        if not self.category.get():

            show_error(self, "Select a category.")
            return

        try:

            amount = float(
                self.amount.get()
            )

        except ValueError:

            show_error(self, "Invalid amount.")
            return

        conn = get_connection()

        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT id
            FROM categories
            WHERE name=?
            """,
            (
                self.category.get(),
            )
        )

        category = cursor.fetchone()

        conn.close()

        IncomeService.add(

            category["id"],

            amount,

            self.description.get(),

            self.date.get(),

            Session.get_user()["id"]

        )

        self.refresh_callback()

        self.destroy()

        show_success(self.master, "Income added successfully.")