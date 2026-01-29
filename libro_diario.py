class DailyLedger:
    INCOME = "ingreso"
    EXPENSE = "egreso"

    def __init__(self):
        self.transactions = []

    def add_transaction(self, date: str, description: str, amount: float, transaction_type: str) -> None:
        if amount <= 0:
            raise ValueError("El monto debe ser mayor que 0.")
        if transaction_type not in [self.INCOME, self.EXPENSE]:
            raise ValueError("El tipo de transacción debe ser 'ingreso' o 'egreso'.")
        
        self.transactions.append({
            "date": date,
            "description": description,
            "amount": amount,
            "type": transaction_type
        })

    def get_summary(self) -> dict:
        income_total = sum(t["amount"] for t in self.transactions if t["type"] == self.INCOME)
        expense_total = sum(t["amount"] for t in self.transactions if t["type"] == self.EXPENSE)
        
        return {
            "total_ingresos": income_total,
            "total_egresos": expense_total
        }

    def print_summary(self) -> str:
        summary = self.get_summary()
        return f"Total ingresos: {summary['total_ingresos']} Total egresos: {summary['total_egresos']}"
