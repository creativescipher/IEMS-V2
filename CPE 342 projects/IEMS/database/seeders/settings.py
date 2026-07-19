from database.connection import get_connection
from utils.logger import get_logger

logger = get_logger(__name__)


DEFAULT_SETTINGS = [

    ("company_name", "Seven Up Bottling Company"),
    ("currency", "₦"),
    ("financial_year", "2026"),
    ("app_theme", "Light")
]


def seed():

    conn = get_connection()
    cursor = conn.cursor()

    for key, value in DEFAULT_SETTINGS:

        cursor.execute(
            """
            INSERT OR IGNORE INTO system_settings
            (
                setting_key,
                setting_value
            )
            VALUES (?, ?)
            """,
            (key, value)
        )

    conn.commit()

    logger.info("System settings seeded.")

    conn.close()