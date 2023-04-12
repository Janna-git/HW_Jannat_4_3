import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'banking.settings')
django_asgi_app = get_asgi_application()

import random

from credit.models import *

def account_number():
    return random.randint(10**15*1, 10**16)

client1 = Client.objects.create(name='Бердиев Н.Д.', birth_year=1994, work_place='Codify')
client2 = Client.objects.create(name='Шаякунова Ж.К.', birth_year=1988, work_place='Импекс')


account1 = Account.objects.create(number=account_number(), account_type='2', client=client1)
account2 = Account.objects.create(number=account_number(), client=client1)
account3 = Account.objects.create(number=account_number(), account_type='5', client=client2)
account4 = Account.objects.create(number=account_number(), account_type='3', client=client2)


credit1 = Credit.objects.create(sum=20_000, account=account1)
credit2 = Credit.objects.create(sum=10_000, account=account2)
credit3 = Credit.objects.create(sum=25_000, account=account3)
credit4 = Credit.objects.create(sum=30_000, account=account4)

