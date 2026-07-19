import bcrypt

from database.connection import get_connection
from utils.logger import get_logger

logger = get_logger(__name__)


def seed():
    """
    Create the default administrator account.
    """

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT id FROM users WHERE username = ?",
        ("admin",)
    )

    if cursor.fetchone():

        logger.info("Administrator already exists.")

        conn.close()
        return

    password_hash = bcrypt.hashpw(
        "admin123".encode("utf-8"),
        bcrypt.gensalt()
    ).decode("utf-8")

    cursor.execute(
        """
        INSERT INTO users
        (
            username,
            password_hash,
            full_name,
            role,
            is_active
        )
        VALUES (?, ?, ?, ?, ?)
        """,
        (
            "admin",
            password_hash,
            "System Administrator",
            "Admin",
            1
        )
    )

    conn.commit()

    logger.info("Default administrator created.")

    conn.close()