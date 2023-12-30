import re

addStudent = "addStudent (?P<sID>\d{5})"
addLecturer = "addLecturer (?P<ltID>\d{5}) (?P<cIDs>(\d{5} ?)*)"
addCourse = "addCourse (?P<cID>\d{5}) (?P<unit>\d+)"
start_semester = "start semester"
register = "(?P<sID>\d{5}) register (?P<cID>(\d{5} ?)+)"
capacitate = "(?P<ltID>\d{5}) capacitate (?P<cID>\d{5}) (?P<n>\d+)"
end_registration = "end registration"
w = "W (?P<cID>\d{5}) (?P<sID>\d{5})"
mark = "(?P<ltID>\d{5}) mark (?P<cID>\d{5}) (?P<marks>((?P<sID>\d{5}) (?P<mark>\d+(\.\d+)?) ?)+)"
mark_all = "(?P<ltID>\d{5}) mark (?P<cID>\d{5}) (?P<mark>\d+) -all"
end_semester = "end semester"
showAverage = "showAverage course (?P<cID>\d{5})"
showStudentCourse = "showStudentCourse (?P<sID>\d{5})"
showCourse = "showCourse (?P<ltID>\d{5})"
showRank = "showRank (?P<cID>\d{5})"
showAverages = "showAverages (?P<sID>\d{5})"
showTopRanks = "showTopRanks (?P<n>\d+)"
showTopRanks_all = "showTopRanks -all"

cmd = input()

students = []
classes = []                
lecturers = []   

class Student:

    def __init__(self, student_id):
        #self.__class__.count += 1
        self.student_id = student_id
        self.courses = dict()
        self.unit = unit
        # print('courses creation', id(self.courses))
        students.append(self)

    def get_student(student_id):
        for student in students:
            if student_id == student.student_id:
                return student

    def add_class(self, class_id_dict,class_id_list):
        self.courses.update(class_id_dict)
        self.add_unit(class_id_list)
    
    def add_unit (self,class_id_list):
        c = 0
        for class_id in class_id_list:
            classs = Classes.get_class(class_id)
            c += classs.unit
        self.unit += c
    
    def showAverage(self):
        average = sum((self.courses.values())) / len(self.courses)
        print(average)

    def showTopRanks(self):
        x22 = 0
        c22 = 0
        for i in self.courses.values():
            if i !='':
                x22 +=i
                c22 +=1
        try :
            average = x22 / c22
            return(self.student_id,average)
        except:
            x22 = 0
            c22 = 1
            for i in self.courses.values():
                if i !='':
                    x22 +=i
                    c22 +=1
                average = x22 / c22
                return(self.student_id,average)

    def del_class(self , classs):
        del self.courses[classs.class_id]
        self.unit - classs.unit
        del classs.student_id_dict[self.student_id]
        classs.capacity = classs.capacity -1
        # پاک کردن درس با ایدی ۶۷۶۲۷۸۶ از دیکشنری
    
    def mark(self,class_id,mark):
        self.courses[class_id] = float(mark)

    def del_class2 (self,clas_id):
        del self.courses[clas_id.class_id]
        self.unit -= clas_id.unit
        print(self.unit)

class Lecturer:
    count = 0

    def __init__(self, ltID, class_id_dict={}):
        self.ltID = ltID
        self.class_id_dict = class_id_dict
        lecturers.append(self)
    
    def get_lecturer (ltID):
        for lecturer in lecturers:
            if ltID == lecturer.ltID:
                return lecturer
    def class_student(self,classs):
        self.class_id_dict[classs.class_id] = classs.student_id_dict

class Classes:
    count = 0

    def __init__( self, class_id, unit , capacity=15 ,lecturer=None ,class_mark = True ):
       
        self.class_id = class_id
        self.unit = unit
        self.capacity = capacity
        self.student_id_dict = dict()
        self.lecturer = lecturer
        self.class_mark = class_mark
        classes.append(self)

    def get_class(class_id):

        for clas in classes:
            if class_id == clas.class_id:
                return clas
            
    def add_capacity(self, n):
       
       self.capacity += n
    
    def add_lecturer(self,ltID):
        self.lecturer = ltID

    def add_student(self,student_id):
        self.student_id_dict[student_id]=''

    def capacity_min(self):
        self.capacity -= 1

    def mark_sid(self,student_id,mark):
        self.student_id_dict[student_id] = float(mark)

    def mark_all_sid(self,mark):
        for i in range(len(self.student_id_dict)):
            self.student_id_dict[i] = mark
    
    def mark_all(self):
        self.class_mark = False

    def showAverage(self):
        average = sum((self.student_id_dict.values())) / len(self.student_id_dict)
        print(average)

    def showRank(self,n=3):
        try:
            rank_dict = sorted(self.student_id_dict.items(), key=lambda x: float(x[1]), reverse=True)
            list1_ = []
            c=0
            while c < n:
                for item in rank_dict:
                    list1_.append((item[0]))
                    c +=1
            print(list1_)
        except:
            print("no mark")

    def del_class(self):
        for student_id in  self.student_id_dict.keys():
            student=Student.get_student(student_id)
            student.del_class2(self)

    def del_student(self,student):
        del classs.student_id_dict[student.student_id]
        self.capacity +=1

