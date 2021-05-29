from django import forms
from .models import Students, Teachers


class StudentsForm(forms.Form):
    class Meta:
        model = Teachers
        fields = ['name', 'add_teacher']

    def __init__(self, *args, **kwargs):
        json_student = kwargs.pop('student_list')
        super(StudentsForm, self).__init__(*args, **kwargs)
        self.fields['add_teacher'].initial = json_student[0]['fields']['teachers']
        self.fields['add_teacher'].choices = [(teacher.pk, teacher.name) for teacher in Teachers.objects.all()]
        self.fields['name'].initial = json_student[0]['fields']['name']

    name = forms.CharField(
        label='Student name',
        max_length=100,
        widget=forms.TextInput(attrs={'class': "form-control"}))

    add_teacher = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple())


class StudentsAddForm(forms.Form):
    class Meta:
        model = Teachers
        fields = ['name', 'add_teacher']

    def __init__(self, *args, **kwargs):
        super(StudentsAddForm, self).__init__(*args, **kwargs)
        self.fields['add_teacher'].choices = [(teacher.pk, teacher.name) for teacher in Teachers.objects.all()]

    name = forms.CharField(
        label='Student name',
        max_length=100,
        widget=forms.TextInput(attrs={'class': "form-control"}))

    add_teacher = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple())


class TeachersForm(forms.Form):
    class Meta:
        model = Teachers
        fields = ['name', 'add_student']

    def __init__(self, *args, **kwargs):
        pk = kwargs.pop('pk')
        super(TeachersForm, self).__init__(*args, **kwargs)
        self.fields['add_student'].initial = [student.pk for student in Students.objects.filter(teachers__pk=pk)]
        self.fields['add_student'].choices = [(student.pk, student.name) for student in Students.objects.all()]
        self.fields['add_star'].initial = [student.pk for student in Students.objects.filter(stars__pk=pk)]
        self.fields['add_star'].choices = [(student.pk, student.name) for student in Students.objects.all()]
        self.fields['name'].initial = Teachers.objects.get(pk=pk)

    name = forms.CharField(
        label='Student name',
        max_length=100,
        widget=forms.TextInput(attrs={'class': "form-control"}))

    add_student = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple())

    add_star = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple())


class TeachersAddForm(forms.Form):
    class Meta:
        model = Teachers
        fields = ['name', 'add_student']

    def __init__(self, *args, **kwargs):
        super(TeachersAddForm, self).__init__(*args, **kwargs)
        self.fields['add_student'].choices = [(student.pk, student.name) for student in Students.objects.all()]

    name = forms.CharField(
        label='Teacher name',
        max_length=100,
        widget=forms.TextInput(attrs={'class': "form-control"}))

    add_student = forms.MultipleChoiceField(
        # choices=OPTIONS_STUDENTS,
        widget=forms.CheckboxSelectMultiple())
