from main.models import Class, Student, Lesson, Lesson_time, Room, Teacher, Shedule

class StudentRepository():
    @staticmethod
    def get_all():
        return Student.objects.all().values('name')

    def get_by_id(self,id):
        try:
            return Student.objects.get(pk = id).name
        except Student.DoesNotExist:
            return None

    def add(self,name,surname,class_id,phone,email):
        entity = Student(name=name,surname=surname,class_id=class_id,phone=phone,email=email)
        entity.save()

class ClassRepository:
    @staticmethod
    def get_all():
        return Class.objects.all().values('name')
    
    def get_by_id(self, id):
        try:
            return Class.objects.get(pk=id).name
        except Class.DoesNotExist:
            return None

    def add(self,name, number_of_students, average_mark):
        entity = Class(name = name,number_of_students=number_of_students, average_mark=average_mark)
        entity.save()
        return entity

class LessonRepository:
    def get_all(self):
        return Lesson.objects.all()
    
    def get_by_id(self, id):
        try:
            return Lesson.objects.get(pk=id)
        except Lesson.DoesNotExist:
            return None

    def add(self, name, credits, term):
        entity = Lesson(name=name, credits=credits, term=term)
        entity.save()
        return entity

class LessonTimeRepository:
    def get_all(self):
        return Lesson_time.objects.all()
    
    def get_by_id(self, id):
        try:
            return Lesson_time.objects.get(pk=id)
        except Lesson_time.DoesNotExist:
            return None

    def add(self, start_time, end_time):
        entity = Lesson_time(start_time=start_time, end_time=end_time)
        entity.save()
        return entity

class RoomRepository:
    def get_all(self):
        return Room.objects.all().values('number_of_room')
    
    def get_by_id(self, id):
        try:
            return Room.objects.get(pk=id).number_of_room
        except Room.DoesNotExist:
            return None

    def add(self, number_of_room, floor):
        entity = Room(number_of_room=number_of_room, floor=floor)
        entity.save()
        return entity


class TeacherRepository:
    def get_all(self):
        return Teacher.objects.all()
    
    def get_by_id(self, id):
        try:
            return Teacher.objects.get(pk=id)
        except Teacher.DoesNotExist:
            return None

    def add(self, first_name, last_name, class_id, phone, email, own_room_id=None):
        entity = Teacher(
            first_name=first_name,
            last_name=last_name,
            class_id=class_id,
            phone=phone,
            email=email,
            own_room_id=own_room_id
        )
        entity.save()
        return entity


class SheduleRepository:
    def get_all(self):
        return Shedule.objects.all()
    
    def get_by_id(self, id):
        try:
            return Shedule.objects.get(pk=id)
        except Shedule.DoesNotExist:
            return None

    def add(self, day, lesson_id, class_id, teacher_id, room_id, time_id):
        entity = Shedule(
            day=day,
            lesson_id=lesson_id,
            class_id=class_id,
            teacher_id=teacher_id,
            room_id=room_id,
            time_id=time_id
        )
        entity.save()
        return entity

class UnitOfWork:
    def __init__(self):
        self.student=StudentRepository()
        self.klass = ClassRepository()
        self.lesson = LessonRepository()
        self.lessontime = LessonTimeRepository()
        self.room = RoomRepository()
        self.teacher = TeacherRepository()
        self.shedule = SheduleRepository()