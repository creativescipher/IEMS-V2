ROLE_PERMISSIONS = {

    "Admin": {
        "users": True,
        "income": True,
        "expenditure": True,
        "reports": True,
        "settings": True
    },

    "Accountant": {
        "users": False,
        "income": True,
        "expenditure": True,
        "reports": True,
        "settings": False
    },

    "Manager": {
        "users": False,
        "income": False,
        "expenditure": False,
        "reports": True,
        "settings": False
    }

}