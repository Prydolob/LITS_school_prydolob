def dec_b(function):
    def inner(*args, **kwargs):
        return f'<b>{function(*args, **kwargs)}</b>'

    return inner


def dec_i(function):
    def inner(*args, **kwargs):
        return f'<i>{function(*args, **kwargs)}</i>'

    return inner


def dec_u(function):
    def inner(*args, **kwargs):
        return f'<u>{function(*args, **kwargs)}</u>'

    return inner


def not_error(f):
    _dict = dict()

    def inner(*args):
        if args not in _dict:
            _dict[args] = f(*args)
        return _dict[args]

    return inner

