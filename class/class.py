import math

from abc import ABC, abstractmethod

'''
class Person:
    # 构造函数，在创建实例的时候会自动调用
    # 在__init__里初始化的属性都是实例属性
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def getName(self):
        print("your name is ",self.name)


# 使用dir()可以查看一个类的所有属性
# print(dir(Person))
# 特殊的类属性   __dict__,__name__等等
'''


'''
# 组合是 拥有关系，即一个类以另一个类的实例作为属性
# 而继承是 是关系
# 因此可以使用多个简单的类来组合成一个复杂的类
class Circle:
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return math.pi*self.radius**2


class Ring:
    def __init__(self,outside_radius,inside_radius):
        self.inside_radius = Circle(inside_radius)
        self.outside_radius = Circle(outside_radius)

    def area(self):
        return self.outside_radius.area() - self.inside_radius.area()

circle = Circle(1)
ring = Ring(2,1)
print(ring.area)
print(type(circle.radius))
print(type(ring.inside_radius))

'''


'''
# 子类重写父类的方法,默认为虚方法，因此可以实现多态
# 如果需要调用父类的方法，可以使用类名打点调用，也可以使用super方法
# 如果不想让子类覆盖父类的方法

class Student(Person):
    def __init__(self, name, age,id):
        super().__init__(name, age)
        self.id = id

    def getName(self):
        super().getName()
        print("you are a student")

student = Student('wtr',19,'b24051005')
student.getName()
'''


'''
# 在实际开发中，一些派生类需要实现对应的功能，但是不同开发者命名不同，导致最后无法实例化
# 所以需要设计接口类，强制所有派生类必须重写该方法

class Animal(ABC):
    # 子类必须重写 abstractmethod修饰的抽象方法
    @classmethod
    @abstractmethod
    def eat(self):
        pass

class Dog(Animal):
    def bark(self):
        print('big dog bark bark bark')

    def eat(self):
        print('dogs like eating bone')

dog = Dog()
dog.bark()
'''


# property
class Teacher():
    def __init__(self,name,age):
        self.__name = name
        self.age = age
    
    def getName(self):
        print('get')
        return self.__name

    def setName(self,new_name):
        print('set')
        self.__name = new_name

    def delName(self):
        print('delete')
        del self.__name

    # 定义property，关联get,set,del
    name = property(getName,setName,delName)

teacher = Teacher('mf',40)
teacher.name
teacher.name = 'lse'
del teacher.name
