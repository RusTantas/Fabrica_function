def create_operation(operation):
    if operation == "multiplication":
        def multiplication(x, y):
            return x * y
        return multiplication
    elif operation == "division":
        def division(x, y):
            try:
                return x / y
            except ZeroDivisionError:
                return ('Cannot devide by 0')
        return division
my_func_add = create_operation("division")
print(my_func_add(1,0))