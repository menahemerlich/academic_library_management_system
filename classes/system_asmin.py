from classes import library

class SistemAdmin:
    total_transactions:int = 0
    @classmethod
    def update_transactions_count(cls, amount: int = 1) -> None:
        cls.total_transactions += amount

    @classmethod
    def report_stats(cls) -> None:
        print(library.Library.max_borrow_days, cls.total_transactions)








