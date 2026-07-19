from database.connection import get_connection


class IncomeRepository:

    @staticmethod
    def get_all():

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT
                income.id,
                categories.name,
                income.amount,
                income.description,
                income.transaction_date
            FROM income
            JOIN categories
                ON income.category_id = categories.id
            ORDER BY income.transaction_date DESC
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
            INSERT INTO income
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
    def delete(income_id):

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "DELETE FROM income WHERE id=?",
            (income_id,)
        )

        conn.commit()
        conn.close()

    @staticmethod
    def get_total():

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT COALESCE(SUM(amount), 0) AS total FROM income"
        )

        total = cursor.fetchone()["total"]

        conn.close()

        return total