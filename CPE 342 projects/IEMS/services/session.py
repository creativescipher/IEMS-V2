class Session:
    """
    Stores information about the currently logged-in user.
    """

    current_user = None

    @classmethod
    def login(cls, user):
        cls.current_user = user

    @classmethod
    def logout(cls):
        cls.current_user = None

    @classmethod
    def is_logged_in(cls):
        return cls.current_user is not None

    @classmethod
    def get_user(cls):
        return cls.current_user

    @classmethod
    def username(cls):
        return cls.current_user["username"] if cls.current_user else ""

    @classmethod
    def full_name(cls):
        return cls.current_user["full_name"] if cls.current_user else ""

    @classmethod
    def role(cls):
        return cls.current_user["role"] if cls.current_user else ""

    @classmethod
    def is_admin(cls):
        return cls.role() == "Admin"

    @classmethod
    def is_accountant(cls):
        return cls.role() == "Accountant"

    @classmethod
    def is_manager(cls):
        return cls.role() == "Manager"