import sys
from pathlib import Path

# ==========================================================
# APPLICATION INFORMATION
# ==========================================================

APP_NAME = "Income & Expenditure Management System"
APP_VERSION = "1.0.0"

# ==========================================================
# PROJECT PATHS
# ==========================================================

if getattr(sys, "frozen", False):

    # Running as a bundled exe — store data in AppData so it
    # survives restarts and isn't wiped with the temp extraction.
    BASE_DIR = Path.home() / "AppData" / "Local" / "IEMS"

else:

    # Running as a normal Python script during development.
    BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data"
LOGS_DIR = BASE_DIR / "logs"
EXPORTS_DIR = BASE_DIR / "exports"

DB_PATH = DATA_DIR / "iems.db"
LOG_FILE = LOGS_DIR / "app.log"

# ==========================================================
# CREATE REQUIRED DIRECTORIES
# ==========================================================

for directory in (DATA_DIR, LOGS_DIR, EXPORTS_DIR):
    directory.mkdir(parents=True, exist_ok=True)

# ==========================================================
# USER ROLES
# ==========================================================

ROLE_PERMISSIONS = {
    "Admin": [
        "manage_users",
        "manage_income",
        "manage_expenditure",
        "generate_reports",
        "export_reports",
        "manage_settings"
    ],
    "Accountant": [
        "manage_income",
        "manage_expenditure",
        "generate_reports",
        "export_reports"
    ],
    "Manager": [
        "generate_reports",
        "view_dashboard"
    ]
}

# ==========================================================
# UI SETTINGS
# ==========================================================

THEME = "dark"
COLOR_THEME = "blue"