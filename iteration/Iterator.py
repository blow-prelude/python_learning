# iterator 是迭代器，可以指向下一个对象
# iterable 是一个可迭代对象，可以提供iterator
# 两者配合可以实现指针的效果

# 实现一个链表

# 这个类是链表的一个单元，相当于一个iterator,可以指向iterabler的下一个元素
class NodeIter():
    def __init__(self,node):
        self.curr_node = node

    def __next__(self):
        if self.curr_node is None:
            raise StopIteration
        node,self.curr_node = self.curr_node,self.curr_node.next
        return node

# 这个类是链表或者其表头，相当于一个iterable，可以产生iterator
class Node():
    def __init__(self,name):
        self.name = name
        self.next = None

    def __iter__(self):
        return NodeIter(self)
    
# 将3个节点连成链表
node1 = Node("node1")
node2 = Node("node2")
node3 = Node("node3")
node1.next = node2
node2.next = node3

# for语句触发node1 的 __iter__方法，返回一个iterator
# 每次循环调用iterator __next__方法，返回当前节点并指向下一位
for node in node1:
    print(node.name)

