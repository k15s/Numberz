from grammar import simple_math


def test_basic_addition():
    sp = simple_math.SimpleMathService()
    assert sp.parse_basic_formula("one plus one") == 2
    assert sp.parse_basic_formula("one plus 1") == 2
    assert sp.parse_basic_formula("eight plus five") == 13
    assert sp.parse_basic_formula("negative four plus negative two") == -6
    assert sp.parse_basic_formula("thirty three plus twenty four") == 57


def test_larger_addition():
    sp = simple_math.SimpleMathService()
    assert sp.parse_basic_formula("eight plus fifty plus thirty two") == 90
    assert sp.parse_basic_formula("one hundred eighty four plus eight hundred forty three") == 1027
    assert sp.parse_basic_formula("negative three hundred fifty six plus two hundred four") == -152
    assert sp.parse_basic_formula("six thousand four hundred thirty plus nine") == 6439
    assert sp.parse_basic_formula("nine hundred fifty four plus six") == 960
    assert sp.parse_basic_formula("one million plus two million") == 3000000


def test_basic_subtraction():
    sp = simple_math.SimpleMathService()
    assert sp.parse_basic_formula("one minus one") == 0
    assert sp.parse_basic_formula("eight minus three") == 5
    assert sp.parse_basic_formula("sixteen minus twelve") == 4
    assert sp.parse_basic_formula("twenty two minus eight") == 14
    assert sp.parse_basic_formula("twenty two minus eighty nine") == -67
    assert sp.parse_basic_formula("negative four minus negative eight") == 4


def test_basic_multiplication():
    sp = simple_math.SimpleMathService()
    assert sp.parse_basic_formula("six times three") == 18
    assert sp.parse_basic_formula("negative four times three") == -12
    assert sp.parse_basic_formula("zero times four hundred three") == 0
    assert sp.parse_basic_formula("four times four") == 16
    assert sp.parse_basic_formula("eight times two") == 16
    assert sp.parse_basic_formula("negative eight times two") == -16


def test_basic_division():
    sp = simple_math.SimpleMathService()
    assert sp.parse_basic_formula("six divided by three") == 2
    assert sp.parse_basic_formula("nine divided by four") == 2.25
    assert sp.parse_basic_formula("one divided by one") == 1
    assert sp.parse_basic_formula("fifty divided by twenty five") == 2
    assert sp.parse_basic_formula("thirty two divided by four") == 8


def test_basic_powers():
    sp = simple_math.SimpleMathService()
    assert sp.parse_basic_formula("two raised to four") == 16
    assert sp.parse_basic_formula("two raised to three") == 8
    assert sp.parse_basic_formula("five raised to three") == 125
    assert sp.parse_basic_formula("two raised to zero") == 1
    assert sp.parse_basic_formula("three raised to four") == 81

    assert sp.parse_basic_formula("two to four") == 16
    assert sp.parse_basic_formula("two to three") == 8
    assert sp.parse_basic_formula("five to three") == 125
    assert sp.parse_basic_formula("two to zero") == 1
    assert sp.parse_basic_formula("three to four") == 81


def test_larger_powers():
    sp = simple_math.SimpleMathService()
    assert sp.parse_basic_formula("four raised to eight") == 65536
    assert sp.parse_basic_formula("seven raised to nine") == 40353607
    assert sp.parse_basic_formula("nine raised to five") == 59049

    assert sp.parse_basic_formula("four to eight") == 65536
    assert sp.parse_basic_formula("seven to nine") == 40353607
    assert sp.parse_basic_formula("nine to five") == 59049


def test_basic_xor():
    sp = simple_math.SimpleMathService()
    assert sp.parse_basic_formula("two xor six") == 4
    assert sp.parse_basic_formula("two XOR six") == 4


def test_basic_exception_handling():
    sp = simple_math.SimpleMathService()

    try:
        sp.parse_basic_formula("one")
    except Exception:
        pass
    else:
        raise Exception("Exception not thrown")
