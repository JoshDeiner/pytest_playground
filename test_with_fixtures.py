''' play with fixtures  '''

import pytest
import test_example as te


@pytest.fixture(scope='session')
def get_sum_test_data():
    ''' fetches sum data  '''
    return [te.TEST_CASE_1, te.TEST_CASE_2, te.TEST_CASE_3, te.TEST_CASE_4]


@pytest.fixture(autouse=True)
def setup_and_teardpwn():
    ''' simulates interaction with db '''
    print('\nFetching data from db')
    yield
    print('\nsaving test run data in dbi')


@pytest.mark.slow
def test_slow():
    ''' dummy func  '''
    assert te.sum_nums(1, 2) == 3


def test_int_answers():
    ''' check if int  '''
    assert isinstance(te.sum_nums(1, 2), int)


def test_sum(get_sum_test_data):
    ''' test sums of test cases  '''
    for data in get_sum_test_data:
        num1, num2, expected = data
        assert te.sum_nums(num1, num2) == expected
