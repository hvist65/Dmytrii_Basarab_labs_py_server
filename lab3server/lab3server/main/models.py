from django.db import models

# Create your models here.


class Class(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 20)
    number_of_students = models.IntegerField(null = True)
    average_mark = models.IntegerField(null=True)

class Student(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 100)
    surname = models.CharField(max_length = 100)
    class_id = models.ForeignKey(Class,on_delete=models.CASCADE)
    phone = models.CharField(max_length = 20,null = True)
    email= models.CharField(max_length=100)
   
class Lesson(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 100)
    credits = models.IntegerField()
    term = models.IntegerField()

class Lesson_time(models.Model):
    id = models.AutoField(primary_key = True)
    start_time = models.TimeField()
    end_time = models.TimeField()

class Room(models.Model):
    id = models.AutoField(primary_key = True)
    number_of_room = models.IntegerField()
    floor = models.IntegerField()

class Teacher(models.Model):
    id = models.AutoField(primary_key = True)
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    class_id = models.ForeignKey(Class,on_delete=models.CASCADE)
    phone = models.CharField(max_length = 20,null = True)
    email= models.CharField(max_length=100)
    own_room_id = models.ForeignKey(Room,on_delete=models.CASCADE,null = True)

class Shedule(models.Model):
    id = models.AutoField(primary_key = True)
    day = models.CharField(max_length = 20)
    lesson_id = models.ForeignKey(Lesson,on_delete=models.CASCADE)
    class_id = models.ForeignKey(Class,on_delete=models.CASCADE)
    teacher_id = models.ForeignKey(Teacher,on_delete=models.CASCADE)
    room_id = models.ForeignKey(Room,on_delete=models.CASCADE)
    time_id = models.ForeignKey(Lesson_time,on_delete=models.CASCADE)
