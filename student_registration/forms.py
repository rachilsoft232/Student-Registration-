from django import forms
from .models import Student  # Make sure to replace Student with your actual model name

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student  # Replace with your model
        fields = ['name', 'roll_number', 'email', 'phone_number']  # Replace with your model fields
