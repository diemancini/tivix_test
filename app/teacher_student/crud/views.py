from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from .forms import StudentsForm, TeachersForm, StudentsAddForm, TeachersAddForm
from .models import Students, Teachers
import json

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

    submitted = False
    try:
        if request.method == "POST":
            form = TeachersAddForm(request.POST)
            if form.is_valid():
                name: str = form.cleaned_data.get('name')
                teacher: Teachers = Teachers(name=name)
                teacher.save()
                print(form.cleaned_data.get('add_student'))
                students: Students = [Students.objects.get(pk=pk) for pk in form.cleaned_data.get('add_student')]
                [student.teachers.add(teacher) for student in students]

                return HttpResponseRedirect('/api/teachers/list')
        else:
            form = TeachersAddForm()
            if 'submitted' in request.GET:
                submitted = True

        return render(request, 'teachers/add_form.html', {'form': form, 'submitted': submitted})

    except Exception as e:
        raise e

        return render(request, 'teachers/add_form.html', {'form': form, 'submitted': submitted})

@csrf_exempt
def edit_teachers(request, pk):

    submitted = False
    try:
        if request.method == "POST":
            form = TeachersForm(pk=pk, data=request.POST)
            if form.is_valid():

                old_students = Students.objects.filter(teachers__pk=pk)#.distinct()
                updated_students = Students.objects.filter(pk__in=form.cleaned_data.get('add_student'))
                teacher = Teachers.objects.get(pk=pk)
                teacher.name = form.cleaned_data.get('name')
                teacher.save()
                [student.teachers.remove(teacher) for student in old_students if student not in updated_students]
                [student.teachers.add(teacher) for student in updated_students if student not in old_students]
            else:
                teacher = Teachers.objects.get(pk=pk)
                teacher.name = form.cleaned_data.get('name')
                teacher.save()
                old_students = Students.objects.filter(teachers__pk=pk)
                [student.teachers.remove(teacher) for student in old_students]

            return HttpResponseRedirect('/api/teachers/list')
        else:
            form = TeachersForm(pk=pk)
            if 'submitted' in request.GET:
                submitted = True

        return render(request, 'teachers/edit_form.html', {'form': form, 'submitted': submitted})

    except Exception as e:
        raise e

        return render(request, 'teachers/edit_form.html', {'form': form, 'submitted': submitted})

@csrf_exempt
def delete_teachers(request, pk):

    try:
        if request.method == "POST":
            Teachers.objects.filter(pk=pk).delete()

        return HttpResponseRedirect('/api/teachers/list')

    except Exception as e:
        raise e

        return HttpResponseRedirect('/api/teachers/list')

@csrf_exempt
def list_students(request):

    try:
        students_list = Students.objects.all()
        json_string = serializers.serialize('json', students_list)
        json_objects_list = json.loads(json_string)

        if request.method == "GET":

            return render(request, 'students/list.html', {"students_list": json_objects_list})

        else:
            return render(request, 'students/list.html')

    except Exception as e:
        raise e

        return render(request, 'students/list.html')

@csrf_exempt
def add_students(request):

    submitted = False
    try:
        if request.method == "POST":
            form = StudentsAddForm(request.POST)
            if form.is_valid():
                name = form.cleaned_data.get('name')
                student = Students(name=name)
                student.save()
                teachers = [Teachers.objects.get(pk=pk) for pk in form.cleaned_data.get('add_teacher')]
                [student.teachers.add(teacher) for teacher in teachers]

                return HttpResponseRedirect('/api/students/list')
        else:
            form = StudentsAddForm()
            if 'submitted' in request.GET:
                submitted = True

        return render(request, 'students/add_form.html', {'form': form, 'submitted': submitted})

    except Exception as e:
        raise e

        return render(request, 'students/add_form.html', {'form': form, 'submitted': submitted})

@csrf_exempt
def edit_students(request, pk):

    submitted = False
    try:
        student_info = Students.objects.filter(pk=pk)
        json_string = serializers.serialize('json', student_info)
        json_student = json.loads(json_string)

        if request.method == "POST":
            form = StudentsForm(student_list=json_student, data=request.POST)
            if form.is_valid():
                student = Students.objects.get(pk=pk)
                student.name = form.cleaned_data.get('name')
                student.save()
                old_teachers = Teachers.objects.filter(students__pk=pk)
                updated_teachers = Teachers.objects.filter(pk__in=form.cleaned_data.get('add_teacher'))
                [student.teachers.remove(teacher) for teacher in old_teachers if teacher not in updated_teachers]
                [student.teachers.add(teacher) for teacher in updated_teachers if teacher not in old_teachers]
            else:
                student = Students.objects.get(pk=pk)
                student.name = form.cleaned_data.get('name')
                student.save()
                old_teachers = Teachers.objects.filter(students__pk=pk)
                [student.teachers.remove(teacher) for teacher in old_teachers]

            return HttpResponseRedirect('/api/students/list')

        else:
            form = StudentsForm(student_list=json_student)
            if 'submitted' in request.GET:
                submitted = True

        return render(request, 'students/edit_form.html', {'form': form, 'submitted': submitted})

    except Exception as e:
        raise e

        return render(request, 'students/edit_form.html', {'form': form, 'submitted': submitted})

@csrf_exempt
def delete_students(request, pk):

    try:
        if request.method == "POST":
            Students.objects.filter(pk=pk).delete()
            #return HttpResponseRedirect('/api/students/list')

        return HttpResponseRedirect('/api/students/list')

    except Exception as e:
        raise e

        return HttpResponseRedirect('/api/students/list')





