from timeit import timeit

''''
# 创建一个列表
def with_for():
    lst = []
    for i in range(100):
        lst.append(2*i) 
    return lst

def with_comprehension():
    return [2*i for i in range(100)]

def with_generator():
    return (2*i for i in range(100))

print(f'with_for:{timeit(with_for,number=10000)}')
print(f'with_comprehension:{timeit(with_comprehension,number=10000)}')
print(f'with_generator:{timeit(with_generator,number=10000)}')

# 列表生成器的速度明显快于for loop，原因在于append需要先在lst里找到append的方法，而使用列表生成器可以直接调用该方法
# 还可以发现生成器的速度快了1个数量级，原因在于generetor的惰性，在调用的时候才会计算元素的值
'''


'''
# 能用built in 函数尽量不要自己实现，因为built in 函数底层用c实现

# any:检测是否有元素满足
# all:检测是否所有元素都满足
lst = [2*i for i in range(100)]

def with_for():
    for num in lst:
        if num > 50:
            return True
    return False

def with_any():
    return any(lst)
# 如果把这里换成列表生成式或者生成器都会降低速率，毕竟没有现成的块
# 列表生成式会先把列表生成完毕,然后传递给any,而生成器会一个一个生成.直到有满足的

print(f'with_for:{timeit(with_for,number=10000)}')
print(f'with_any:{timeit(with_any,number=10000)}')
'''

'''
# 实现判断功能，如果列表中元素大于一个值就放入列表
# filter函数第一个参数是一个判断函数，第2个是iterable,返回值是generator
lst = [i for i in range(10)]
def bigger(num):
    return num>=50

def with_comprehension():
    return [n for n in lst if bigger(n)]

def with_filter():
    return filter(bigger,lst)
'''

'''
# map函数:映射,可以接受多个参数
# 我要实现将2个列表的元素对应相加
lst1 = [i for i in range(10)]
lst2 = [2*i for i in range(10)]
def add(num1,num2):
    return num1+num2

def with_map():
    return map(add,lst1,lst2)

# 使用生成器就有些冗长
def without_map():
    return (add(lst1[i],lst2[i]) for i in range(len(lst1)))
'''

# zip可以将几个iterable组合在一起，返回一个元组的generator
ids = ['1005','1006','1007']
ages = [18,19,18]
names = ['wtr','wjx','msy']

def with_zip():
    for name,age,id in zip(names,ages,ids):
        print(name,age,id)