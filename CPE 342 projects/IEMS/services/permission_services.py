from config.permissions import ROLE_PERMISSIONS
from services.session import Session


class PermissionService:

    @staticmethod
    def can(permission):

        role = Session.role()

        if role not in ROLE_PERMISSIONS:
            return False

        return ROLE_PERMISSIONS[role].get(permission, False)