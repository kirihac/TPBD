from django.core.management.base import BaseCommand
from budjetapp.models import User,Category,Income,Expense,Budget


class Command(BaseCommand):
    help = 'Show all authors and books'

    def handle(self, *args, **kwargs):
        users = User.objects.all()
        categorys = Category.objects.all()
        incomes = Income.objects.all()
        expenses = Expense.objects.all()
        budgets = Budget.objects.all()

        self.stdout.write("Users:")
        self.stdout.write("id: first_name, last_name, email")
        for user in users:
            self.stdout.write(f"{user.id}: {user.first_name}, {user.last_name}, {user.email}")

        self.stdout.write("Сategorys:")
        self.stdout.write("id: name")
        for category in categorys:
            self.stdout.write(f"{category.id}: {category.name}")

        self.stdout.write("Incomes:")
        self.stdout.write("id: user, category, amount, date")
        for income in incomes:
            self.stdout.write(f"{income.id}: {income.user}, {income.category}, {income.amount}, {income.date}")

        self.stdout.write("Expenses:")
        self.stdout.write("id: user, category, amount, date")
        for expense in expenses:
            self.stdout.write(f"{expense.id}: {expense.user}, {expense.category}, {expense.amount}, {expense.date}")

        self.stdout.write("Budgets:")
        self.stdout.write("id: user, category, limit, period")
        for budget in budgets:
            self.stdout.write(f"{budget.id}: {budget.user}, {budget.category}, {budget.limit}, {budget.period}")
