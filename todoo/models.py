from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class todooses(models.Model):
    task_name=models.CharField(max_length=70,unique=True)
    options=(("completed","completed"),("not completed","not completed"))
    status=models.CharField(max_length=15,choices=options,default="not completed")
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.task_name
