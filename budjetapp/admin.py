# books/admin.py
from django.contrib import admin
from .models import User,Category,Income,Expense,Budget

admin.site.register(User)
admin.site.register(Category)
admin.site.register(Income)
admin.site.register(Expense)
admin.site.register(Budget)

