from django.urls import path,include
from api.views import *
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('EmployeeViewset',EmployeeViewset,basename='EmployeeViewset')

urlpatterns = [
    path('studentsView/',studentsView,name='studentsView'),
    path('studentDetailView/<int:pk>/',studentDetailView,name='studentDetailView'),

   #class based urls
    path('EmployeesView/',EmployeesView.as_view(),name='EmployeesView') ,
    path('EmployeeDetailView/<int:pk>/',EmployeeDetailView.as_view(),name='EmployeeDetailView'),

   #Viewsets
   path('',include(router.urls)),
   path('BlogsView/',BlogsView.as_view(),name='BlogsView'),
   path('CommentsView/',CommentsView.as_view(),name='CommentsView'),

   path('BlogDetailView/<int:pk>/',BlogDetailView.as_view(),name='BlogDetailView'),
   path('CommentDetailView/<int:pk>/',CommentDetailView.as_view(),name='CommentDetailView'),
]