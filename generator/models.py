from django.db import models

# Create your models here.

class Code(models.Model):
    code = models.CharField(max_length=8, unique=True, verbose_name='Код')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    quantity = models.PositiveSmallIntegerField(default=0,  verbose_name='Сколько раз активирован')
    active = models.BooleanField(verbose_name='Активность', default=False)