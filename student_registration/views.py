from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentForm



def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')  # Redirect to student list page after saving
    else:
        form = StudentForm()
    return render(request, 'add_student.html', {'form': form})

def delete_student(request, pk):
    student = Student.objects.get(pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')
    return render(request, 'confirm_delete.html', {'student': student})

def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})