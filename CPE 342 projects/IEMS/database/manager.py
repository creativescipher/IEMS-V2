from database.connection import check_connection
from database.schema import initialize_database

from database.seeders import (
    admin,
    categories,
    settings,
    version
)

from utils.logger import get_logger

logger = get_logger(__name__)


class DatabaseManager:
    """
    Handles all database initialization tasks.
    """

    @staticmethod
    def initialize():
        """
        Initialize the application's database.
        """

        logger.info("Initializing database...")

        if not check_connection():
            raise RuntimeError("Unable to connect to the database.")

        initialize_database()

        admin.seed()
        categories.seed()
        settings.seed()
        version.seed()

        logger.info("Database initialization completed successfully.")