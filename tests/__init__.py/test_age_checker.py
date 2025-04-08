from lib.age_checker import *

def test_returns_dob():
    dob = '01-01-2009'
    assert age_checker(dob) == '01-01-2009'