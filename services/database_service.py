from database.db import (
    save_interaction,
    get_history,
)


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
            agent=agent,
            user_input=user_input,
            response=response,
            execution_time=execution_time,
            status=status,
        )

    @staticmethod
    def history():

        return get_history()