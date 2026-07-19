from dataclasses import dataclass


@dataclass
class User:
    """
    Represents a system user.
    """

    id: int | None = None
    username: str = ""
    password_hash: str = ""
    full_name: str = ""
    role: str = ""
    is_active: bool = True