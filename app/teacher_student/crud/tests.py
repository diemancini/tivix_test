from django.test import TestCase
from .models import Students, Teachers


class CrudTest(TestCase):
    fixtures = [
        'students.json',
        'teachers.json'
    ]

    def test_student_name(self) -> None:
        student: Students = Students.objects.get(pk=1)
        self.assertEqual(student.name, "Enzo")

    def test_student_teacher_name(self) -> None:
        student: Students = Students.objects.get(pk=1)
        teachers: Teachers = student.teachers.all()
        self.assertEqual(teachers[0].name, "Diego M Mancini")

    def test_teacher_name(self) -> None:
        teacher: Teachers = Teachers.objects.get(pk=1)
        self.assertEqual(teacher.name, "Diego M Mancini")

    def test_teacher_student_name(self) -> None:
        teacher: Teachers = Teachers.objects.get(pk=1)
        student: Students = Students.objects.get(pk=1)
        teachers: Teachers = student.teachers.all()
        self.assertEqual(teacher.name, teachers[0].name)

    def test_teacher_student_star(self) -> None:
        teacher: Teachers = Teachers.objects.get(pk=1)
        student: Students = Students.objects.get(pk=1)
        teachers: Teachers = student.stars.all()
        self.assertEqual(teacher.name, teachers[0].name)
