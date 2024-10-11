from lib.greet import * 

def test_if_given_name_return_hello_name():
    result = greet("Sylwia")
    assert result == "Hello, Sylwia!"
    