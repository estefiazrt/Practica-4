class DailyLedger:
    def __init__(self):
        self.transactions = []

    def add_transaction(self, date, description, amount, transaction_type):
        self.transactions.append({
            "date": date,
            "description": description,
            "amount": amount,
            "type": transaction_type
        })

    def get_summary(self):
        income = 0
        expense = 0
        for t in self.transactions:
            if t["type"] == "ingreso":
                income += t["amount"]
            else:
                expense += t["amount"]
        return "Total ingresos: " + str(income) + " Total egresos: " + str(expense)
