Numberz
========
Numberz is a RESTful, Flas-based API that can translate english/human friendly
numbers to value-based expressions. Assuming the virtual environment is set up
correctly, run 'python run.py' to activate the service and then reference the
snippets below.

### Numbers (*numbers.py*) ###
Functionality:
* Extracts numbers from English text
* curl http://127.0.0.1:5000/english_to_number -X POST -d "number_expression=One"
* curl http://127.0.0.1:5000/english_to_number -X POST -d "number_expression=eight hundred sixty four thousand two hundred nine"

Examples:

    from grammar import numbers

    s = numbers.NumberService()
    assert 1 == s.parse_english("one")
    assert 12 == s.parse_english("twelve")
    assert 72 == s.parse_english("seventy two")
    assert 300 == s.parse_english("three hundred")
    assert 1200 == s.parse_english("twelve hundred")
    assert 12304 == s.parse_english("twelve thousand three hundred four")

### Math (*simple_math.py*) ###
Functionality:
* Solves expressions from English text
* curl http://127.0.0.1:5000/solve/eight%20times%20two -X GET
* curl http://127.0.0.1:5000/solve -X POST -d "arithmetic_expression=one plus one"

Examples:

    from grammar import simple_math

    s = simple_math.SimpleMathService()
    assert s.parse_basic_formula("one plus one") == 2
    assert s.parse_basic_formula("one minus one") == 0
    assert s.parse_basic_formula("six times three") == 18
    assert s.parse_basic_formula("two raised to four") == 16
