
from django.contrib import admin
from django.urls import path

from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.student_list, name='student_list'),  # Root URL
    path('add/', views.add_student, name='add_student'),
    path('update/<int:pk>/', views.student_update, name='update_student'),
    path('delete/<int:pk>/', views.delete_student, name='delete_student'),
    # path('students/', views.student_list, name='student_list'),
]
