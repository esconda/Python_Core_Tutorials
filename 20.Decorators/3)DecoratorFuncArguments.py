#Author: Burak Dogancay

#DECORATOR ARGUMENT FUNCTION EXAMPLE
def decoratorfactory(message):
    def decorator(func):
        def wrapped_func(*args, **kwargs):
            print('The decorator wants to tell you: {}'.format(message))
            print("---------------------")
            return func(*args, **kwargs)
        return wrapped_func
    return decorator

@decoratorfactory('Pass argument to Decorator')
def test_function():
    pass
#-------------------------------

#DECORATOR ARGUMENT CLASS EXAMPLE
def decoratorfactory(*decorator_args, **decorator_kwargs):
    class Decorator(object):
        def __init__(self, func):
            self.func = func
        def __call__(self, *args, **kwargs):
            print('Inside the decorator with arguments {}'.format(decorator_args))
            print("---------------------")
            return self.func(*args, **kwargs)
    return Decorator
@decoratorfactory("Pass argument to Decorator")
def test_decorator_class():
    pass
#-------------------------------

def main():
    test_function()
    test_decorator_class()
    
if __name__ == '__main__':
    main()
