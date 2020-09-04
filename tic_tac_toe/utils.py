import itertools as it


def transpose(xs):
    """
    Transpose a matrix
    """
    return map(list, zip(*xs))


def concat(xss):
    """
    Concatenate list of lists.
    """
    return list(it.chain.from_iterable(xss))


def chop(n, xs):
    """
    Create a list of lists sized with n from list elements in xs.
    """
    if len(xs) == 0:
        return []
    return [xs[:n]] + chop(n, xs[n:])


def drop_at(nth, xs):
    """
    Drop nth element in a list. Returns the init and tail of the xs without the nth element.
    """
    if nth <= 0:
        return [], xs
    elif len(xs) < nth:
        return xs, []
    return xs[: nth - 1], xs[nth:]


def zip_with(fn, xs, ys):
    """
    Standard python zip with function. User can define custom zipping function instead of the standard tuple.
    """
    return [fn(a, b) for (a, b) in zip(xs, ys)]


def interleave(item, xs):
    """
    Insert an item in between every item of xs.
    """
    if len(xs) <= 1:
        return xs
    return [xs[0]] + [item] + interleave(item, xs[1:])
