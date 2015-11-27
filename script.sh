#pip install -r ./requirements/requirements-testing.txt
python ./tests/test_searching.py > test.html
#pip install pylint selenium
python selenium_test.py > selenium_test.html
pylint ./algorithms/searching/binary_search.py
