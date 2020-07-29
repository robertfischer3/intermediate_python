# This is a simple decorator that takes a no argument function
def decorator_function(original_function):
    print("Happens prior to ...")

    def wrapper_function():
        print("Wrapper exeecute this prior to {}".format(original_function.__name__))
        return original_function()

    return wrapper_function


# def decorator_function(original_function):
#     def wrapper_function(*args, **kwargs):
#         print("Wrapper exeecute this prior to {}".format(original_function.__name__))
#         return original_function(*args, **kwargs)
#     return wrapper_function


class decorator_class(object):
    def __init__(self, original_function):
        self.original_function = original_function

    def __call__(self, *args, **kwargs):
        print(
            "Wrapper exeecute this method prior to {}".format(
                self.original_function.__name__
            )
        )
        return self.original_function(*args, **kwargs)


#
# @decorator_function
@decorator_class
def display():
    print("display function ran")


# display = decorator_function(display)

# @decorator_class
@decorator_class
def display_info(name, age):
    print("display_info ran with arguements ({}, {})".format(name, age))
