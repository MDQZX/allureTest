import pytest
import allure


@allure.step("1+1=2")
@allure.story("测试1")
def test_1(login_test):
    print('case 1')


@allure.story("测试2")
def test_2(login_test):
    a = 1
    print('case 2')
    assert a == 2


def test_3(login_test):
    print('case 3')


def test_4(login_test):
    print('case 4')
