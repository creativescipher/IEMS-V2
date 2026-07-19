from repositories.dashboard_repository import DashboardRepository


class DashboardService:

    @staticmethod
    def get_summary():

        return DashboardRepository.get_summary()