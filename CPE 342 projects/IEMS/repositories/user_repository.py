from database.connection import get_connection
from utils.logger import get_logger

logger = get_logger(__name__)


class UserRepository:
    """
    Handles all database operations related to users.
    """

    @staticmethod
    def get_by_username(username: str):
        """
        Return a user by username.
        """

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT *
            FROM users
            WHERE username = ?
            """,
            (username,)
        )

        user = cursor.fetchone()

        conn.close()

        return user

    @staticmethod
    def get_by_id(user_id: int):
        """
        Return a user by ID.
        """

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT *
            FROM users
            WHERE id = ?
            """,
            (user_id,)
        )

        user = cursor.fetchone()

        conn.close()

        return user