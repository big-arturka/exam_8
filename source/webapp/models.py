from django.contrib.auth import get_user_model
from django.db import models

DEFAULT_CATEGORY = 'other'
CATEGORY_CHOICES = {
    (DEFAULT_CATEGORY, 'Разное'),
    ('food', "Еда"),
    ('tech', 'Бытовая техника'),
    ('tools', 'Инструменты')
}


RATING_CHOICES = {
    ('1', 'Плохо'),
    ('2', 'Удовлетворительно'),
    ('3', 'Нормально'),
    ('4', 'Хорошо'),
    ('5', 'Отлично')
}


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    category = models.CharField(max_length=40, verbose_name='Категория',
                                choices=CATEGORY_CHOICES, default=DEFAULT_CATEGORY)
    description = models.TextField(max_length=2000, null=True, blank=True, verbose_name='Описание')
    image = models.ImageField(null=True, blank=True, upload_to='user_pics', verbose_name='Изображение')

    def __str__(self):
        return f'{self.pk}-{self.name}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Review(models.Model):
    product = models.ForeignKey('webapp.Product', on_delete=models.CASCADE,
                                verbose_name='Продукт', related_name='review_products')
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, default=1,
                               related_name='review_authors', verbose_name='Автор')
    description = models.TextField(max_length=2000, verbose_name='Отзыв')
    rating = models.IntegerField(verbose_name='Оценка', choices=RATING_CHOICES)

    def __str__(self):
        return f'{self.author}-{self.rating}'

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'