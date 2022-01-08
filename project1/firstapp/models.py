from django.db import models
from django.core.validators import MinValueValidator


class Article(models.Model):
    name = models.CharField(
        max_length=50,
        unique=True,
    )
    description = models.TextField(blank=True)
    category = models.IntegerField(
        validators=[MinValueValidator(0)],
    )
    # поле категории будет ссылаться на модель категории
    category = models.ForeignKey(
        to='News',
        on_delete=models.CASCADE,
        related_name='Article',
    )

    def __str__(self):
        return f'{self.name.title()}: {self.description[:20]}'


class News(models.Model):
    name = models.CharField(max_length=100, unique=True)  # названия категорий тоже не должны повторяться
    description = models.TextField(blank=True)

    def __str__(self):
        return f'{self.name.title()}'

    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'
