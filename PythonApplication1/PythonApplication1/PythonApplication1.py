

class Student:

    def __init__(self,name,surname,phone):
        self._name = name
        self._surname = surname
        self._phone = phone
        self._extracurricular_lesson_id = []
        self._email = None
        self._mark=0
        self._class_id = None    
        print("Student created")

    def printinfo(self):
        print(self._name,self._surname,self._class_id,self._phone,self._email,self._extracurricular_lesson_id)

    def set_email(self,email):
        self._email=email

    def set_extracurricular_lesson_id(self,extracurricular_lesson_id):
        self._extracurricular_lesson_id.append(extracurricular_lesson_id)

    def set_mark(self,mark):
        self._mark=mark








class TeacherAssist():
    def __init__(self):
        self._announcement = 12
        print("TeacherAssist created")

    def printinfo(self):
        print(f"teacher set!!!!!!!!!!!!! announcement {self._announcement}")




class Starosta(Student,TeacherAssist):
    def __init__(self,name,surname,phone):
        Student.__init__(self,name,surname,phone)
        TeacherAssist.__init__(self)
        print("Starosta created")

    def printinfo(self):
        print("The teacher announcment is", self._announcement) 



    


class Class:

    #_number_of_students = 0
    def __init__(self,name):
        self._name = name
        self._average_mark = 0
        self._students_list = []
        
    def addstudent(self,Student):
        self._students_list.append(Student)
        Student._class_id = self._name
        print(f"Student {Student._name} added to {self._name}")
        

    def removestudent(self,Student):
        self._students_list.remove(Student)
        print(f"Student {Student._name} removed from {self._name}")

    def print_average_mark(self):
        sum=0
        for i in self._students_list:
            sum+=i._mark
        sum/=len(self._students_list)
        _average_mark = sum
        print(_average_mark)

    def printinfo(self):
        print(self._name)
        for i in self._students_list:
            i.printinfo()


            
            


    @staticmethod
    def showshedule():
        print("""        1 lection:8.30 - 9.50
        2 lection:10.05 - 11.25
        3 lection:11.40 - 13.00
        4 lection:13.10 - 14.40""")
        
    


        



s1 = Student("Nadya","Lud","0988832896")
s2 = Student("Bodya","Piluk","0954949304")
s1.set_mark(100)
s2.set_mark(50)
s1.printinfo()
s2.printinfo()
c=Class("9-A")
Class.showshedule()
c.addstudent(s1)
c.addstudent(s2)
c.print_average_mark()
c.printinfo()
st=Starosta("Maks","Fraud","0975485434")
c.addstudent(st)
st.printinfo()

    

