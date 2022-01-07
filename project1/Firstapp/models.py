from django.db import models
from django.core.validators import MinValueValidator


class Article(models.Model):
    name = models.CharField(
        max_length=50,
        unique=True,  # названия товаров не должны повторяться
    )
    description = models.TextField()
    quantity = models.IntegerField(
        validators=[MinValueValidator(0)],
    )
    # поле категории будет ссылаться на модель категории
    article = models.ForeignKey(
        to='article',
        on_delete=models.CASCADE,
        related_name='news',  # все продукты в категории будут доступны через поле products
    )

    def __str__(self):
        return f'{self.name.title()}: {self.description[:20]}'


#
class News(models.Model):
    name = models.CharField(max_length=100, unique=True)  # названия категорий тоже не должны повторяться
    description = models.TextField()

    def __str__(self):
        return f'{self.name.title()}' 

    class Meta:
        verbose_name = 'News',
        verbose_name_plural = 'News'
