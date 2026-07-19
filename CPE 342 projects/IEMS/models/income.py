from dataclasses import dataclass
from datetime import date


@dataclass
class Income:
    """
    Represents an income transaction.
    """

    id: int | None = None
    category: str = ""
    amount: float = 0.0
    description: str = ""
    transaction_date: date | None = None
    created_by: int | None = None