# 装饰器的使用
# 使用@property来设置getter和setter方法，getter只能够获取数据，使用setter方法来设置变量，其余地方无法修改变量
class Person(object):
    def __init__(self, name, age):
        self._name = name
        self._age = age


    # 访问器
    @property
    def name(self):
        return self._name 
    
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, age):
        self._age = age
    
    def play(self):
        if self._age <= 16:
            print("%s 正在玩飞行棋" %self._name)
        else:
            print("%s 正在上班" % self._name)

from time import time, localtime, sleep

class Clock(object):
    """数字时钟"""

    def __init__(self, hour=0, minute=0, second=0):
        self._hour = hour
        self._minute = minute
        self._second = second
    @classmethod
    def now(cls):
        ctime = localtime(time())
        return cls(ctime.tm_hour, ctime.tm_min, ctime.tm_sec)

    def run(self):
        """走字"""
        self._second += 1
        if self._second == 60:
            self._second = 0
            self._minute += 1
            if self._minute == 60:
                self._minute = 0
                self._hour += 1
                if self._hour == 24:
                    self._hour = 0

    def show(self):
        """显示时间"""
        return '%02d:%02d:%02d' % \
               (self._hour, self._minute, self._second)
    
class Student(Person):
    """学生"""

    def __init__(self, age, name, grade):
        super().__init__(name, age)
        self._grade = grade

    @property
    def grade(self):
        return self._grade
    
    @grade.setter
    def grade(self, grade):
        self._grade = grade
    
    def study(self, course):
        print('%s的%s正在学习%s' % (self._grade, self._name, course))

class Teacher(Person):
    """教师"""
    def __init__(self, age, name, title):
        super().__init__(name, age)
        self._title = title
    
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title

    
    def teach(self, course):
        print('%s%s正在教%s' % (self._name, self._title, course))


from abc import ABCMeta, abstractmethod

class Pet(object, metaclass=ABCMeta):

    def __init__(self, nickname):
        self._nickname = nickname

    # 定义一个抽象方法
    @abstractmethod
    def make_voice(self):
        """发出声音"""
        pass

class Dog(Pet):
    def make_voice(self):
        print("%s: 汪汪汪。。。" %self._nickname)

class Cat(Pet):
    def make_voice(self):
        print("%s: 喵喵喵。。。" %self._nickname)


    


def main():
    stu = Student(16, '王大锤', '初二')
    stu.study('数学')
    stu.play()
    t = Teacher(35, 'moss','教授')
    t.teach('计算机课')
    pets = [Dog('旺财'), Cat('桃酥'), Cat('大饼')]
    for pet in pets:
        pet.make_voice()


    # person.name = '白元芳'  # AttributeError: can't set attribute
    # person.age = 22
    # person.play()
    # 通过类方法创建对象并获取系统时间
    # clock = Clock.now()
    # while True:
    #     print(clock.show())
    #     sleep(1)
    #     clock.run()

    

if __name__ == '__main__':
    main()
