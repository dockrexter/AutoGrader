from django.shortcuts import render
from django.conf.urls import url
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from .models import home_student_record,home_teacher_record,uploaded_files
from .forms import UploadFileForm
# Create your views here.
def handle_uploaded_file(f):
    with open('some/file/name.txt', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


# def assignment_upload(request):
#     if request.method == 'POST':
#         form = UploadFileForm(request.POST, request.FILES)
#         if form.is_valid():
#             file =handle_uploaded_file(request.FILES['teachertestfile'])
#             file.save()
            
#             return HttpResponse('uploaded')

#         else:
#             return HttpResponse('file not uploaded')
#     else:
#         form = UploadFileForm()
#     return render(request,'home/assignment_upload.html')


def assignment_upload(request):
    if request.method == 'POST':
        question_file = request.FILES['questionfile']
        uploaded_files1=uploaded_files(zipFile=question_file)
        uploaded_files1.save()
        return HttpResponse('uploaded')
        # teacher_test_file = request.FILES['teachertestfile']
        # student_test_file = request.FILES['studenttestfile']
    else:
        return render(request,'home/assignment_upload.html')

def check_login(request):
    if request.method == 'GET':
            
        l = home_student_record.objects.all()
        for p in home_student_record.objects.raw('SELECT * FROM home_home_student_record'):
            print(p)
        for i in l:
            print(i.email,i.password)
            if(i.password==request.GET["password"] and i.email==request.GET["email"]):
                print("yes")
                return HttpResponse('Success full login')
            else:
                return HttpResponse('wrong password or email')


    
def index(request):
    return render(request,'home/index.html')
def signup(request):
    return render(request,'home/signup.html') 
def login(request):
      return render(request,'home/login.html') 
def teacher_index(request):
      return render(request,'home/teacher_index.html') 
def teacher_login_l(request):
      return render(request,'home/teacher_login.html') 
def teacher_signup(request):
      return render(request,'home/teacher_signup.html') 


def teacher_signup(request):
    if request.method == 'POST':
        print("hello")
        #check_login(request)
        email=request.POST["email"]
        password=request.POST["password"]
        teacher_record=home_teacher_record(email=email,password=password)
        teacher_record.save()
        return HttpResponseRedirect('/home/')
    else:
        return render(request,'home/teacher_signup.html') 



def add_signup(request):
    if request.method == 'POST':  
        print("hello")
        #check_login(request)
        email=request.POST["email"]
        password=request.POST["password"]
        studentrecord=home_student_record(email=email,password=password)
        studentrecord.save()
        return HttpResponseRedirect('/home/')


def teacher_login(request):
    
    if request.method == 'GET':

        l = home_teacher_record.objects.all()
        for p in home_teacher_record.objects.raw('SELECT * FROM home_home_teacher_record'):
            print(p)
        for i in l:
            print(i.email,i.password)
            if(i.password==request.GET["password"] and i.email==request.GET["email"]):
                print("yes")
                return HttpResponseRedirect('/home/assignment_upload')

            else:
                return HttpResponse('wrong password or email')