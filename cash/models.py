from django.db import models
from earning.models import Earning
from expense.models import Expense

class CashActionType:
    CREDIT = 1
    DEBIT = 2


class Cash(models.Model):
    ACTION_CHOICES = (
        (CashActionType.CREDIT, "Credit"),
        (CashActionType.DEBIT, "Debit"),
    )
    total_cash = models.IntegerField(blank=True, null=True)
    action = models.IntegerField(choices=ACTION_CHOICES, blank=True, null=True)
    earning = models.ForeignKey(Earning, blank=True, null=True, default=None, on_delete=models.CASCADE)
    expense = models.ForeignKey(Expense, blank=True, null=True, default=None, on_delete=models.CASCADE)
    