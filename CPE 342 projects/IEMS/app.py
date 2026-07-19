from utils.logger import setup_logging
from database.schema import initialize_database
from database.seeders import admin, categories, settings, version
from views.login_view import LoginView


def bootstrap_database():
    """
    Ensures the database, tables, and default data exist.
    Safe to run on every launch — each step checks for
    existing data before inserting anything.
    """
    initialize_database()
    admin.seed()
    categories.seed()
    settings.seed()
    version.seed()


def main():

    setup_logging()
    bootstrap_database()

    app = LoginView()
    app.mainloop()


if __name__ == "__main__":
    main()