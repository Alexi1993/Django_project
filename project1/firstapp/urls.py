from django.urls import path
from .views import ArticleList, ArticleDetail, NewsList , NewsDetail  # импортируем наше представление

urlpatterns = [
    # path — означает путь. В данном случае путь ко всем товарам у нас останется пустым, позже станет ясно, почему
    path('', ArticleList.as_view()),
    path('<int:pk>', ArticleDetail.as_view()),
    path('', NewsList.as_view()),
    path('<int:pk>', NewsDetail.as_view())
    # т. к. сам по себе это класс, то нам надо представить этот класс в виде view. Для этого вызываем метод as_view
]