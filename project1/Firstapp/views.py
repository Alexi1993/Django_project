from django.shortcuts import render
from django.views.generic import \
    ListView, \
    DetailView
from .models import Article
import datetime

class ArticleList(ListView):
    model = Article  # указываем модель, объекты которой мы будем выводить
    template_name = 'article.html'  # указываем имя шаблона, в котором будет лежать HTML, в котором будут все инструкции о том, как именно пользователю должны вывестись наши объекты
    context_object_name = 'articles'  # это имя списка, в котором будут лежать все объекты, его надо указать, чтобы обратиться к самому списку объектов через HTML-шаблон
    queryset = Article.objects.order_by('-id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()  # добавим переменную текущей даты time_now
        context[
            'value1'] = None  # добавим ещё одну пустую переменную, чтобы на её примере посмотреть работу другого фильтра
        return context

class ArticleDetail(DetailView):
    model = Article  # модель всё та же, но мы хотим получать детали конкретно отдельного товара
    template_name = 'article.html'  # название шаблона будет product.html
    context_object_name = 'articles'  # название объекта. в нём будет



def index(request):
    return render(request, 'article.html')
