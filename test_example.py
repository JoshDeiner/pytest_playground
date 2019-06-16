''' playing with pytest  '''
import pytest

TEST_CASE_1 = (3, 5, 8)
TEST_CASE_2 = (-2, -2, -4)
TEST_CASE_3 = (-1, 5, 4)
TEST_CASE_4 = (0, 5, 5)


def sum_nums(num1, num2):
    ''' practice func  '''
    return num1 + num2


@pytest.mark.parametrize('num1, num2, expected',
                         [TEST_CASE_1, TEST_CASE_2,
                          TEST_CASE_2, TEST_CASE_4])
def test_sum(num1, num2, expected):
    ''' testing  '''
    assert sum_nums(num1, num2) == expected
