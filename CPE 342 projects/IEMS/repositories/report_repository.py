from database.connection import get_connection


class ReportRepository:

    @staticmethod
    def get_summary():

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT COALESCE(SUM(amount), 0) AS total FROM income"
        )
        total_income = cursor.fetchone()["total"]

        cursor.execute(
            "SELECT COALESCE(SUM(amount), 0) AS total FROM expenditure"
        )
        total_expenditure = cursor.fetchone()["total"]

        cursor.execute(
            "SELECT COUNT(*) AS total FROM income"
        )
        income_count = cursor.fetchone()["total"]

        cursor.execute(
            "SELECT COUNT(*) AS total FROM expenditure"
        )
        expenditure_count = cursor.fetchone()["total"]

        conn.close()

        return {
            "total_income": total_income,
            "total_expenditure": total_expenditure,
            "balance": total_income - total_expenditure,
            "income_count": income_count,
            "expenditure_count": expenditure_count
        }