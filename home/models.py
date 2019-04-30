from django.db import models
# Create your models here.
class home_student_record(models.Model):
    email=models.CharField(max_length=200)
    password=models.CharField(max_length=50)


class home_teacher_record(models.Model):
    email=models.CharField(max_length=200)
    password=models.CharField(max_length=50)

class uploaded_files(models.Model):
    zipFile = models.FileField()
