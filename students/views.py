from django.shortcuts import render ,redirect ,get_object_or_404
from .models import Student
from .forms import StudentForm
from django.core.paginator import Paginator
# Create your views here.


def student_list(request):
    students =Student.objects.all().order_by('full_name')
    search_query = request.GET.get("q","").strip()
    course_query = request.GET.get("course","").strip()
    if search_query:
        from django.db.models import Q
        students = students.filter(Q(full_name__icontains=search_query)|Q(email__iconatins=search_query))
    if course_query:
        students = students.filter(course__iexact=course_query)
    courses =(Student.objects.order_by("course").values_list("course",flat=True).distinct())
    paginator = Paginator(students,10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number) 
    context = {
        'students' :page_obj.object_list,
        'page_obj': page_obj,
        'search_query':search_query,
        'course_query':course_query,
        'courses':courses,
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

def student_update(request,pk):
    student = get_object_or_404(Student,pk=pk)

    if request.method=='POST':
        form =StudentForm(request.POST,instance=student)
        if form.is_valid():
            form.save()
            return redirect("student_list")
    else:
        form = StudentForm(instance=student)
    return render(request,'students/student_form.html',
                  {
                      'form':form,
                      'student':student,
                  })

def student_delete(request,pk):
    student = get_object_or_404(Student,pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list.html')
    return render(request,"students/student_confirm_delete.html",
                  {"student":student})