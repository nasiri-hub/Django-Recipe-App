from django.contrib import admin
from django.db import models
from django.conf import settings


class Recipe(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField(blank=True, null=True)
    time = models.DateTimeField(auto_now=False, auto_now_add=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    link = models.CharField(max_length=250, blank=True)
    ingredient = models.ManyToManyField('Ingredient')

    def __str__(self):
        return self.title


class Ingredient(models.Model): 
    name = models.CharField(max_length=250)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Customer(models.Model):
    class Membership(models.TextChoices):
        GOLD = 'G', 'Gold'
        SILVER = 'S', 'Silver'
        BRONZE = 'B', 'Bronze'
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)
    phone = models.CharField(max_length=255)
    birth_date = models.DateField(null=True, blank=True)
    membership = models.CharField(
        choices=Membership.choices, max_length=1, default=Membership.BRONZE)

    class Meta:
        ordering = ['user__first_name', 'user__last_name']

    def __str__(self) -> str:
        return f'{self.user.first_name} {self.user.last_name}'

    @admin.display(ordering=['user__first_name'])
    def first_name(self):
        return self.user.first_name

    @admin.display(ordering=['user__last_name'])
    def last_name(self):
        return self.user.last_name