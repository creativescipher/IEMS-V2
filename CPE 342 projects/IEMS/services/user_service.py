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