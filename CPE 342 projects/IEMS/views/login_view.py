import customtkinter as ctk

from config import theme
from services.auth_service import AuthService


class LoginView(ctk.CTk):

    def __init__(self):

        super().__init__()

        theme.set_mode(theme.current_mode())
        ctk.set_default_color_theme("blue")

        self.title("Income & Expenditure Management System")
        self.geometry("500x480")
        self.resizable(False, False)
        self.configure(fg_color=theme.BACKGROUND)

        self.build_ui()

        self.bind("<Return>", lambda event: self.login())

    # ==================================================

    def build_ui(self):

        card = ctk.CTkFrame(
            self,
            fg_color=theme.CARD,
            corner_radius=20,
            border_width=1,
            border_color=theme.BORDER,
            width=380
        )

        card.pack(
            expand=True,
            padx=40,
            pady=40
        )

        # ---------------- Logo ----------------

        logo = ctk.CTkFrame(
            card,
            width=64,
            height=64,
            corner_radius=16,
            fg_color=theme.PRIMARY
        )

        logo.pack(pady=(40, 15))
        logo.pack_propagate(False)

        ctk.CTkLabel(
            logo,
            text="IEMS",
            font=("Segoe UI Semibold", 14),
            text_color="white"
        ).pack(expand=True)

        # ---------------- Title ----------------

        ctk.CTkLabel(
            card,
            text="Income & Expenditure\nManagement System",
            font=theme.SUBTITLE_FONT,
            text_color=theme.TEXT,
            justify="center"
        ).pack(pady=(0, 5))

        ctk.CTkLabel(
            card,
            text="Sign in to continue",
            font=theme.BODY_FONT,
            text_color=theme.TEXT_LIGHT
        ).pack(pady=(0, 25))

        # ---------------- Fields ----------------

        self.username = ctk.CTkEntry(
            card,
            width=300,
            height=42,
            corner_radius=10,
            placeholder_text="Username"
        )

        self.username.pack(pady=8, padx=20)

        self.password = ctk.CTkEntry(
            card,
            width=300,
            height=42,
            corner_radius=10,
            placeholder_text="Password",
            show="*"
        )

        self.password.pack(pady=8, padx=20)

        # ---------------- Status ----------------

        self.status = ctk.CTkLabel(
            card,
            text="",
            font=theme.SMALL_FONT,
            text_color=theme.DANGER
        )

        self.status.pack(pady=(10, 0))

        # ---------------- Button ----------------

        self.login_button = ctk.CTkButton(
            card,
            text="Login",
            width=300,
            height=44,
            corner_radius=10,
            fg_color=theme.PRIMARY,
            hover_color=theme.PRIMARY_HOVER,
            font=theme.BODY_FONT,
            command=self.login
        )

        self.login_button.pack(pady=(15, 40))

    # ==================================================

    def login(self):

        username = self.username.get().strip()
        password = self.password.get()

        self.status.configure(
            text="",
            text_color=theme.DANGER
        )

        if not username or not password:

            self.status.configure(
                text="Please enter your username and password."
            )

            return

        self.login_button.configure(state="disabled")

        if AuthService.login(username, password):

            self.status.configure(
                text=f"Welcome, {username}! Signing you in...",
                text_color=theme.SUCCESS
            )

            self.after(700, self.open_main)

        else:

            self.status.configure(
                text="Invalid username or password."
            )

            self.login_button.configure(state="normal")

    # ==================================================

    def open_main(self):

        from views.main_shell import MainShell

        self.withdraw()

        shell = MainShell()
        shell.mainloop()

        self.destroy()