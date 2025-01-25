from django.db import models
from django.conf import settings


class Recipe(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    description = models.TextField(blank=True, null=True)
    time = models.DateTimeField(auto_now=False, auto_now_add=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    link = models.CharField(max_length=250, blank=True)

    def __str__(self):
        return self.title
