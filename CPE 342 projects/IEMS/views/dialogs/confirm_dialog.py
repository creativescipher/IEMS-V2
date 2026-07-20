import customtkinter as ctk

from config import theme


class ConfirmDialog(ctk.CTkToplevel):

    def __init__(self, parent, title, message, on_confirm):

        super().__init__(parent)

        self.on_confirm = on_confirm

        self.title(title)
        self.geometry("360x220")
        self.resizable(False, False)
        self.configure(fg_color=theme.BACKGROUND)

        self.grab_set()

        ctk.CTkLabel(
            self,
            text=title,
            font=theme.SUBTITLE_FONT,
            text_color=theme.TEXT
        ).pack(pady=(30, 10))

        ctk.CTkLabel(
            self,
            text=message,
            font=theme.BODY_FONT,
            text_color=theme.TEXT_LIGHT,
            wraplength=300,
            justify="center"
        ).pack(pady=(0, 25), padx=20)

        buttons = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        buttons.pack(pady=10)

        ctk.CTkButton(
            buttons,
            text="Confirm",
            width=130,
            height=40,
            corner_radius=10,
            fg_color=theme.DANGER,
            hover_color="#DC2626",
            font=theme.BODY_FONT,
            command=self.confirm
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

    def confirm(self):
        self.destroy()
        self.on_confirm()