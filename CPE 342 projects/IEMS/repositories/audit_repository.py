from database.connection import get_connection


class AuditRepository:

    @staticmethod
    def log(user_id, action, table_name=None, record_id=None, details=None):

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO audit_logs
            (
                user_id,
                action,
                table_name,
                record_id,
                details
            )
            VALUES (?, ?, ?, ?, ?)
            """,
            (
                user_id,
                action,
                table_name,
                record_id,
                details
            )
        )

        conn.commit()
        conn.close()