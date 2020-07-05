from package import bisection_method

def test_bisection():
    assert bisection_method.bisection_method(2, 4) == "Root does not exist"
