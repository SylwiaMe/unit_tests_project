from lib.string_builder import *

def test_of_the_string_builder():
    string_builder = StringBuilder()
    string_builder.add('test')
    assert string_builder.size() == 4
    assert string_builder.str == 'test' 
    assert string_builder.output() == 'test'
