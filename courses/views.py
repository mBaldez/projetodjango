from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from .models import Course, Student
from .forms import CourseForm, SearchForm, StudentForm, StudentSearchForm

def home(request):
    courses = Course.objects.all()
    return render(request, "index.html", {"courses": courses})


def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    return render(request, "course_detail.html", {"course": course})


def course_create(request):
    if request.method == "POST":
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = CourseForm()
    return render(request, "course_form.html", {"form": form})


def search(request):
    form = SearchForm(request.GET)
    results = []
    if form.is_valid():
        query = form.cleaned_data["query"]
        if query:
            results = Course.objects.filter(title__icontains=query)
    return render(request, "search.html", {"form": form, "results": results})


# ---- Students ----
def student_list(request):
    students = Student.objects.all()
    return render(request, "student_list.html", {"students": students})


def student_create(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("student_list")
    else:
        form = StudentForm()
    return render(request, "student_form.html", {"form": form})


def student_search(request):
    form = StudentSearchForm(request.GET)
    results = []
    if form.is_valid():
        q = form.cleaned_data.get("query")
        if q:
            results = Student.objects.filter(Q(full_name__icontains=q) | Q(cpf__icontains=q))
    return render(request, "student_search.html", {"form": form, "results": results})
