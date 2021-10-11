from math_series import __version__


def test_version():
    assert __version__ == '0.1.0'
from math_series import __version__
from math_series.series import fibonacci
from math_series.series import lucas
from math_series.series import sum_series
def test_version():
    assert __version__ == '0.1.0'

def test_fibonacci():
    #arrang
    number=7
    expected=13

    tset=fibonacci(number)
    assert expected == tset

def test_lucas():
    number=7
    expected=29
    tset=lucas(number)
    assert expected == tset

def test_sum_series():
    number=7
    n1=8
    n2=7
    expected=155
    tset=sum_series(number,n1,n2)
    assert expected == tset


def test_sum_series2():
    number=7
    expected=13
    tset=sum_series(number)
    assert expected == tset
