from django.db import models


class Contact(models.Model):
    name = models.CharField(unique=True, max_length=100)
    adress = models.CharField(max_length=300, blank=True)

    def __str__(self):
        return self.name


class Phone(models.Model):
    contact = models.ForeignKey(Contact, related_name='phones')
    number = models.CharField(unique=True, max_length=30)

    def __str__(self):
        return self.number
