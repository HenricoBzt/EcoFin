from django.db import models
from django.conf import settings
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=45)
    userfk = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Expense(models.Model):
    title = models.CharField(max_length=50,blank=True,null=True)
    describe = models.CharField(max_length=200)
    value = models.FloatField(default=0.00)
    date = models.DateField()

    status =(
        ('Pendente', 'Pendente'),
        ('Atrasado', 'Atrasado'),
        ('Pago','Pago')
    )

    status_choice = models.CharField(max_length=20,choices=status,default='Pendente')
    categoryfk = models.ForeignKey(Category, on_delete=models.CASCADE)
    userfk =  models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,blank=False,null=False,default=False)

    def __str__(self):
        return f'{self.describe} - {self.value}'

