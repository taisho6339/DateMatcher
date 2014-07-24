__author__ = 'taisho6339'


def make_hash(n):
    import random

    source_str = 'abcdefghijklmnopqrstuvwxyz1234567890'
    random.choice(source_str)
    return "".join([random.choice(source_str) for x in xrange(n)])
