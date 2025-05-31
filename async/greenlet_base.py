# 协程，又称微线程，是比线程更小的执行单元。协程是用户态的，线程是内核态的。
# 协程的切换不需要内核的参与，切换速度快，开销小。
# 协程的切换是通过用户态的调度器来完成的，线程的切换是通过内核态的调度器来完成的。
# 协程的切换是通过保存和恢复上下文来完成的，线程的切换是通过保存和恢复上下文来完成的。

# greenlet是python的一个协程库，它是一个轻量级的协程库，使用C语言实现，性能比python的内置协程库asyncio要高。
import greenlet

def foo():
    print("foo start")    #第2步
    gl_bar.switch()        #第3步，切换到bar函数，保留foo函数的执行状态
    print("foo end")      #第6步

def bar():
    print("bar start")      #第4步
    gl_foo.switch()         #第5步，切换到foo函数，保留bar函数的执行状态
    print("bar end")       #第7步

 
if __name__ == "__main__":
    gl_foo = greenlet.greenlet(foo)
    gl_bar = greenlet.greenlet(bar)
    gl_foo.switch()    #第1步，切换到foo函数
