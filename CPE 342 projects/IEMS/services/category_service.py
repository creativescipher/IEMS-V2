from repositories.category_repository import CategoryRepository


class CategoryService:

    @staticmethod
    def get_income_categories():

        return CategoryRepository.get_income_categories()

    @staticmethod
    def get_expenditure_categories():

        return CategoryRepository.get_expenditure_categories()