from django.db import models


class Client(models.Model):
    """ CRM base client model """

    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=256)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
