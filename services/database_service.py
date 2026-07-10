from database.db import *

class DatabaseService:

    @staticmethod
    def save(
        agent,
        user_input,
        response,
        execution_time=None,
        status="SUCCESS",
    ):

        save_interaction(
            agent,
            user_input,
            response,
            execution_time,
            status,
        )

    @staticmethod
    def history():

        return get_history()

    @staticmethod
    def total_reports():

        return get_total_reports()

    @staticmethod
    def total_medications():

        return get_total_medications()

    @staticmethod
    def success_count():

        return get_success_count()

    @staticmethod
    def failed_count():

        return get_failed_count()

    @staticmethod
    def average_runtime():

        return get_average_runtime()

    @staticmethod
    def latest_activity():

        return get_latest_activity()