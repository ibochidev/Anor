from django.db import models


class Car(models.Model):
    name = models.CharField(max_length=64)
    color = models.CharField(max_length=64)
    year = models.CharField(max_length=16)
    image = models.ImageField(upload_to='media')

    def __str__(self):
        return f"{self.id} - {self.name}"

    class Meta:
        verbose_name = "Mashina"
        verbose_name_plural = "Mashinalar"
        ordering = ['-id']
