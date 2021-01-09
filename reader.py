import os

import pywinauto
from pywinauto import Application
from pywinauto import application

import test1211



def reader():
    path = 'config\\hello.txt'
    # abs_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), path) # 절대경로(dirname(__file__))+상대경로(path)
    print(os.path.join(os.getcwd(), path))
    # print(abs_path)

    with open(path) as f:
        for line in f:
            print(line)

# app = Application(backend="win32").connect(title='[공지] 2021년 성찰노트 작성 및 제출 일자 공지 드립니다. - danny@akuo.ai - akuo.ai 메일 - Chrome', timeout=1).window()
# app.print_control_identifiers()
#
# app.child_window(title="").click()
#
# procs = pywinauto.findwindows.find_elements()
# for proc in procs:
#     print(proc)

app = Application(backend="uia").start('notepad.exe').window()
app.print_control_identifiers()
