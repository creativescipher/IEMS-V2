from repositories.dashboard_repository import DashboardRepository


class DashboardService:

    @staticmethod
    def total_income():
        return DashboardRepository.total_income()

    @staticmethod
    def total_expenditure():
        return DashboardRepository.total_expenditure()

    @staticmethod
    def balance():
        return (
            DashboardService.total_income()
            - DashboardService.total_expenditure()
        )