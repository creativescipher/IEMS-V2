from repositories.expenditure_repository import ExpenditureRepository


class ExpenditureService:

    @staticmethod
    def get_all():

        return ExpenditureRepository.get_all()

    @staticmethod
    def add(
        category_id,
        amount,
        description,
        transaction_date,
        created_by
    ):

        ExpenditureRepository.add(
            category_id,
            amount,
            description,
            transaction_date,
            created_by
        )

    @staticmethod
    def delete(expenditure_id):

        ExpenditureRepository.delete(expenditure_id)

    @staticmethod
    def get_total():

        return ExpenditureRepository.get_total()