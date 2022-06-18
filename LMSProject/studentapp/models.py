from django.db import models

# Create your models here.

class dept(models.Model):
    dept_name = models.CharField(max_length=100)
    def __str__(self):
        return self.dept_name
    
class Students(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField()
    email = models.EmailField()
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    department = models.ForeignKey(dept, on_delete=models.CASCADE)
    rollno = models.IntegerField()
    admityear = models.IntegerField()

    def __str__(self):
        return self.name


