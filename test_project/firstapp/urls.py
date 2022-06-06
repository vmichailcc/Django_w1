from django.urls import path
from .views import hellodjango, input_name, date, year, month, day

urlpatterns = [
    path('', hellodjango),
    path('date/', date),
    path('date/year/', year),
    path('date/month/', month),
    path('date/day/', day),
    path('<str:name>/', input_name),
]
