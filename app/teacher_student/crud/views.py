from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Students

@csrf_exempt
def list_teachers(request):

    try:
        json_request = {'teachers_array': [
            {"name": "Diego Martin Mancini"},
            {"name": "Luciana Agnoleto"},
        ]}
        if request.method == "GET":
            return render(request, 'list_teachers.html', json_request)

        else:
            return render(request, 'list_teachers.html')

    except Exception as e:
        raise e

        return render(request, 'list_teachers.html')

@csrf_exempt
def add_teachers(request):

    try:
        if request.method == "POST":
            return render(request, 'add_teachers.html')

        else:
            return render(request, 'add_teachers.html')

    except Exception as e:
        raise e

        return render(request, 'add_teachers.html')

@csrf_exempt
def edit_teachers(request):

    try:
        if request.method == "POST":
            return render(request, 'edit_teachers.html')

        else:
            return render(request, 'edit_teachers.html')

    except Exception as e:
        raise e

        return render(request, 'edit_teachers.html')

@csrf_exempt
def delete_teachers(request):

    try:
        if request.method == "DELETE":
            return render(request, 'delete_teachers.html')

        else:
            return render(request, 'delete_teachers.html')

    except Exception as e:
        raise e

        return render(request, 'delete_teachers.html')

@csrf_exempt
def list_students(request):

    try:
        students_list = Students.objects.all()
        for student in students_list:
            print("---------------------")
            print(student.name)
            for teacher in student.teachers.all():
                print("teacher: ", teacher.name)
            for star in student.stars.all():
                print("star: ", star.teachers.name)
        json_request = {'students_list': [
            {"name": "Diego Martin Mancini"},
            {"name": "Luciana Agnoleto"},
        ]}
        if request.method == "GET":
            return render(request, 'list_students.html', json_request)

        else:
            return render(request, 'list_students.html')

    except Exception as e:
        raise e

        return render(request, 'list_students.html')

@csrf_exempt
def add_students(request):

    try:
        if request.method == "POST":
            return render(request, 'add_students.html')

        else:
            return render(request, 'add_students.html')

    except Exception as e:
        raise e

        return render(request, 'add_students.html')

@csrf_exempt
def edit_students(request):

    try:
        if request.method == "POST":
            return render(request, 'edit_students.html')

        else:
            return render(request, 'edit_students.html')

    except Exception as e:
        raise e

        return render(request, 'edit_students.html')

@csrf_exempt
def delete_students(request):

    try:
        if request.method == "DELETE":
            return render(request, 'delete_students.html')

        else:
            return render(request, 'delete_students.html')

    except Exception as e:
        raise e

        return render(request, 'delete_students.html')





