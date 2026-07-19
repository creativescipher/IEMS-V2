from repositories.income_repository import IncomeRepository


class IncomeService:

    @staticmethod
    def get_all():

        return IncomeRepository.get_all()

    @staticmethod
    def add(
        category_id,
        amount,
        description,
        transaction_date,
        created_by
    ):

        IncomeRepository.add(
            category_id,
            amount,
            description,
            transaction_date,
            created_by
        )

    @staticmethod
    def delete(income_id):

        IncomeRepository.delete(income_id)

    @staticmethod
    def get_total():

        return IncomeRepository.get_total()