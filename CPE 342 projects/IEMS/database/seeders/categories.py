from database.connection import get_connection
from utils.logger import get_logger

logger = get_logger(__name__)


DEFAULT_CATEGORIES = [

    ("Product Sales", "Income"),
    ("Service Revenue", "Income"),
    ("Investment", "Income"),

    ("Salary", "Expenditure"),
    ("Utilities", "Expenditure"),
    ("Transportation", "Expenditure"),
    ("Maintenance", "Expenditure"),
]


def seed():

    conn = get_connection()
    cursor = conn.cursor()

    for name, category_type in DEFAULT_CATEGORIES:

        cursor.execute(
            """
            INSERT OR IGNORE INTO categories
            (name, type)
            VALUES (?, ?)
            """,
            (name, category_type)
        )

    conn.commit()

    logger.info("Default categories seeded.")

    conn.close()