from django.db import models

# Create your models here.

NULLABLE = {'blank': True, 'null': True}


class Student(models.Model):
    first_name = models.CharField(max_length=100, verbose_name='Имя')
    last_name = models.CharField(max_length=100, verbose_name='Фамилия')
    avatar = models.ImageField(upload_to='students/', verbose_name='Avatar', **NULLABLE)

    is_active = models.BooleanField(default=True, verbose_name='учится')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'
        ordering = ('last_name',)
