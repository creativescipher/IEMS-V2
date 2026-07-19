from repositories.audit_repository import AuditRepository
from repositories.user_repository import UserRepository
from services.password_service import PasswordService
from services.session import Session
from utils.logger import get_logger

logger = get_logger(__name__)


class AuthService:

    @staticmethod
    def login(username, password):

        user = UserRepository.get_by_username(username)

        if user is None:
            logger.warning("Unknown username.")
            return False

        if not user["is_active"]:
            logger.warning("Inactive account.")
            return False

        if not PasswordService.verify_password(
            password,
            user["password_hash"]
        ):
            logger.warning("Invalid password.")
            return False

        Session.login(user)

        AuditRepository.log(
            user["id"],
            "LOGIN"
        )

        logger.info(f"{username} logged in.")

        return True

    @staticmethod
    def logout():

        if Session.current_user:

            AuditRepository.log(
                Session.current_user["id"],
                "LOGOUT"
            )

            logger.info(
                f"{Session.current_user['username']} logged out."
            )

        Session.logout()