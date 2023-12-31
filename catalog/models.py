from django.db import models


NULLABLE = {'blank': True, 'null': True}


class Product(models.Model):
    title = models.CharField(max_length=150, verbose_name='наименование')
    description = models.TextField(verbose_name='описание', **NULLABLE)
    image = models.ImageField(upload_to='images/product/', verbose_name='изображение', **NULLABLE)
    category = models.ForeignKey('catalog.Category', verbose_name='категория', on_delete=models.CASCADE)
    price = models.IntegerField(verbose_name='цена за штуку')
    date_of_creation = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    last_modified_date = models.DateTimeField(auto_now=True, verbose_name='дата последнего изменения')

    def __str__(self):
        return f'{self.title}, {self.price}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'


class Category(models.Model):
    title = models.CharField(max_length=150, verbose_name='наименование')
    description = models.TextField(verbose_name='описание', **NULLABLE)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'

class Blog(models.Model):
    title = models.CharField(max_length=150, verbose_name='title')
    slug = models.CharField(max_length=150, verbose_name='slug')
    content = models.CharField(max_length=150, verbose_name='content')
    preview = models.ImageField(max_length=150, verbose_name='поле 4')
    date_of_creation = models.DateField(auto_now_add=True)
    publication_sign = models.BooleanField(max_length=150, verbose_name='publication_sign')
    views = models.IntegerField(default=0,editable=False)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'

