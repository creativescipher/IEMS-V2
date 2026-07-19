from database.connection import get_connection


class UserRepository:

    @staticmethod
    def get_by_username(username):

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

    # ==================================================

    @staticmethod
    def username_exists(username):

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT id
            FROM users
            WHERE username = ?
            """,
            (username,)
        )

        exists = cursor.fetchone() is not None

        conn.close()

        return exists

    # ==================================================

    @staticmethod
    def get_all():

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT
                id,
                username,
                full_name,
                role,
                is_active,
                created_at
            FROM users
            ORDER BY username
        """)

        rows = cursor.fetchall()

        conn.close()

        return rows

    # ==================================================

    @staticmethod
    def add(
        username,
        password_hash,
        full_name,
        role
    ):

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO users
            (
                username,
                password_hash,
                full_name,
                role
            )
            VALUES
            (?, ?, ?, ?)
            """,
            (
                username,
                password_hash,
                full_name,
                role
            )
        )

        conn.commit()
        conn.close()

    # ==================================================

    @staticmethod
    def set_active(user_id, active):

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            UPDATE users
            SET is_active = ?
            WHERE id = ?
            """,
            (
                active,
                user_id
            )
        )

        conn.commit()
        conn.close()