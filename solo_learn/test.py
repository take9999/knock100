for i in range(10):
    try:
        if 10/i == 2.0:
            print(i)
            break
    except ZeroDivisionError:
        print(1)
    else:
        print("i="+str(i))
        print(2)