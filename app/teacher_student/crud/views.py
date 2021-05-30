from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from .forms import StudentsForm, TeachersForm, StudentsAddForm, TeachersAddForm
from .models import Students, Teachers
from typing import Union
import json

@csrf_exempt
def home(request: csrf_exempt) -> render:
    try:
        if request.method == "GET":
            return render(request, 'base/index.html')
        else:
            return render(request, 'base/index.html')

    except Exception as e:
        raise e

        return render(request, 'base/index.html')


@csrf_exempt
def list_teachers(request: csrf_exempt) -> render:
    try:
        teachers_list: Teachers = Teachers.objects.all()
        json_string: str = serializers.serialize('json', teachers_list)
        json_objects_list: json = json.loads(json_string)

        if request.method == "GET":
            return render(request, 'teachers/list.html', {"teachers_list": json_objects_list})
        else:
            return render(request, 'teachers/list.html')

    except Exception as e:
        raise e

        return render(request, 'teachers/list.html')


@csrf_exempt
def add_teachers(request: csrf_exempt) -> render:
    submitted: bool = False
    try:
        if request.method == "POST":
            form: TeachersAddForm = TeachersAddForm(request.POST)
            if form.is_valid():
                name: str = form.cleaned_data.get('name')
                teacher: Teachers = Teachers(name=name)
                teacher.save()

                students: Students = [Students.objects.get(pk=pk) for pk in form.cleaned_data.get('add_student')]
                [student.teachers.add(teacher) for student in students]
            else:
                name: str = form.cleaned_data.get('name')
                teacher: Teachers = Teachers(name=name)
                teacher.save()

            return HttpResponseRedirect('/api/teachers/list')

        else:
            form = TeachersAddForm()
            if 'submitted' in request.GET:
                submitted = True

        return render(request, 'teachers/add_form.html', {'form': form, 'submitted': submitted, "title": "Teacher"})

    except Exception as e:
        raise e

        return render(request, 'teachers/add_form.html', {'form': form, 'submitted': submitted, "title": "Teacher"})


@csrf_exempt
def edit_teachers(request: csrf_exempt, pk: int) -> Union[render, HttpResponseRedirect]:
    submitted: bool = False
    try:
        if request.method == "POST":
            form: TeachersForm = TeachersForm(pk=pk, data=request.POST)

            if form.is_valid():

                teacher: Teachers = Teachers.objects.get(pk=pk)
                teacher.name = form.cleaned_data.get('name')
                teacher.save()

                old_students: Students = Students.objects.filter(teachers__pk=pk)
                updated_students: Students = Students.objects.filter(pk__in=form.cleaned_data.get('add_student'))
                old_stars_students: Students = Students.objects.filter(stars__pk=pk)
                updated_stars_students: Students = Students.objects.filter(pk__in=form.cleaned_data.get('add_star'))

                [student.teachers.remove(teacher) for student in old_students
                 if student not in updated_students]
                [student.teachers.add(teacher) for student in updated_students
                 if student not in old_students]

                [student.stars.remove(teacher) for student in old_stars_students
                 if student not in updated_stars_students or student not in updated_students]
                [student.stars.add(teacher) for student in updated_stars_students
                 if student not in old_stars_students and student in updated_students]

            else:
                teacher: Teachers = Teachers.objects.get(pk=pk)
                teacher.name = form.cleaned_data.get('name')
                teacher.save()

                add_students_list: str = form.cleaned_data.get('add_student')
                add_stars_list: str = form.cleaned_data.get('add_star')
                if not add_students_list:
                    old_students: Students = Students.objects.filter(teachers__pk=pk)
                    [student.teachers.remove(teacher) for student in old_students]
                    old_stars_students: Students = Students.objects.filter(stars__pk=pk)
                    [student.stars.remove(teacher) for student in old_stars_students]
                if add_students_list and not add_stars_list:
                    old_stars_students: Students = Students.objects.filter(stars__pk=pk)
                    [student.stars.remove(teacher) for student in old_stars_students]

            return HttpResponseRedirect('/api/teachers/list')

        else:
            form: TeachersForm = TeachersForm(pk=pk)
            if 'submitted' in request.GET:
                submitted = True

        return render(request, 'teachers/edit_form.html', {'form': form, 'submitted': submitted, "title": "Teacher"})

    except Exception as e:
        raise e

        return render(request, 'teachers/edit_form.html', {'form': form, 'submitted': submitted, "title": "Teacher"})


