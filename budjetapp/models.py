from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=100, verbose_name='First Name')
    last_name = models.CharField(max_length=100, verbose_name='Last Name')
    email = models.EmailField(unique=True, verbose_name='Email')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Category Name')

    def __str__(self):
        return self.name


class Income(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='incomes')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='incomes')
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Amount')
    date = models.DateField(verbose_name='Date')

    def __str__(self):
        return f"Income: {self.amount} for {self.user}"


class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='expenses')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='expenses')
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Amount')
    date = models.DateField(verbose_name='Date')

    def __str__(self):
        return f"Expense: {self.amount} for {self.user}"


class Budget(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='budgets')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='budgets')
    limit = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Limit')
    period = models.CharField(max_length=50, verbose_name='Period')

    def __str__(self):
        return f"Budget: {self.limit} for {self.user} in {self.category}"

