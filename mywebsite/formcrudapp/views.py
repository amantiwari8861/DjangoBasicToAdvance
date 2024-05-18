# from django.shortcuts import render,redirect
# from .models import Student

# # Create your views here.
# def form_update(request):
    
#     if(request.POST):
#         form_data=request.POST.dict()
#         print(form_data)
#     name=form_data.get("name")
#     mobileno=form_data.get("mobileno")
#     # print(name,mobileno)
#     Student.objects.create(name=name,mobileno=mobileno)
#     return redirect("saveform")

from django.shortcuts import render, get_object_or_404, redirect
from .models import Student
from .forms import StudentForm

# List all students
def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})

# Create a new student
def student_create(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'student_form.html', {'form': form})

# Update an existing student
def student_update(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'student_form.html', {'form': form})

# Delete a student
def student_delete(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == "POST":
        student.delete()
        return redirect('student_list')
    return render(request, 'student_confirm_delete.html', {'student': student})
