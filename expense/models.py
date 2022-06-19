from django.db import models


class ExpenseSourceType:
    BUY_GOODS = 1
    TRAVEL = 2
    FOOD = 3
    RENT = 4
    BILL = 5
    EMI = 6
    MOVIE = 7
    TO_FAMILY_FRIENDS = 8
    OTHER = 9


class Expense(models.Model):
    EXPENSE_SOURCE_TYPE_CHOICES = (
        (ExpenseSourceType.BUY_GOODS, "Buy Goods"),
        (ExpenseSourceType.TRAVEL, "Travel"),
        (ExpenseSourceType.FOOD, "Food"),
        (ExpenseSourceType.RENT, "Rent"),
        (ExpenseSourceType.BILL, "Bill Payment"),
        (ExpenseSourceType.EMI, "EMI Repayment"),
        (ExpenseSourceType.MOVIE, "Movie"),
        (ExpenseSourceType.TO_FAMILY_FRIENDS, "Family or Friends"),
        (ExpenseSourceType.OTHER, "Others")
    )
    total_expense = models.IntegerField(blank=True, null=True)
    source = models.IntegerField(choices=EXPENSE_SOURCE_TYPE_CHOICES, blank=True, null=True)
    source_other = models.CharField(max_length=255, blank=True, null=True)