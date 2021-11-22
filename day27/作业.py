class Student:
    def __init__(self, name, age, number, sex, school):
        self.choices = []
        self.name = name
        self.age = age
        self.number = number
        self.sex = sex
        self.school = school

    def choose(self, course):
        self.choices.append(course)


class Class:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.course = None

    def relate(self, course):
        self.course = course

    def tell_class(self):
        print('%s' % self.name, end=" ")
        self.course.tell_course()


class Course:
    def __init__(self, name, period, price):
        self.name = name
        self.period = period
        self.price = price

    def tell_course(self):
        print(f"课程{self.name}周期为{self.period}，价格为{self.price}")


class School:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.classes = []

    def add_class(self, cls):
        self.classes.append(cls)

    def tell_class(self):
        print(self.name.center(60, '='))
        for each in self.classes:
            each.tell_class()


class Teacher:
    def __init__(self, name, age, salary, level):
        self.name = name
        self.age = age
        self.salary = salary
        self.level = level

    def score(self, name, grade):
        print("老师%s正在为学生%s打%d分" % (self.name, name, grade))


school_obj1 = School('老男孩魔都校区', '上海')
school_obj2 = School('老男孩帝都校区', '北京')
class_obj1 = Class('脱产14期', '老男孩魔都校区')
class_obj2 = Class('脱产15期', '老男孩魔都校区')
class_obj3 = Class('脱产29期', '老男孩帝都校区')
course_obj1 = Course('python全栈开发', '6mons', 20000)
course_obj2 = Course('linux运维', '5mons', 18000)
class_obj1.relate(course_obj1)
class_obj2.relate(course_obj2)
class_obj3.relate(course_obj1)
school_obj1.add_class(class_obj1)
school_obj1.add_class(class_obj2)
school_obj2.add_class(class_obj3)
school_obj1.tell_class()
school_obj2.tell_class()
