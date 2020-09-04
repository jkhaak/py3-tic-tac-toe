import functools
import itertools


def transpose(xs):
    return map(list, zip(*xs))


def concat(xss):
    return list(itertools.chain.from_iterable(xss))


def chop(n, xs):
    if len(xs) == 0:
        return []
    return [xs[:n]] + chop(n, xs[n:])


def drop_at(i, xs):
    return xs[: i - 1], xs[i:]


def zip_with(fn, xs, ys):
    return [fn(a, b) for (a, b) in zip(xs, ys)]


def interleave(x, xs):
    if len(xs) <= 1:
        return xs
    return [xs[0]] + [x] + interleave(x, xs[1:])
