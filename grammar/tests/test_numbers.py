from grammar import numbers


def test_float_parse():
    s = numbers.NumberService()
    assert s.parse_english("1") == 1
    assert s.parse_english("124") == 124


def test_simplest_parse():
    s = numbers.NumberService()
    assert s.parse_english("zero") == 0
    assert s.parse_english("one") == 1
    assert s.parse_english("One") == 1
    assert s.parse_english("twelve") == 12
    assert s.parse_english("NINEteen") == 19
    assert s.parse_english("negative four") == -4
    assert s.parse_english("negative nine") == -9


def test_simpler_parse():
    s = numbers.NumberService()
    assert s.parse_english("twenty") == 20
    assert s.parse_english("twenty four") == 24
    assert s.parse_english("ninety three") == 93
    assert s.parse_english("sixty eight") == 68


def test_large_parse():
    s = numbers.NumberService()
    assert s.parse_english("one hundred") == 100
    assert s.parse_english("three hundred four") == 304
    assert s.parse_english("nine hundred fifty six") == 956
    assert s.parse_english("four thousand eighty seven") == 4087
    assert s.parse_english("seven thousand twenty") == 7020
    assert s.parse_english("one hundred thousand") == 100000
    assert s.parse_english("one hundred eighty thousand fifty four") == 180054
    assert s.parse_english("four hundred thirty thousand nine hundred fifty four") == 430954
    assert s.parse_english("eight hundred fifty six thousand nine hundred twenty two") == 856922
    assert s.parse_english("one hundred fifty six thousand two hundred twelve") == 156212
    assert s.parse_english("two hundred forty four thousand eight") == 244008
    assert s.parse_english("one million") == 1000000
    assert s.parse_english("negative one million") == -1000000


def test_text_2_num():
    s = numbers.NumberService()
    assert 1 == s.parse_english("one")
    assert 12 == s.parse_english("twelve")
    assert 72 == s.parse_english("seventy two")
    assert 300 == s.parse_english("three hundred")
    assert 1200 == s.parse_english("twelve hundred")
    assert 12304 == s.parse_english("twelve thousand three hundred four")
    assert 6000000 == s.parse_english("six million")
    assert 6400005 == s.parse_english("six million four hundred thousand five")
    assert 123456789012 == s.parse_english("one hundred twenty three billion four hundred fifty six million seven hundred eighty nine thousand twelve")

    assert -1 == s.parse_english("negative one")
    assert -12 == s.parse_english("negative twelve")
    assert -72 == s.parse_english("negative seventy two")
    assert -300 == s.parse_english("negative three hundred")
    assert -1200 == s.parse_english("negative twelve hundred")
    assert -12304 == s.parse_english("negative twelve thousand three hundred four")
    assert -6000000 == s.parse_english("negative six million")
    assert -6400005 == s.parse_english("negative six million four hundred thousand five")
    assert -123456789012 == s.parse_english("negative one hundred twenty three billion four hundred fifty six million seven hundred eighty nine thousand twelve")
