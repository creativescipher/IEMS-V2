import tkinter as tk
import customtkinter as ctk

from config import theme


class Toast(ctk.CTkToplevel):
    """
    A centered, theme-matched notification card with an
    icon, title, subtitle, and action button — replaces
    native OS popups.
    """

    def __init__(
        self,
        parent,
        title,
        subtitle="",
        kind="success",
        button_text=None,
        duration=3500
    ):

        super().__init__(parent)

        self.overrideredirect(True)
        self.attributes("-topmost", True)

        is_success = (kind == "success")

        accent_color = theme.SUCCESS if is_success else theme.DANGER
        button_text = button_text or ("Continue" if is_success else "Go Back")

        # Resolve theme colors (they're (light, dark) tuples)
        mode_index = 1 if theme.current_mode() == "Dark" else 0
        card_bg = theme.CARD[mode_index] if isinstance(theme.CARD, tuple) else theme.CARD
        border_col = theme.BORDER[mode_index] if isinstance(theme.BORDER, tuple) else theme.BORDER
        icon_color = accent_color[mode_index] if isinstance(accent_color, tuple) else accent_color

        card = ctk.CTkFrame(
            self,
            fg_color=theme.CARD,
            corner_radius=16,
            border_width=1,
            border_color=theme.BORDER,
            width=300
        )

        card.pack(fill="both", expand=True)
        card.pack_propagate(False)

        # ---------------- Icon (circle + check / exclamation) ----------------

        canvas = tk.Canvas(
            card,
            width=64,
            height=64,
            bg=card_bg,
            highlightthickness=0
        )

        canvas.pack(pady=(28, 12))

        canvas.create_oval(
            4, 4, 60, 60,
            outline=icon_color,
            width=3
        )

        if is_success:

            canvas.create_line(
                18, 33, 28, 43,
                fill=icon_color,
                width=4,
                capstyle="round"
            )

            canvas.create_line(
                28, 43, 46, 21,
                fill=icon_color,
                width=4,
                capstyle="round"
            )

        else:

            canvas.create_line(
                32, 16, 32, 38,
                fill=icon_color,
                width=4,
                capstyle="round"
            )

            canvas.create_oval(
                29, 44, 35, 50,
                fill=icon_color,
                outline=icon_color
            )

        # ---------------- Title ----------------

        ctk.CTkLabel(
            card,
            text=title,
            font=theme.SUBTITLE_FONT,
            text_color=theme.TEXT
        ).pack(pady=(0, 4))

        # ---------------- Subtitle ----------------

        if subtitle:

            ctk.CTkLabel(
                card,
                text=subtitle,
                font=theme.SMALL_FONT,
                text_color=theme.TEXT_LIGHT,
                wraplength=250,
                justify="center"
            ).pack(pady=(0, 15))

        else:

            ctk.CTkLabel(card, text="", height=1).pack(pady=(0, 5))

        # ---------------- Button ----------------

        ctk.CTkButton(
            card,
            text=button_text,
            width=180,
            height=40,
            corner_radius=10,
            fg_color=accent_color,
            hover_color="#DC2626" if not is_success else "#16A34A",
            font=theme.BODY_FONT,
            command=self.destroy
        ).pack(pady=(0, 28))

        self.update_idletasks()

        parent_root = parent.winfo_toplevel()
        parent_root.update_idletasks()

        px = parent_root.winfo_rootx()
        py = parent_root.winfo_rooty()
        pw = parent_root.winfo_width()
        ph = parent_root.winfo_height()

        w = self.winfo_width()
        h = self.winfo_height()

        x = px + (pw - w) // 2
        y = py + (ph - h) // 2

        self.geometry(f"{w}x{h}+{x}+{y}")

        self.grab_set()

        self.after(duration, self._safe_destroy)

    def _safe_destroy(self):
        try:
            self.destroy()
        except Exception:
            pass


def show_success(parent, message, title="Successful!"):
    Toast(parent, title, message, kind="success")


def show_error(parent, message, title="Oops!"):
    Toast(parent, title, message, kind="error")