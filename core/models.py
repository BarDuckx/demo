from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    fio = models.CharField(max_length=255, verbose_name='ФИО')
    phone = models.CharField(max_length=20, verbose_name='Телефон')


class Application(models.Model):
    STATUS_CHOICES = (
        ('new', 'Новая'),
        ('learning', 'Идет обучение'),
        ('completed', 'Обучение завершено'),
    )
    COURSE_CHOICES = (
        ('Основы алгоритмизации и программирования', 'Основы алгоритмизации и программирования'),
        ('Основы веб-дизайна', 'Основы веб-дизайна'),
        ('Основы проектирования баз данных', 'Основы проектирования баз данных'),
    )
    PAYMENT_CHOICES = (
        ('cash', 'Наличными'),
        ('transfer', 'Переводом по номеру телефона'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='applications')
    course_name = models.CharField(max_length=100, choices=COURSE_CHOICES, verbose_name='Курс')
    start_date = models.CharField(max_length=10, verbose_name='Дата начала')
    payment_method = models.CharField(max_length=20, choices=PAYMENT_CHOICES, verbose_name='Способ оплаты')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new', verbose_name='Статус')
    feedback = models.TextField(blank=True, null=True, verbose_name='Отзыв')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
