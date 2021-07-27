
from django.db import models

# Create your models here.
class ModelQuote(models.Model):
    quote = models.TextField(max_length=2000000)
    penned_by = models.CharField(max_length=1000)

    def __str__(self):
        return self.quote