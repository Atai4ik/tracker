from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models

SOURCE = (
    ('Salary', 'Salary'),
    ('Deposit', 'Deposit'),
    ('Business', 'Business'),
)


class Transactions(models.Model):
    description = models.CharField(max_length=255)
    money = models.DecimalField(max_digits=20, default=None, decimal_places=2)
    currency = models.CharField(max_length=10)
    date = models.DateTimeField(auto_now_add=True)


class UserIncome(models.Model):
    user = models.ForeignKey(User)
    amount = models.DecimalField(max_digits=20, default=None, decimal_places=2)
    source = models.CharField(max_length=255, choices=SOURCE)
    comment = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def update_balance(self):
        self.user.balance += self.amount
        Transactions.objects.create(money=self.amount, user=self.user)
        self.user.save()



