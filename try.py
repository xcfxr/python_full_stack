class Course():
    def __init__(self, name, period, price):
        self.name = name
        self.period = period
        self.__price = price

    def tell_course(self):
        print(f"课程{self.name}周期为{self.period}，价格为{self.__price}")

    def get_price(self):
        return self.__price

    def set_price(self, val):
        self.__price = val

    def del_price(self):
        del self.__price

    price = property(get_price, set_price, del_price)
course_obj1 = Course('python全栈开发', '6mons', 20000)
course_obj1.price

