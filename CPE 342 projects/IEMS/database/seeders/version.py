from database.connection import get_connection
from utils.logger import get_logger

logger = get_logger(__name__)


def seed():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM schema_version")

    count = cursor.fetchone()[0]

    if count == 0:

        cursor.execute(
            "INSERT INTO schema_version(version) VALUES (1)"
        )

        conn.commit()

        logger.info("Schema version initialized.")

    conn.close()