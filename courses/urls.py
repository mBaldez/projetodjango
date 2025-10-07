from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('curso/<int:pk>/', views.course_detail, name='course_detail'),
    path('novo/', views.course_create, name='course_create'),
    path('buscar/', views.search, name='search'),

    # alunos
    path('alunos/', views.student_list, name='student_list'),
    path('aluno/novo/', views.student_create, name='student_create'),
    path('aluno/buscar/', views.student_search, name='student_search'),
]
