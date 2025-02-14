from django.urls import path,include
from emp_app.views import *
urlpatterns = [
    path('index/',index,name='index'),
    path('view_all_emp/',view_all_emp,name='view_all_emp'),
    path('add_emp/',add_emp,name='add_emp'),
    path('remove_emp/',remove_emp,name='remove_emp'),
    path('filter_emp/',filter_emp,name='filter_emp'),
]