from django.db import models

# Create your models here.
class Produto(models.Model):
    produto = models.CharField(max_length=200)
    preco = models.FloatField()


    def __str__(self):
        return self.name
    
