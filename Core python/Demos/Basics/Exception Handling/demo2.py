def add():
    try:
        num=int(input("Enter number:"))
        return num
    except Exception as e:
        print(e)
        return
    finally:
        print("All task are done.")
res=add()
print(res)