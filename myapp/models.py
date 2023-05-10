from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=100)
    s_id = models.IntegerField()
    date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=100)
    course = models.CharField(max_length=100) 
    teacher = models.CharField(max_length=100)
    performance = models.CharField(max_length=100)
    typ_work = models.CharField(max_length=100)
    jour_name_place = models.CharField(max_length=200)


    def __str__(self):
        return self.name + ","+str(self.s_id)+","+str(self.status)