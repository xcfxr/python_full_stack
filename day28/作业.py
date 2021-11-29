import os.path
import uuid
import pickle
BASE_PATH = os.path.dirname(__file__)


class BaseMixin:
    def save_obj(self):
        dir_path = os.path.join(BASE_PATH, self.__class__.__name__)
        if not os.path.exists(dir_path):
            os.mkdir(dir_path)
        save_path = os.path.join(dir_path, self.id)
        with open(save_path, 'wb') as f:
            pickle.dump(self, f)

    @classmethod
    def load_obj(cls, id_num):
        dir_path = os.path.join(BASE_PATH, cls.__name__)
        if not os.path.exists(dir_path):
            os.mkdir(dir_path)
        load_path = os.path.join(dir_path, id_num)
        with open(load_path, 'rb') as f:
            return pickle.load(f)


class Student:
    def __init__(self, name, age, sex, school):
        self.choices = []
        self.name = name
        self.age = age
        self.id = str(uuid.uuid4())
        self.sex = sex
        self.school = school
        self.number = uuid.uuid4()

    def choose(self, course):
        self.choices.append(course)


class Class(BaseMixin):
    def __init__(self, name, school):
        self.id = str(uuid.uuid4())
        self.name = name
        self.school = school
        self.course = None

    def relate(self, course):
        self.course = course.id
        self.save_obj()

    def tell_class(self):
        print('%s' % self.name, end=" ")
        course_obj = Course.load_obj(self.course)
        course_obj.tell_course()


class Course(BaseMixin):
    def __init__(self, name, period, price):
        self.name = name
        self.period = period
        self.__price = price
        self.id = str(uuid.uuid4())
        self.save_obj()

    def tell_course(self):
        print(f"课程{self.name}周期为{self.period}，价格为{self.__price}")

    def get_price(self):
        return self.__price

    def set_price(self, val):
        self.__price = val

    def del_price(self):
        del self.__price

    price = property(get_price, set_price, del_price)


class School(BaseMixin):
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.classes = []
        self.id = str(uuid.uuid4())
        self.save_obj()

    def add_class(self, cls_obj):
        self.classes.append(cls_obj.id)
        self.save_obj()

    def tell_class(self):
        for each in self.classes:
            cls_obj = Class.load_obj(each)
            cls_obj.tell_class()


class Teacher(BaseMixin):
    def __init__(self, name, age, salary, level):
        self.name = name
        self.age = age
        self.__salary = salary
        self.level = level
        self.id = str(uuid.uuid4())
        self.save_obj()

    def score(self, name, grade):
        print("老师%s正在为学生%s打%d分" % (self.name, name, grade))

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, salary):
        self.__salary = salary

    @salary.deleter
    def salary(self):
        print('无法删除')


# school_obj1 = School('老男孩魔都校区', '上海')
# school_obj2 = School('老男孩帝都校区', '北京')
# class_obj1 = Class('脱产14期', '老男孩魔都校区')
# class_obj2 = Class('脱产15期', '老男孩魔都校区')
# class_obj3 = Class('脱产29期', '老男孩帝都校区')
# course_obj1 = Course('python全栈开发', '6mons', 20000)
# course_obj2 = Course('linux运维', '5mons', 18000)
# class_obj1.relate(course_obj1)
# class_obj2.relate(course_obj2)
# class_obj3.relate(course_obj1)
# school_obj1.add_class(class_obj1)
# school_obj1.add_class(class_obj2)
# school_obj2.add_class(class_obj3)
# school_obj1.tell_class()
# school_obj2.tell_class()
# tea_obj = Teacher('xucee', 18, 20000, '教授')
tea_obj = Teacher.load_obj('6d0f61b1-1c3e-4552-8eea-607b1d6c38c3')
print(tea_obj.salary)
tea_obj.salary = 2000
print(tea_obj.salary)
del tea_obj.salary
print(tea_obj.salary)
course_obj = Course.load_obj('54ec65d7-eef9-4f15-83bf-10896a1d09eb')
print(course_obj.__dict__)
course_obj.price = 2000
print(course_obj.price)