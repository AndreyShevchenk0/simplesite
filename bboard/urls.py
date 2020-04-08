from django.urls import path
from .views import index, by_rubric  # последнее
from . import views


urlpatterns = [
    path('<int:rubric_id>/', by_rubric, name='by_rubric'),  # последний
    path('', views.index, name='index'),
]