from django.utils import timezone
from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=20, null=False, blank=False)
    citizenship = models.CharField(max_length=20, default='Кыргызстан')
    birth_year = models.IntegerField()
    work_place = models.CharField(max_length=30, null=True, blank=True)
    update_date = models.DateField(default=timezone.now)

    class Meta:
        db_table = 'customers'
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

    def __str__(self):
        return self.name


class Account(models.Model):
    number = models.CharField(max_length=16, null=False, blank=False, unique=True)
    account_type = models.IntegerField(default=1, null=False)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)

    class Meta:
        db_table = 'accounts'
        verbose_name = 'Счет'
        verbose_name_plural = 'Счета'

    def __str__(self):
        return self.number


class Credit(models.Model):
    sum = models.IntegerField(null=False, blank=False)
    date = models.DateField(default=timezone.now)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)


    class Meta:
        db_table = 'loans'
        verbose_name = 'Кредит'
        verbose_name_plural = 'Кредиты'


    def __str__(self):
        return self.sum