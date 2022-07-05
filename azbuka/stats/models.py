from django.db import models


# Create your models here.
class Couch(models.Model):
    name = models.CharField(max_length=512)
    articul = models.IntegerField()
    item_id = models.IntegerField()
    full_price = models.IntegerField(blank=True, null=True)
    sale_price = models.IntegerField()
    status = models.CharField(max_length=128)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = "Диван"
        verbose_name_plural = "Диваны"
