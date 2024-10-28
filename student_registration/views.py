from django.shortcuts import render, redirect, get_object_or_404
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

def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)  # Corrected to use Student model
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)  # Added request.POST to handle form data
        if form.is_valid():
            form.save()
            return redirect("student_list")
    else:
        form = StudentForm(instance=student)  # Corrected 'from' to 'form'
    
    return render(request, 'confirm_update.html', {'form': form})  # Make sure 'update_student.html' exists

def delete_student(request, pk):
    student = get_object_or_404(Student, pk=pk)  # Changed to use get_object_or_404
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')
    return render(request, 'confirm_delete.html', {'student': student})

def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})
