from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def index(request):
    #return HttpResponse('first view')
    return render(request, 'myApp/index.html')

def detail(request,num1,num2):
    return HttpResponse('detail-%s-%s'%(num1,num2))

from .models import Grades
def grades(request):
    #去模板里取数据
    gradesList = Grades.objects.all()
    #将数据传递给模板,模板渲染页面，将渲染好的页面返回浏览器
    return render(request, 'myApp/grades.html', {'grades':gradesList})

from .models import Students
def students(request):
    studentsList = Students.stuObj.all()
    return render(request, 'myApp/students.html', {'students':studentsList})

def gredeStudent(request,num):
    grade1 = Grades.objects.get(pk=num)
    studentsList = grade1.students_set.all()
    return render(request, 'myApp/students.html', {'students':studentsList})

def addstudent(request):
    grade=Grades.objects.get(pk=1)
    stu = Students.createStudents('li_18',25,True,'我叫li_18',grade,'2018-10-25','2018-10-25')
    stu.save()
    return HttpResponse('OO')

def addstudent2(request):
    grade = Grades.objects.get(pk=1)
    stu = Students.createStudents('li_19',25,True,'我叫li_119',grade,'2018-10-25','2018-10-25')
    stu.save()
    return HttpResponse('ooo')

#显示前5条数据
def student3(request):
    studentsList = Students.stuObj.all()[0:5]
    return render(request, 'myApp/students.html', {'students':studentsList})

#分页显示
def student4(request, page):
    page = int(page)
    studentsList = Students.stuObj.all()[(page-1)*5:(page)*5]
    return render(request, 'myApp/students.html', {'students': studentsList})
#查询
from django.db.models import Max
def search(request):
    #studentsList = Students.stuObj.filter(sname__contains='li_2')
    #studentsList = Students.stuObj.filter(sname__startswith='li')
    studentsList = Grades.objects.filter(students__sname__startswith='li')
    #studentsList = Students.stuObj.aggregate(Max('sage'))
    return render(request, 'myApp/students.html', {'students': studentsList})

from django.db.models import F,Q
def FQ(request):

    # g = Grades.objects.filter(ggirlnum__lt=F('gboynum'))
    # print(g)
    Students.stuObj.filter(Q(pk__lte=3)|Q(sage__gt=50))
    return HttpResponse('00000')