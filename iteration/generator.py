# 生成器和迭代器有很多相似处，比如都可以使用Next函数取出当前元素指向下一元素，都可以放在for _ in 后面

# iterator是一个类的实例，他会把当前迭代的状态保存在对象里的一个变量
# 而generator直接保存生成器函数的状态

# 这是一个生成器函数
# 函数内部有yield就不会当作普通函数
def gen(num):
    while num>0:
        yield num
        num -= 1
    return 

# 返回一个生成器对象
g = gen(5)

# for循环就是不断指向g的下一位，即对g使用next函数
# 对生成器对象使用next函数才会执行函数，当进行到yield时会返回当前的num，然后函数按下暂停键，直到下一次next
for i in g:
    print(i)


# 用生成器实现链表
class Node():
    def __init__(self,name):
        self.name = name
        self.next = None

    def __iter__(self):
        node = self
        while node is not None:
            yield node
            node = node.next

# 将3个节点连成链表
node1 = Node("node1")
node2 = Node("node2")
node3 = Node("node3")
node1.next = node2
node2.next = node3

for node in node1:
    print(node.name)