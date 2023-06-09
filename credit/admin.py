from django.contrib import admin

from .models import Client, Account, Credit

admin.site.register(Client)
admin.site.register(Account)


class CreditAdmin(admin.ModelAdmin):
    list_display = ['account', 'sum', 'date']


admin.site.register(Credit, CreditAdmin)


