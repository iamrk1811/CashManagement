from django.db import models


class EarningSourceType:
    SALARY = 1
    BUSINESS = 2
    OTHER = 3


class Earning(models.Model):
    EARNING_SOURCE_TYPE_CHOICES = (
        (EarningSourceType.SALARY, "Salary"),
        (EarningSourceType.BUSINESS, "Business"),
        (EarningSourceType.OTHER, "Others")
    )
    total_earning = models.IntegerField(blank=True, null=True)
    source = models.IntegerField(choices=EARNING_SOURCE_TYPE_CHOICES, blank=True, null=True)
    source_other = models.CharField(max_length=255, blank=True, null=True)
    datetime = models.DateTimeField(blank=True, null=True)
