from django import forms
from .models import Course, Student

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'description', 'price', 'category', 'instructor']


class SearchForm(forms.Form):
    query = forms.CharField(label="Buscar Curso", max_length=100, required=False)


class StudentForm(forms.ModelForm):
    birth_date = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}), required=False)

    class Meta:
        model = Student
        fields = [
            'full_name', 'birth_date', 'cpf', 'address', 'city',
            'state', 'postal_code', 'phone', 'email', 'preferred_payment_method'
        ]


class StudentSearchForm(forms.Form):
    query = forms.CharField(label="Buscar Aluno (nome ou CPF)", max_length=100, required=False)
