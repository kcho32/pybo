from django.contrib import admin
from django.urls import path
from pybo import views

app_name = 'pybo'

urlpatterns = [
    # path('', views.index, name='index'),
    # path('<int:question_id>', views.detail, name='detail')
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>', views.DetailView.as_view(), name='detail'),
    path('answer/create/<int:question_id>', views.answer_create, name='answer_create'),
    path('question/create', views.question_create, name='question_create'),
]

