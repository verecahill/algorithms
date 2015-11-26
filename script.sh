#pip install -r ./requirements/requirements-testing.txt
python ./tests/test_searching.py -v
pip install pylint selenium
python selenium_test.py
pylint ./algorithms/searching/binary_search.py
