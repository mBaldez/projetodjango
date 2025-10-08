from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('curso/<int:pk>/', views.course_detail, name='course_detail'),
    path('novo/', views.course_create, name='course_create'),
    path('buscar/', views.search, name='search'),
    path('cursos/', views.course_list, name='course_list'),
    
    # alunos
    path('alunos/', views.student_list, name='student_list'),
    path('aluno/novo/', views.student_create, name='student_create'),
    path('aluno/buscar/', views.student_search, name='student_search'),

    # Category
    path('categories/', views.category_list, name='category_list'),
    path('categories/create/', views.category_create, name='category_create'),
    path('categories/<int:pk>/edit/', views.category_update, name='category_update'),
    path('categories/<int:pk>/delete/', views.category_delete, name='category_delete'),

    # Instructor
    path('instructors/', views.instructor_list, name='instructor_list'),
    path('instructors/create/', views.instructor_create, name='instructor_create'),
    path('instructors/<int:pk>/edit/', views.instructor_update, name='instructor_update'),
    path('instructors/<int:pk>/delete/', views.instructor_delete, name='instructor_delete'),
]
