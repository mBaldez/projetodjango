from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from .models import Course, Student, Category, Instructor
from .forms import CourseForm, SearchForm, StudentForm, StudentSearchForm, CategoryForm, InstructorForm

def home(request):
    context = {
        'total_students': Student.objects.count(),
        'total_courses': Course.objects.count(),
        'total_categories': Category.objects.count(),
        'total_instructors': Instructor.objects.count()
    }
    return render(request, 'home.html', context)


def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    return render(request, "course_detail.html", {"course": course})


def course_create(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('course_list')
    else:
        form = CourseForm()

    return render(request, 'cursos/course_form.html', {'form': form})

def course_list(request):
    form = SearchForm(request.GET or None)
    courses = Course.objects.select_related('category', 'instructor')

    if form.is_valid() and form.cleaned_data['query']:
        q = form.cleaned_data['query']
        courses = courses.filter(
            Q(title__icontains=q) |
            Q(description__icontains=q) |
            Q(category__name__icontains=q) |
            Q(instructor__user__username__icontains=q)
        )

    return render(request, 'cursos/course_list.html', {
        'courses': courses.order_by('-created_at'),
        'form': form
    })

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
    form = StudentSearchForm(request.GET or None)
    students = Student.objects.all()

    if form.is_valid() and form.cleaned_data['query']:
        q = form.cleaned_data['query']
        students = students.filter(
            Q(full_name__icontains=q) | Q(cpf__icontains=q)
        )

    context = {
        'students': students.order_by('-created_at'),
        'form': form
    }
    return render(request, 'cursos/student_list.html', context)


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

# ---- CATEGORY ----
def category_list(request):
    categories = Category.objects.all()
    return render(request, 'category_list.html', {'categories': categories})

def category_create(request):
    form = CategoryForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('category_list')
    return render(request, 'category_form.html', {
        'form': form,
        'title': 'Nova Categoria',
        'list_url': 'category_list'
        })

def category_update(request, pk):
    category = get_object_or_404(Category, pk=pk)
    form = CategoryForm(request.POST or None, instance=category)
    if form.is_valid():
        form.save()
        return redirect('category_list')
    return render(request, 'category_form.html', {'form': form})

def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    category.delete()
    return redirect('category_list')

# ---- INSTRUCTOR ----
def instructor_list(request):
    instructors = Instructor.objects.all()
    return render(request, 'instructor_list.html', {'instructors': instructors})

def instructor_create(request):
    form = InstructorForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('instructor_list')
    return render(request, 'instructor_form.html', {
        'form': form,
        'title': 'Novo Instrutor',
        'list_url': 'instructor_list'
        })

def instructor_update(request, pk):
    instructor = get_object_or_404(Instructor, pk=pk)
    form = InstructorForm(request.POST or None, instance=instructor)
    if form.is_valid():
        form.save()
        return redirect('instructor_list')
    return render(request, 'instructor_form.html', {'form': form})

def instructor_delete(request, pk):
    instructor = get_object_or_404(Instructor, pk=pk)
    instructor.delete()
    return redirect('instructor_list')
