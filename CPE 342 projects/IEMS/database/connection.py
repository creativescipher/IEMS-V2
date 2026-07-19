import sqlite3

from config.settings import DB_PATH
from utils.logger import get_logger

logger = get_logger(__name__)


def get_connection():
    """
    Create and return a SQLite database connection.
    """

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def close_connection(conn):
    """
    Safely close a database connection.
    """

    if conn:
        conn.close()


def check_connection():
    """
    Verify that the SQLite database is accessible.
    """

    conn = None

    try:
        conn = get_connection()
        logger.info("Database connection successful.")
        return True

    except sqlite3.Error as error:
        logger.exception(f"Database connection failed: {error}")
        return False

    finally:
        if conn:
            close_connection(conn)