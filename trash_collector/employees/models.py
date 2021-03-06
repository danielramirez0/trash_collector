from django.db import models

# Create your models here.


class Employee(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey('accounts.User', blank=True, null=True, on_delete=models.CASCADE)
    zip_code = models.CharField(max_length=5)

    def __str__(self) -> str:
        return self.name
