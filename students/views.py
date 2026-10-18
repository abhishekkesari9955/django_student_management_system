from django.shortcuts import render ,redirect
from .models import Student
from .forms import StudentForm
# Create your views here.


def student_list(request):
    students =Student.objects.all().order_by('full_name')
    context = {
        'students' :students
    }
    return render(request, 'students/student_list.html', context)
def student_create(request):
    if request.method=="POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("student_list")
    else:
        form = StudentForm()
    return render(request, "students/student_form.html",{
        'form':form
    })
