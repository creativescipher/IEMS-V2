from database.connection import get_connection


class CategoryRepository:

    @staticmethod
    def get_income_categories():

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT id, name
            FROM categories
            WHERE type='Income'
            ORDER BY name
            """
        )

        rows = cursor.fetchall()

        conn.close()

        return rows

    @staticmethod
    def get_expenditure_categories():

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT id, name
            FROM categories
            WHERE type='Expenditure'
            ORDER BY name
            """
        )

        rows = cursor.fetchall()

        conn.close()

        return rows