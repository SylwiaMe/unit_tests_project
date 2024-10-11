from lib.report_length import *

def test_check_the_lenght_of_the_str():
    result = report_length('Sylwia')
    assert result == "This string was 6 characters long."
