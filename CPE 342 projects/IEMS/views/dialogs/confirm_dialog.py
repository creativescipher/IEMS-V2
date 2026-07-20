import customtkinter as ctk

from config import theme


class ConfirmDialog(ctk.CTkToplevel):

    def __init__(self, parent, title, message, on_confirm):

        super().__init__(parent)

        self.on_confirm = on_confirm

        self.overrideredirect(True)
        self.attributes("-topmost", True)

        self.configure(fg_color=theme.BACKGROUND)

        card = ctk.CTkFrame(
            self,
            fg_color=theme.CARD,
            corner_radius=16,
            border_width=1,
            border_color=theme.BORDER,
            width=340
        )

        card.pack(fill="both", expand=True)
        card.pack_propagate(False)

        ctk.CTkLabel(
            card,
            text=title,
            font=theme.SUBTITLE_FONT,
            text_color=theme.TEXT
        ).pack(pady=(30, 10))

        ctk.CTkLabel(
            card,
            text=message,
            font=theme.BODY_FONT,
            text_color=theme.TEXT_LIGHT,
            wraplength=280,
            justify="center"
        ).pack(pady=(0, 25), padx=20)

        buttons = ctk.CTkFrame(
            card,
            fg_color="transparent"
        )

        buttons.pack(pady=(0, 30))

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

        w = 340
        h = 260

        parent_root = parent.winfo_toplevel()
        parent_root.update_idletasks()

        px = parent_root.winfo_rootx()
        py = parent_root.winfo_rooty()
        pw = parent_root.winfo_width()
        ph = parent_root.winfo_height()

        x = px + (pw - w) // 2
        y = py + (ph - h) // 2

        self.geometry(f"{w}x{h}+{x}+{y}")

        self.grab_set()

    # ==================================================

    def confirm(self):
        self.destroy()
        self.on_confirm()