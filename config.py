# run tests in 'tests' directory with 'nosetests test_numbers.py'
#
# curl http://127.0.0.1:5000/english_to_number -X POST -d "number_expression=One"
# curl http://127.0.0.1:5000/english_to_number -X POST -d "number_expression=eight hundred sixty four thousand two hundred nine"
# curl http://127.0.0.1:5000/english_to_number -X POST -d "number_expression=One" -d "number_expression=Two"
# curl http://127.0.0.1:5000/english_to_number/one -X GET
# curl http://127.0.0.1:5000/english_to_number/two%20hundred -X GET
#
# curl http://127.0.0.1:5000/solve/one%20plus%20one -X GET
# curl http://127.0.0.1:5000/solve/eight%20times%20two -X GET
# curl http://127.0.0.1:5000/solve -X POST -d "arithmetic_expression=one plus one"

# import requests
# requests.post('http://127.0.0.1:5000/english_to_number', data={'number_expression': 'One'})
# requests.get('http://127.0.0.1:5000/english_to_number/One')
#
# requests.post('http://127.0.0.1:5000/solve', data={'arithmetic_expression': 'one plus one'})
