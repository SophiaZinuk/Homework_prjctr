import time

# Write a decorator that ensures a function is only called by users with a specific role. 
# Each function should have an user_type with a string type in kwargs

def is_admin(func):
    def check(user_type):
        if user_type == 'admin':
            func(user_type)
        elif user_type == 'user':
            print('ValueError: Permission denied')
        else:
            print("Wrong data.")
    return check


@is_admin
def show_customer_receipt(user_type: str):
    # some very dangerous operation
    print('You have an access!')


# Write a decorator that wraps a function in a try-except block and print an error if error has happened

def catch_errors(func):
    def finder(data):
        try:
            func(data)
        except KeyError as ke:
            print('KeyError no such key as', ke)
        except Exception:
            print(f'You have an error {Exception}')
    return finder

@catch_errors
def some_function_with_risky_operation(data):
    print(data['key'])

# Optional: Create a decorator that will check types. It should take a function with arguments and validate inputs with annotations.

def check_types(func):
    list_ = list(func.__annotations__.values())[:-1]
    def inner(*args): 
        for i in range(len(list_)):
            if list_[i] != type([*args][i]):
                print(f'Argument a must be {list_[i]}, not {type([*args][i])}')
                return
        return print(func(*args))
    return inner

@check_types
def add(a: int, b: int) -> int:
    return a + b


# Create a function that caches the result of a function, so that if it is called with same argument multiple times, 
# it returns the cached result first instead of re-executing the function.

def cach_result(func):
    cache = {}
    def inner(*args):
        if str(args) not in cache.keys():
            cache[str(args)] = func(*args)
            return cache[str(args)]
        else: 
            return cache[str(args)]
    return inner


#  Write a decorator that adds a rate-limiter to a function, so that it can only be called a certain amount of times per minute.

def rate_limiter(num_of_calls: int):
    start = time.time()
    end = start + 60
    num_of_calls_in_process = 0
    def inner (func, *args):
        if time.time() <= end:
            if num_of_calls_in_process > num_of_calls:
                print('The maximum number of function calls per minute has been reached.')
                time.sleep(end - start)
            else:
                func(*args)
                num_of_calls_in_process += 1
                
    return inner

# чому помилка?
@rate_limiter(num_of_calls=5)
def add(a: int, b: int) -> int:
    return a + b


















