from django.urls import path
from .views import IndexView

urlpatterns = [

    path('endereco/', MinhaView.as_view(), name='name-da-url'),

]