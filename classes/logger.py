from datetime import datetime

class Logger:

    @staticmethod
    def log_action(action_type: str, details: str) -> None:
        print(f"{datetime.now().strftime("%d/%m/%Y %H:%M:%S")}: {action_type}, {details}")





