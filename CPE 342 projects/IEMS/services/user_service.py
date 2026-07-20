from repositories.user_repository import UserRepository
from services.password_service import PasswordService


class UserService:

    @staticmethod
    def get_all():
        return UserRepository.get_all()

    @staticmethod
    def add(
        username,
        password,
        full_name,
        role
    ):
        password_hash = PasswordService.hash_password(password)
        UserRepository.add(
            username,
            password_hash,
            full_name,
            role
        )

    @staticmethod
    def activate(user_id):
        UserRepository.set_active(
            user_id,
            1
        )

    @staticmethod
    def deactivate(user_id):
        UserRepository.set_active(
            user_id,
            0
        )

    # ==================================================
    # Admin resets someone else's password — no old
    # password required.
    # ==================================================

    @staticmethod
    def reset_password(user_id, new_password):
        password_hash = PasswordService.hash_password(new_password)
        UserRepository.update_password(user_id, password_hash)

    # ==================================================
    # A user changes their own password — must prove they
    # know the current one first.
    # ==================================================

    @staticmethod
    def change_password(user_id, current_password, new_password):

        user = UserRepository.get_by_id(user_id)

        if user is None:
            raise ValueError("User not found.")

        if not PasswordService.verify_password(
            current_password,
            user["password_hash"]
        ):
            raise ValueError("Current password is incorrect.")

        password_hash = PasswordService.hash_password(new_password)
        UserRepository.update_password(user_id, password_hash)