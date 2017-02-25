import functools

def trace_function(f):
    @functools.wraps(f)
    def new_f(*args):
        print(
            'Called  {}({!r})'
            .format(f, *args))
        result = f(*args)
        print("Returning", result)
        return result
    return new_f

@trace_function        
def add(first, second):
    return first + second


print(add(5,6))


def memoize(f):
    print("Called Memoize({!r})".format(f))
    cache = {}
    @functools.wraps(f)

    def memoize_f(*args):
        print("Called memoize with ")
        if (args in cache):
            print("Cache Hit!!")
            return cache[args]

        if (args not in cache):
            result = f(*args)
            cache[args] = result
            return result
        
    return memoize_f

@memoize
def add1(first, second):
    return first + second


add1(2,3)
add1(3,5)
add1(2,3)