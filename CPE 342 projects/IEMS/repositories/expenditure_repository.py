from database.connection import get_connection


class ExpenditureRepository:

    @staticmethod
    def get_all():

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT
                expenditure.id,
                categories.name,
                expenditure.amount,
                expenditure.description,
                expenditure.transaction_date
            FROM expenditure
            JOIN categories
                ON expenditure.category_id = categories.id
            ORDER BY expenditure.transaction_date DESC
        """)

        rows = cursor.fetchall()

        conn.close()

        return rows

    @staticmethod
    def add(
        category_id,
        amount,
        description,
        transaction_date,
        created_by
    ):

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO expenditure
            (
                category_id,
                amount,
                description,
                transaction_date,
                created_by
            )
            VALUES
            (?, ?, ?, ?, ?)
            """,
            (
                category_id,
                amount,
                description,
                transaction_date,
                created_by
            )
        )

        conn.commit()
        conn.close()

    @staticmethod
    def delete(expenditure_id):

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "DELETE FROM expenditure WHERE id=?",
            (expenditure_id,)
        )

        conn.commit()
        conn.close()

    @staticmethod
    def get_total():

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT COALESCE(SUM(amount), 0) AS total FROM expenditure"
        )

        total = cursor.fetchone()["total"]

        conn.close()

        return total