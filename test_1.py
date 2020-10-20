# coding=UTF-8
import pytest

@pytest.fixture(scope="function")
def case():
   print('开始')
   yield
   print('结束')
def test_one(case):
   print('case-1')
def test_two(case):
   print('case-2')
def test_three():
   print('case-3')
if __name__ == '__main__':
    pytest.main()
