from contextlib import contextmanager


@contextmanager
def expected_exception(exception_class, *args):
    try:
        yield
    except exception_class as e:
        for arg in args:
            msg = ("arg '{}' is not in exception\n"
                   'Actual args: {}'.format(arg, e.args))
            assert arg in e.args, msg
    except Exception as e:
        msg = ('expected {} exception but got {}'
               .format(exception_class, e.__class__.__name__))
        raise AssertionError(msg)
    else:
        raise AssertionError('expected {} but there was no exception'.format(exception_class))
