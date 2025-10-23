import os
import django


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lab3server.settings')  
django.setup()
from main.models import Class, Student, Lesson, Lesson_time, Room, Teacher, Shedule
from main.repositories import UnitOfWork

uow = UnitOfWork()
cl = uow.klass.add("11A",30,0)
st = uow.student.add("Andrii","Fir",cl,"0986","and@gmail")
st2 = uow.student.add("Ara","Fiodos",cl,"0987","fira@gmail")
room = uow.room.add(215,2)

print(uow.student.get_by_id(2))
print(uow.klass.get_by_id(1))
print(uow.room.get_by_id(1))

print(uow.student.get_all())
print()
print(uow.klass.get_all())
print()
print(uow.room.get_all())
print()
print(uow.teacher.get_all())
