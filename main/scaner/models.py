from django.db import models
from django.urls import reverse


class Scan(models.Model):
    code = models.CharField(max_length=150, verbose_name="Код")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.code

    #def get_absolute_url(self):
    #    return reverse('scan', kwargs={"slug": self.slug})

    class Meta:
        verbose_name = 'Скан'
        verbose_name_plural = 'Сканы'
