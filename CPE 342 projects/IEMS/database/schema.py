from pathlib import Path

from database.connection import get_connection
from utils.logger import get_logger

logger = get_logger(__name__)


def initialize_database():
    """
    Creates all database tables by executing schema.sql.
    Safe to run multiple times because the SQL uses
    CREATE TABLE IF NOT EXISTS.
    """

    schema_file = Path(__file__).parent / "schema.sql"

    if not schema_file.exists():
        raise FileNotFoundError(
            f"Schema file not found: {schema_file}"
        )

    conn = get_connection()

    try:
        cursor = conn.cursor()

        with open(schema_file, "r", encoding="utf-8") as file:
            cursor.executescript(file.read())

        conn.commit()

        logger.info("Database schema initialized successfully.")

    except Exception:
        conn.rollback()
        logger.exception("Failed to initialize database.")
        raise

    finally:
        conn.close()