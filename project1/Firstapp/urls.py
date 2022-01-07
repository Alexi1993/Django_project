from django.urls import path
from .views import ArticleList, ArticleDetail # импортируем наше представление

urlpatterns = [
    # path — означает путь. В данном случае путь ко всем товарам у нас останется пустым, позже станет ясно, почему
    path('', ArticleList.as_view()),
    path('<int:pk>', ArticleDetail.as_view()),
]
