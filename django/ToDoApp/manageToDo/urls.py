from django.urls import path
from . import views

app_name = 'manageToDo'

urlpatterns = [
    path('', views.home, name='home'),
    path('delete/<list_id>', views.delete, name='delete'),
    path('cross/<list_id>', views.cross, name='cross'),
    path('uncross/<list_id>', views.uncross, name='uncross'),

]
