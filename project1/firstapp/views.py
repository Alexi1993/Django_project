from django.views.generic import \
    ListView, \
    DetailView  # импортируем класс, который говорит нам о том, что в этом представлении мы будем выводить список объектов из БД
from .models import Article, News
import datetime


class ArticleList(ListView):
    model = Article  # указываем модель, объекты которой мы будем выводить
    template_name = 'article.html'  # указываем имя шаблона, в котором будет лежать HTML, в котором будут все инструкции о том, как именно пользователю должны вывестись наши объекты
    context_object_name = 'Article'  # это имя списка, в котором будут лежать все объекты, его надо указать, чтобы обратиться к самому списку объектов через HTML-шаблон

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.datetime.utcnow().strftime(
            '%B %d %Y - %H:%M:%S')  # добавим переменную текущей даты time_now
        context['value1'] = None
        return context


class ArticleDetail(DetailView):
    model = Article  # модель всё та же, но мы хотим получать детали конкретно отдельного товара
    template_name = 'article.html'  # название шаблона будет product.html
    context_object_name = 'Article'  # название объекта. в нём будет


class NewsList(ListView):
    model = News  # указываем модель, объекты которой мы будем выводить
    template_name = 'article.html'  # указываем имя шаблона, в котором будет лежать HTML, в котором будут все инструкции о том, как именно пользователю должны вывестись наши объекты
    context_object_name = 'News'  # это имя списка, в котором будут лежать все объекты, его надо указать, чтобы обратиться к самому списку объектов через HTML-шаблон

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.datetime.utcnow().strftime(
            '%B %d %Y - %H:%M:%S')  # добавим переменную текущей даты time_now
        context['value1'] = None
        return context


class NewsDetail(DetailView):
    model = News  # модель всё та же, но мы хотим получать детали конкретно отдельного товара
    template_name = 'article.html'  # название шаблона будет product.html
    context_object_name = 'News'  # название объекта. в нём будет
