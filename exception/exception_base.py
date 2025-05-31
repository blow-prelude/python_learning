# 完整结构：
# try
# except
# else
# finally
# 执行try中的代码发生异常时执行except中的代码，否则执行else中的代码
# finally中的代码无论是否发生异常都会执行

# except后面可以跟多个异常类型，也可以跟万能的exception表示处理所有异常
# except后面可以跟异常对象，表示捕获异常对象

if __name__ == "__main__":
    # try:
    #     print(a)
    # except (NameError,IOError) as e :
    #     print(e)

    # except Exception as e:
    #     print(e)


    # 抛出异常，用raise语句
    value = int(input())
    if value < 0:
        raise ValueError("value error")
        # raise ValueError("value error") from None
    else:
        print(value)
