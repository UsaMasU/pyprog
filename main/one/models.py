from django.db import models

class Request(models.Model):
    title = models.CharField(verbose_name='Request', max_length=30)
    price = models.CharField(verbose_name='Price', max_length=10)

    def __str__(self):
        return str(self.title)

class Valve(models.Model):
    title = models.CharField(verbose_name='Valve', max_length=30)
    description = models.CharField(verbose_name='Description', max_length=250, null=True)
    quantity = models.DecimalField(max_digits=6, decimal_places=0, verbose_name="quantity")
    request = models.ForeignKey(Request, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return str(self.title)

class Motor(models.Model):
    title = models.CharField(verbose_name='Motor', max_length=30)
    quantity = models.DecimalField(max_digits=6, decimal_places=0, verbose_name="quantity")
    request = models.ForeignKey(Request, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return str(self.title)

class OtherObject(models.Model):
    title = models.CharField(verbose_name='Object', max_length=30)
    code = models.DecimalField(decimal_places=3, max_digits=6)
    quantity = models.DecimalField(max_digits=6, decimal_places=0, verbose_name="quantity")
    request = models.ManyToManyField(Request, through='OtherObjectsInRequest', verbose_name="Object")

    def __str__(self):
        return str(self.title)

class OtherObjectsInRequest(models.Model):
    request = models.ForeignKey(Request, on_delete=models.CASCADE)
    other_object = models.ForeignKey(OtherObject, on_delete=models.CASCADE)
    quantity = models.DecimalField(verbose_name='quantity', max_digits=10, decimal_places=0)

    def __str__(self):
        return '{0}_{1}'.format(self.request, self.other_object)