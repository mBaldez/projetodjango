from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Category(models.Model):
    name = models.CharField(max_length=100)
    projeto = models.CharField(max_length=100, blank=True, null=True)
    genero = models.CharField(max_length=50, blank=True, null=True)
    nivel = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name


class Instructor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    formacao = models.CharField(max_length=100, blank=True, null=True)  # use sem acento
    curso = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    bio = models.TextField(blank=True)

    def __str__(self):
        return getattr(self.user, "username", str(self.user))


class Student(models.Model):
    PAYMENT_CHOICES = [
        ('card', 'Cartão de Crédito'),
        ('paypal', 'PayPal'),
        ('pix', 'PIX'),
        ('mbway', 'MBWay'),
        ('boleto', 'Boleto'),
        ('other', 'Outro'),
    ]

    # ligação opcional ao User (autenticação)
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True)
    full_name = models.CharField("Nome completo", max_length=200)
    birth_date = models.DateField("Data de nascimento", null=True, blank=True)
    cpf = models.CharField("CPF", max_length=14, unique=True)  # considerar validação extra
    address = models.CharField("Endereço", max_length=255, blank=True)
    city = models.CharField("Cidade", max_length=100, blank=True)
    state = models.CharField("Estado", max_length=100, blank=True)
    postal_code = models.CharField("Código postal", max_length=20, blank=True)
    phone = models.CharField("Telefone", max_length=30, blank=True)
    email = models.EmailField("E-mail")
    preferred_payment_method = models.CharField(
        "Forma de pagamento preferida",
        max_length=10,
        choices=PAYMENT_CHOICES,
        default='pix'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Aluno"
        verbose_name_plural = "Alunos"

    def __str__(self):
        return self.full_name


class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Lesson(models.Model):
    course = models.ForeignKey(Course, related_name="lessons", on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    video_url = models.URLField(blank=True)
    order = models.IntegerField()

    def __str__(self):
        return f"{self.course.title} - {self.title}"


class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrolled_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.full_name} -> {self.course.title}"


class Payment(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pendente'),
        ('paid', 'Pago'),
        ('failed', 'Falhado'),
    ]

    enrollment = models.OneToOneField(Enrollment, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    payment_method = models.CharField(max_length=10, choices=Student.PAYMENT_CHOICES, default='pix')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    paid_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Pagamento {self.enrollment.student.full_name} - {self.amount}"


class Review(models.Model):
    course = models.ForeignKey(Course, related_name="reviews", on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Avaliação {self.course.title} - {self.rating}⭐"
