# import pytest
# # import requests
# import xlrd
#
#
# #
# #
# #
# def getOneCase():
#    with xlrd.open_workbook("test.xls") as file:
#       sheet = file.sheet_by_index(0)
#       onevalue = sheet.row_values(0)
#       # print(onevalue)
#       dict = []
#       for row in range(1, sheet.nrows):
#          list = {}
#          othervalues = sheet.row_values(row)
#          for i in range(0, len(onevalue)):
#             if isinstance(othervalues[i], float):  # 判断是否含有float
#                list[onevalue[i]] = int(othervalues[i])
#             else:
#                list[onevalue[i]] = othervalues[i]
#          dict.append(list)
#       return dict
#
#
# #
# # # print(getOneCase())
# # # @pytest.fixture(scope='module')
# # # def cc():
# # #      with requests.post(url="http://192.168.219.131:81/api/login/", data={
# # #         'account': 'admin',
# # #         'password': 'admin1'
# # #     }) as cc:
# # #          print(cc)
# # #          print(cc)
# # #
# @pytest.mark.parametrize("cc", getOneCase())
# def test_a(cc):
#    print(cc)
#
#
# # #
# # # def test_c(cc):
# # # @pytest.mark.skip('bu')
# # @pytest.mark.apptest
# # def test_a():
# #    print('测试123456789')
# # @pytest.mark.appdup
# # def test_b():
# #    print('测试asdfghjkl')
# if __name__ == '__main__':
#    pytest.main(['-v'])
# import yaml
#
# with open('test.yaml', encoding='UTF-8') as file:
#     rad = file.read()
#     c = yaml.load(rad, Loader=yaml.FullLoader)
#     # print(len(c))
#     print(c)
#     # print(c['test'])
#     # print(len(c['test']))

# def t():
#    for i in range(1,100):
#       c = yield i
#       print(c)
# print(next(t()))

#
# def foo():
#    print("starting...")
#    while True:
#       res = yield 4
#       print("res:", res)
# 
# 
# g = foo()
# print(next(g))
# print("*" * 20)
# print(g.send(7))
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