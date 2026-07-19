from dataclasses import dataclass
from datetime import date


@dataclass
class Expenditure:
    """
    Represents an expenditure transaction.
    """

    id: int | None = None
    category: str = ""
    amount: float = 0.0
    description: str = ""
    transaction_date: date | None = None
    created_by: int | None = None