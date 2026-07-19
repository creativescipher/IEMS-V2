from database.connection import get_connection


class DashboardRepository:

    @staticmethod
    def total_income():
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT IFNULL(SUM(amount), 0)
            FROM income
        """)

        value = cursor.fetchone()[0]

        conn.close()

        return value

    @staticmethod
    def total_expenditure():
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT IFNULL(SUM(amount), 0)
            FROM expenditure
        """)

        value = cursor.fetchone()[0]

        conn.close()

        return value