from repositories.report_repository import ReportRepository


class ReportService:

    @staticmethod
    def get_summary():

        return ReportRepository.get_summary()