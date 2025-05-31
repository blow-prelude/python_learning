# 定义一个全局变量，如果在局部作用域内被读取，这是可行的。  但是如果对其进行赋值就会报错
# 这是可以在局部作用域内global申明

'''
count = 0

def f():
    global count
    count+=1
    print(count)

f()
'''