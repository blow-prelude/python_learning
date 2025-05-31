# 简单区分一下同步和异步，阻塞和非阻塞
# 阻塞和非阻塞是对于一个线程来说，是否需要等待，而同步和异步是对于2个线程之间的关系

# 并行和并发
# 并发是指一个时间段几个程序在一个处理机上运行,但是同一时间只能运行一个程序
# 并行是不同的cpu运行不同的线程,即可以同时处理多个任务


import asyncio
import time


'''
def delay():
    print("start delay")
    # 这是io密集型操作，模拟耗时操作比如等待网络传输，数据库返回数据等等，cpu在等待没事做
    # io密集型操作使用协程可以提高性能
    time.sleep(1)
    # 而对于cpu密集型操作，可以使用多线程，多进程，分布式等进行优化
    
def main():
    start_time = time.time()
    for i in range(5):
        delay()
    end_time = time.time() 
    print("end_time-start_time: ", end_time - start_time)   

main()
'''



'''
# 实现异步，事件循环会创建和记录任务，一旦该任务不需要等待就会被取出并执行其中的协程
# 一个任务中可以有多个协程


# 在函数前加上async关键字，表示这是一个异步函数，即协程
async def delay():
    taskarr = []
    for i in range(5):
        print(f"{str(i)} start sleep")
        # 使用await关键字等待异步操作完成，即让出控制权
        # sleep_coro = asyncio.sleep(1)
        # await asyncio.create_task(sleep_coro)

        # 以上两行代码可以直接用await一个协程实例并自动创建任务
        await asyncio.sleep(1)


        # 当然上述代码也是依次执行5个循环里的sleep，可以参考main函数里的写法，把每个sleep都设置为任务并放在一个任务列表里
    #     sleep_coro = asyncio.sleep(1)
    #     taskarr.append(asyncio.create_task(sleep_coro))
    # await asyncio.gather(*taskarr)


# 在函数前加上async关键字，就会返回一个代表该函数的协程实例
async def main():
    start_time = time.time()
    tasks = []
    for j in range(5):
        # print(f"{str(j)}")
        # 调用协程函数，返回一个协程对象
        delay_coro = delay()
        tasks.append(asyncio.create_task(delay_coro))
        # 需要确保的是，在所有任务完成之前，主函数不会退出
        # 需要用await关键字来等待协程对象的完成

    
    # for j,t in enumerate(tasks):
    #     print(f"{str(j)}")
    #     # 如果当前任务已经完成，await会直接返回
    #     # 如果当前任务没有完成，await会让出控制权，去执行其他可执行的任务
    #     await t
    

    # 等待所有任务完成，可以使用asyncio.gather()函数等待一系列的任务
    print(await asyncio.gather(*tasks))
    # 返回值是一个列表，包含所有任务的返回值

    end_time = time.time()
    print("end_time-start_time: ", end_time - start_time)


# asyncio.run()函数会创建一个事件循环，并运行指定的协程对象
# run函数会为传进的协程创建一个任务，然后运行它
main_coro = main()
asyncio.run(main_coro)
'''


'''
# async库提供了一些同步操作的异步版本
# 假如有一个对象需要初始化，在初始化完成之前不能进行其他操作
# 可以使用asyncio.event()等待该操作执行完毕
async def delay(init_event):
    # 异步操作，释放所有控制权，直到event被触发
    await init_event.wait()

    print("enter delay")
    await asyncio.sleep(delay=1)
    print("exit delay")

async def main():
    tasks = []
    init_event = asyncio.Event()
    for i in range(5):
        sleep_coro = delay(init_event)
        tasks.append(asyncio.create_task(sleep_coro))
    await asyncio.sleep(1)
    print("init Done...")
    # 触发事件，解除所有任务的阻塞状态
    init_event.set()
    await asyncio.gather(*tasks)

asyncio.run(main())
'''






'''
# await的几大功能 : 如果是协程,就会先把该协程包装成任务,然后交出控制权,等执行完成后返回值

# asyncio.run  会把参数里的corroutine 打包成task，并创建一个event loop
# 此时事件循环里只有一个任务就是main ， 此时执行main函数
# 执行到await say_after(1) 时,把这个coroutine function 变成一个coroutine object ,再变成 task,放入event loop 里
# 这时main函数等待该函数,并交还了控制权给event loop  .此时event loop 里有2个task
# 然后event loop 运行say_after(1),到了  await asyncio.sleep(delay) 继续把这个coroutine 变成task 并交给 event loop 
# say_after()等待sleep ,并且交还了控制权,此时有3个task,但是都运行不了,直达1s后sleep完成,此时say_after可以运行了,控制权交给了他
async def say_after(delay):
    await asyncio.sleep(delay)
    print('hello')

async def main():
    print(f'start at {time.strftime('%X')}')
    await say_after(1)
    await say_after(2)
    print(f'end at {time.strftime('%X')}')

asyncio.run(main())
'''


# 上述方式分别等待了2个say_after,因为await做的事情太多了    可不可以同时等待呢

# 使用 create_task 时,把say_after 包装成task 并注册到event loop里,此时控制权还在main,继续执行
# 运行到 await task1 ,main等待task1,并交出控制权,此时 控制权交给了say_after(1) ,直到await sleep .再次交出控制权
# 在等待期间,此时event loop 里还有一个task2 ,控制权交给了task2 , 然后运行到sleep处继续等待

async def say_after(delay):
    await asyncio.sleep(delay)
    print('hello')

async def main():
    print(f'start at {time.strftime('%X')}')
    task1 = asyncio.create_task(say_after(1))
    task2 = asyncio.create_task(say_after(2))
    await task1
    await task2
    print(f'end at {time.strftime('%X')}')

asyncio.run(main())
        

# 上面一个一个的await太麻烦了,可以使用asyncio.gather
# 这个函数的参数可以是coroutine, task ,甚至可以是其返回值 future
# await   gather 的返回值 future时,就相当于告诉 event loop ,要等待所有task完成   同时把所有task的返回值放入一个列表,顺序和填入参数的顺序一致

# 如果参数是coroutine,gather 会先把coroutine变成task,  然后await的时候,main才交出控制权, 然后执行task1等等 不再赘述