import customtkinter as ctk
from tkinter import messagebox
from datetime import datetime

from database.connection import get_connection
from services.income_service import IncomeService
from services.session import Session


class IncomeDialog(ctk.CTkToplevel):

    def __init__(self, parent, refresh_callback):

        super().__init__(parent)

        self.refresh_callback = refresh_callback

        self.title("Add Income")
        self.geometry("420x420")
        self.resizable(False, False)

        self.grab_set()

        ctk.CTkLabel(
            self,
            text="Add Income",
            font=("Segoe UI", 22, "bold")
        ).pack(pady=(20, 20))

        # ---------------- Category ----------------

        ctk.CTkLabel(
            self,
            text="Category"
        ).pack(anchor="w", padx=30)

        self.category = ctk.CTkComboBox(
            self,
            width=300,
            values=self.load_categories()
        )

        self.category.pack(pady=8)

        # ---------------- Amount ----------------

        ctk.CTkLabel(
            self,
            text="Amount"
        ).pack(anchor="w", padx=30)

        self.amount = ctk.CTkEntry(
            self,
            width=300,
            placeholder_text="0.00"
        )

        self.amount.pack(pady=8)

        # ---------------- Description ----------------

        ctk.CTkLabel(
            self,
            text="Description"
        ).pack(anchor="w", padx=30)

        self.description = ctk.CTkEntry(
            self,
            width=300,
            placeholder_text="Description"
        )

        self.description.pack(pady=8)

        # ---------------- Date ----------------

        ctk.CTkLabel(
            self,
            text="Transaction Date"
        ).pack(anchor="w", padx=30)

        self.date = ctk.CTkEntry(
            self,
            width=300
        )

        self.date.insert(
            0,
            datetime.today().strftime("%Y-%m-%d")
        )

        self.date.pack(pady=8)

        # ---------------- Buttons ----------------

        buttons = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        buttons.pack(pady=25)

        ctk.CTkButton(
            buttons,
            text="Save",
            width=120,
            command=self.save
        ).pack(side="left", padx=8)

        ctk.CTkButton(
            buttons,
            text="Cancel",
            width=120,
            fg_color="gray",
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

            messagebox.showerror(
                "Error",
                "Select a category."
            )
            return

        try:

            amount = float(
                self.amount.get()
            )

        except ValueError:

            messagebox.showerror(
                "Error",
                "Invalid amount."
            )

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

        messagebox.showinfo(
            "Success",
            "Income added successfully."
        )

        self.refresh_callback()

        self.destroy()