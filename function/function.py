# 函数传参的几种方式：位置，默认值，关键字，包裹位置，包裹关键字传递

# 参数的包裹和解包裹
# 有的时候不知道传递参数的具体数量，就可以通过包裹来传递

'''
# 在本函数中，在定义的参数前加上*提示解释器这是元组名，所有传入的参数被收集并合成一个元组
def func1(*tuples):
    print(type(tuples))
    print(tuples)

# 使用**则表示是字典类型
def func2(**dirs):
    print(type(dirs))
    print(dirs)

func1(1,2,3)
func2(m=1,n=2,t=3)


# 与定义时类似，在调用时可以使用*或**解包裹
t = ['hello','world','python']
d = {'a':2,'b':4,'c':6}
func1(*t)
func2(**d)
'''


# 闭包机制，内层函数可以使用外层函数内定义的变量
# 不同于普通的函数，函数内是局部变量，函数执行完后就被销毁    ，闭包会保存外层函数的变量，直到该函数被销毁
# 这得益于yield函数的使用
def g():
    lst :list[int] = []
    def app(value):
        lst.append(value)

        return lst
    return app
    
f = g()
print(f(1))
print(f((2,3)))
