from utils.logger import setup_logging
from views.login_view import LoginView


def main():

    setup_logging()

    app = LoginView()

    app.mainloop()


if __name__ == "__main__":
    main()