import configparser
from pywinauto.application import Application

class Student:
    name = ''

    korean = 0

    english = 0

    math = 0

    def __init__(self, name, kor, eng, math): # 생성자

        self.name = name

        self.korean = kor

        self.english = eng

        self.math = math

    def say_hello(self):

        return '안녕하세요 {}님'.format(self.name)

    def average(self):

        return (self.korean + self.english + self.math) / 3

test1 = Student('영훈', 30, 34, 44)
print(test1.math)
print(test1.say_hello())
print(test1.average())

config = configparser.ConfigParser()
config.read('config.ini')

username = config['DEFAULT']['USERNAME']
password = config['DEFAULT']['PASSWORD']

print(username)
print(password)

# try:
#     x = int(input('3의 배수를 입력하세요: '))
#     if x % 3 != 0:  # x가 3의 배수가 아니면
#         raise Exception('3의 배수가 아닙니다.')  # 예외를 발생시킴
#     print(x)
# except Exception as e:  # 예외가 발생했을 때 실행됨
#     print('예외가 발생했습니다.', e)