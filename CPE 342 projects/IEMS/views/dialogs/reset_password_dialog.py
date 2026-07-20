import customtkinter as ctk
from tkinter import messagebox

from config import theme
from services.user_service import UserService
from views.widgets.toast import show_success, show_error


class ResetPasswordDialog(ctk.CTkToplevel):

    def __init__(self, parent, user_id, username, refresh_callback=None):

        super().__init__(parent)

        self.user_id = user_id
        self.refresh_callback = refresh_callback

        self.title("Reset Password")
        self.geometry("380x360")
        self.resizable(False, False)
        self.configure(fg_color=theme.BACKGROUND)

        self.grab_set()

        ctk.CTkLabel(
            self,
            text="Reset Password",
            font=theme.SUBTITLE_FONT,
            text_color=theme.TEXT
        ).pack(pady=(25, 5))

        ctk.CTkLabel(
            self,
            text=f"for {username}",
            font=theme.BODY_FONT,
            text_color=theme.TEXT_LIGHT
        ).pack(pady=(0, 20))

        # ---------------- New Password ----------------

        ctk.CTkLabel(
            self,
            text="New Password",
            font=theme.BODY_FONT,
            text_color=theme.TEXT
        ).pack(anchor="w", padx=30)

        self.new_password = ctk.CTkEntry(
            self,
            width=300,
            height=38,
            corner_radius=10,
            show="*"
        )

        self.new_password.pack(pady=(4, 12))

        # ---------------- Confirm Password ----------------

        ctk.CTkLabel(
            self,
            text="Confirm Password",
            font=theme.BODY_FONT,
            text_color=theme.TEXT
        ).pack(anchor="w", padx=30)

        self.confirm_password = ctk.CTkEntry(
            self,
            width=300,
            height=38,
            corner_radius=10,
            show="*"
        )

        self.confirm_password.pack(pady=(4, 12))

        # ---------------- Buttons ----------------

        buttons = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        buttons.pack(pady=(15, 25))

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

    # ==================================================

    def save(self):

        new_password = self.new_password.get()
        confirm_password = self.confirm_password.get()

        if not new_password or not confirm_password:
            show_error(self, "Both fields are required.")
            return

        if len(new_password) < 6:
            show_error(self, "Password must be at least 6 characters.")
            return

        if new_password != confirm_password:
            show_error(self, "Passwords do not match.")
            return

        UserService.reset_password(
            self.user_id,
            new_password
        )

        if self.refresh_callback:
            self.refresh_callback()

        parent = self.master

        self.destroy()

        show_success(parent, "Password reset successfully.")