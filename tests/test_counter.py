from lib.counter import *

def test_the_counter():
    counter = Counter()
    counter.add(5)
    x = counter.report()
    assert x == f"Counted to 5 so far."

def test_the_atributes():
    counter = Counter()
    counter.add(3)
    counter.add(1)
    assert counter.count == 4