import customtkinter as ctk

from config import theme

from services.auth_service import AuthService

from views.widgets.sidebar import Sidebar
from views.widgets.header import Header

from views.pages.dashboard_page import DashboardPage
from views.pages.income_page import IncomePage
from views.pages.expenditure_page import ExpenditurePage
from views.pages.reports_page import ReportsPage
from views.pages.users_page import UsersPage
from views.pages.settings_page import SettingsPage


class MainShell(ctk.CTk):

    def __init__(self):

        super().__init__()

        self.title(theme.APP_TITLE)
        self.geometry(
            f"{theme.WINDOW_WIDTH}x{theme.WINDOW_HEIGHT}"
        )

        self.configure(
            fg_color=theme.BACKGROUND
        )

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(1, weight=1)

        # ---------------- Header ----------------

        self.header = Header(
            self,
            self.logout
        )

        self.header.grid(
            row=0,
            column=0,
            columnspan=2,
            sticky="ew"
        )

        # ---------------- Sidebar ----------------

        self.sidebar = Sidebar(
            self,
            self.show_page
        )

        self.sidebar.grid(
            row=1,
            column=0,
            sticky="ns"
        )

        # ---------------- Content ----------------

        self.content = ctk.CTkFrame(
            self,
            fg_color=theme.BACKGROUND
        )

        self.content.grid(
            row=1,
            column=1,
            sticky="nsew"
        )

        self.current_page = None

        self.show_page("dashboard")

    # =======================================

    def clear_page(self):

        if self.current_page:

            self.current_page.destroy()

    # =======================================

    def show_page(self, page):

        self.clear_page()

        pages = {

            "dashboard": DashboardPage,

            "income": IncomePage,

            "expenditure": ExpenditurePage,

            "reports": ReportsPage,

            "users": UsersPage,

            "settings": SettingsPage
        }

        page_class = pages.get(page)

        if page_class:

            self.current_page = page_class(
                self.content
            )

            self.current_page.pack(
                fill="both",
                expand=True
            )

    # =======================================

    def logout(self):

        AuthService.logout()

        self.destroy()

        from views.login_view import LoginView

        LoginView().mainloop()