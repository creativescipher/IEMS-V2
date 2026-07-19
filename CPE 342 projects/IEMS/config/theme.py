import customtkinter as ctk

APP_TITLE = "Income & Expenditure Management System"

WINDOW_WIDTH = 1366
WINDOW_HEIGHT = 768

# =====================================================
# COLORS  (light, dark)
# =====================================================

# Main Brand
PRIMARY = ("#5B5FEF", "#7C7FF5")
PRIMARY_HOVER = ("#4B4ED9", "#6669E0")

# Status
SUCCESS = ("#22C55E", "#34D399")
WARNING = ("#F59E0B", "#FBBF24")
DANGER = ("#EF4444", "#F87171")

# Layout
BACKGROUND = ("#EEF2F7", "#0F1224")
SIDEBAR = ("#1F2340", "#12142A")
HEADER = ("#FFFFFF", "#181B34")
CARD = ("#FFFFFF", "#1E2140")

# Text
TEXT = ("#111827", "#F1F5F9")
TEXT_LIGHT = ("#6B7280", "#94A3B8")

# Borders
BORDER = ("#E5E7EB", "#2A2E4F")

# Sidebar
SIDEBAR_TEXT = ("#E5E7EB", "#CBD5E1")
SIDEBAR_ACTIVE = ("#5B5FEF", "#7C7FF5")
SIDEBAR_HOVER = ("#2A3055", "#242850")

# =====================================================
# FONTS
# =====================================================

TITLE_FONT = ("Segoe UI Semibold", 28)
SUBTITLE_FONT = ("Segoe UI Semibold", 20)
BODY_FONT = ("Segoe UI", 14)
SMALL_FONT = ("Segoe UI", 12)
CARD_TITLE_FONT = ("Segoe UI Semibold", 15)
CARD_VALUE_FONT = ("Segoe UI Bold", 30)

# =====================================================
# UI
# =====================================================

CARD_RADIUS = 18
BUTTON_RADIUS = 10
BUTTON_HEIGHT = 40
ENTRY_HEIGHT = 38

PAGE_PADDING = 25
CARD_PADDING = 20

# =====================================================
# APPEARANCE MODE
# =====================================================

def set_mode(mode: str):
    """mode: 'light', 'dark', or 'system'"""
    ctk.set_appearance_mode(mode)


def current_mode() -> str:
    return ctk.get_appearance_mode()


def toggle_mode() -> str:
    new_mode = "Light" if current_mode() == "Dark" else "Dark"
    set_mode(new_mode)
    return new_mode