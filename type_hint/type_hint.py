# 类型注释，可以在编译的时候就能检查到错误

def add(lst) :
    for i in range(len(lst)):
        sum+=lst[i]
    return sum

s = add([1,2,'python'])

# 上述情况，如果把列表里的每个元素都设置为int类型，就可以防患于未然
def add_list(lst : list[int]) -> int:
    for i in range(len(lst)):
        sum+=lst[i]
    return sum

s =add_list([1,2,3])