while re.match(start_semester, cmd) == None:

    if re.match(addStudent, cmd):
        student_id = re.match(addStudent, cmd).group("sID")
        student = Student(student_id)
        
    elif re.match(addCourse, cmd):
        class_id = re.match(addCourse, cmd).group("cID")
        unit = int(re.match(addCourse, cmd).group("unit"))
        classs = Classes(class_id, unit)
    
    elif re.match(addLecturer, cmd):
        ltID = re.match(addLecturer, cmd).group("ltID")
        class_id_list = re.match(addLecturer, cmd).group("cIDs").split()
        class_id_dict = {cid : "" for cid in class_id_list}
        lecturer = Lecturer(ltID,class_id_dict)
        for class_id in class_id_list:
            classs = Classes.get_class(class_id)
            classs.add_lecturer(ltID)        
    
    cmd = input()

while re.match(end_registration, cmd) == None:
    
    if re.match(register, cmd):
        student_id = re.match(register, cmd).group("sID")
        class_id_list = re.match(register, cmd).group("cID").split()
        class_id_dict = {cid : "" for cid in class_id_list}
        student=Student.get_student(student_id)
        student.add_class(class_id_dict,class_id_list)

        for class_id in class_id_list:
            classs = Classes.get_class(class_id)
            classs.add_student(student.student_id)
            classs.capacity_min()
       
    elif re.match(capacitate, cmd):
        ltID = re.match(capacitate, cmd).group("ltID")
        class_id = re.match(capacitate, cmd).group("cID")
        n = int(re.match(capacitate, cmd).group("n"))

        classs = Classes.get_class(class_id)
        ltID = Lecturer.get_lecturer (ltID)

        if classs.lecturer == ltID :
            classs.add_capacity(n)
        else:
            None

    cmd = input()

for courses in classes:
    if len(courses.student_id_dict) <=3:
        classes.remove(courses)
        print(courses.class_id)

while re.match(end_semester, cmd) == None:
   
    if re.match(mark, cmd):
        ltID = re.match(mark, cmd).group("ltID")
        class_id = re.match(mark, cmd).group("cID")
        marks = re.match(mark, cmd).group("marks").split()
        
        ltID= Lecturer.get_lecturer (ltID)
        
        classs = Classes.get_class(class_id)

        for i in range(len(marks)-1):
                if i % 2 == 0:
                    classs.mark_sid(marks[i], marks[i+1])
                    student = Student.get_student(marks[i])
                    student.mark(classs.class_id,marks[i+1])

                else:
                    pass
        
        # if classs.class_mark:
        #     for i in range(len(marks)-1):
        #         if i % 2 == 0:
        #             classs.mark_sid(marks[i], marks[i+1])
        #         else:
        #             pass        

        ltID.class_student(classs)
        #print(ltID.class_id_dict[classs.class_id])
        
    elif re.match(mark_all, cmd):
        ltID = re.match(mark_all, cmd).group("ltID")
        class_id = re.match(mark_all, cmd).group("cID")
        marks = int(re.match(mark_all, cmd).group("mark"))
    
        ltID= Lecturer.get_lecturer (ltID)
        classs = Classes.get_class(class_id)
        classs.mark_all_sid(marks)
        ltID.class_student(classs)

        print(ltID.class_id_dict)
        
    elif re.match(w, cmd):
        class_id = re.match(w, cmd).group("cID")
        student_id = re.match(w, cmd).group("sID")

        classs = Classes.get_class(class_id)
        student=Student.get_student(student_id)

        student.del_class(classs)
        
        
    cmd = input()

while re.match("endShow", cmd) == None:

    if re.match(showAverage, cmd):
        class_id = re.match(showAverage, cmd).group("cID")
        classs = Classes.get_class(class_id)
        classs.showAverage()

    elif re.match(showStudentCourse, cmd):
        student_id = re.match(showStudentCourse, cmd).group("sID")
        student = Student.get_student(student_id)
        print(student.courses.keys())

    elif re.match(showCourse, cmd):
        ltID = re.match(showCourse, cmd).group("ltID")
        lecturer = Lecturer.get_lecturer (ltID)
        print(lecturer.class_id_dict.keys())

    elif re.match(showRank, cmd):
        class_id = re.match(showRank, cmd).group("cID")
        classs = Classes.get_class(class_id)
        classs.showRank()

    elif re.match(showAverages, cmd):
        student_id = re.match(showAverages, cmd).group("sID")
        student = Student.get_student(student_id)
        student.showAverage()

    elif re.match(showTopRanks, cmd):
        n = int(re.match(showTopRanks, cmd).group("n"))
        c = 0
        rank_list = []
        if n < len(students):
            for student in students:
                rank = student.showTopRanks()
                rank_list.append(rank)
            sorted_list = sorted(rank_list, key=lambda x: x[1], reverse=True)
            
            for item in sorted_list:
                if c < n :
                    print(item[0])
                    c += 1              
        
    elif re.match(showTopRanks_all, cmd):
        rank_list = []
        if n < len(students):
            for student in students:
                rank = student.showTopRanks()
                rank_list.append(rank)
            sorted_list = sorted(rank_list, key=lambda x: x[1], reverse=True)
            
            print(sorted_list)
                

           
    cmd = input()