@csrf_exempt
def delete_teachers(request: csrf_exempt, pk: int) -> HttpResponseRedirect:
    try:
        if request.method == "POST":
            Teachers.objects.filter(pk=pk).delete()

        return HttpResponseRedirect('/api/teachers/list')

    except Exception as e:
        raise e

        return HttpResponseRedirect('/api/teachers/list')


@csrf_exempt
def list_students(request: csrf_exempt) -> render:
    try:
        if request.method == "GET":
            students_list: Students = Students.objects.all()
            json_string: str = serializers.serialize('json', students_list)
            json_objects_list: json = json.loads(json_string)

            return render(request, 'students/list.html', {"students_list": json_objects_list})

        else:
            return render(request, 'students/list.html')

    except Exception as e:
        raise e

        return render(request, 'students/list.html')


@csrf_exempt
def add_students(request: csrf_exempt) -> Union[render, HttpResponseRedirect]:
    submitted: bool = False
    try:
        if request.method == "POST":
            form: StudentsAddForm = StudentsAddForm(request.POST)
            if form.is_valid():
                name: str = form.cleaned_data.get('name')
                student: Students = Students(name=name)
                student.save()
                teachers: Teachers = [Teachers.objects.get(pk=pk) for pk in form.cleaned_data.get('add_teacher')]
                [student.teachers.add(teacher) for teacher in teachers]
            else:
                name: str = form.cleaned_data.get('name')
                student: Students = Students(name=name)
                student.save()

            return HttpResponseRedirect('/api/students/list')

        else:
            form: StudentsAddForm = StudentsAddForm()
            if 'submitted' in request.GET:
                submitted = True

        return render(request, 'students/add_form.html', {'form': form, 'submitted': submitted, "title": "Student"})

    except Exception as e:
        raise e

        return render(request, 'students/add_form.html', {'form': form, 'submitted': submitted, "title": "Student"})


@csrf_exempt
def edit_students(request: csrf_exempt, pk: int) -> Union[render, HttpResponseRedirect]:
    submitted: bool = False
    try:
        student_info: Students = Students.objects.filter(pk=pk)
        json_string: str = serializers.serialize('json', student_info)
        json_student: json = json.loads(json_string)

        if request.method == "POST":
            form: StudentsForm = StudentsForm(student_list=json_student, data=request.POST)
            if form.is_valid():
                student: Students = Students.objects.get(pk=pk)
                student.name = form.cleaned_data.get('name')
                student.save()
                old_teachers: Teachers = Teachers.objects.filter(students__pk=pk)
                updated_teachers: Teachers = Teachers.objects.filter(pk__in=form.cleaned_data.get('add_teacher'))
                [student.teachers.remove(teacher) for teacher in old_teachers if teacher not in updated_teachers]
                [student.teachers.add(teacher) for teacher in updated_teachers if teacher not in old_teachers]
            else:
                student: Students = Students.objects.get(pk=pk)
                student.name = form.cleaned_data.get('name')
                student.save()
                old_teachers: Teachers = Teachers.objects.filter(students__pk=pk)
                [student.teachers.remove(teacher) for teacher in old_teachers]

            return HttpResponseRedirect('/api/students/list')

        else:
            form: StudentsForm = StudentsForm(student_list=json_student)
            if 'submitted' in request.GET:
                submitted = True

        return render(request, 'students/edit_form.html', {'form': form, 'submitted': submitted, 'title': "Student"},)

    except Exception as e:
        raise e

        return render(request, 'students/edit_form.html', {'form': form, 'submitted': submitted, 'title': "Student"})


@csrf_exempt
def delete_students(request: csrf_exempt, pk: int) -> HttpResponseRedirect:
    try:
        if request.method == "POST":
            Students.objects.filter(pk=pk).delete()

        return HttpResponseRedirect('/api/students/list')

    except Exception as e:
        raise e

        return HttpResponseRedirect('/api/students/list')
