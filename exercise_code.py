def logging_decorator(function):
    def wrapper(*args, **kwargs):
        sum_math = 0
        print(f"You called: {function.__name__}{args}")
        for n in args:
            sum_math += n

        print(f"It returned: {sum_math}")
    return wrapper 

@logging_decorator
def function(*args):
    list = []
    for n in args:
        list.append(n)
    return list

function(5, 6, 4, 6, 8, 9)