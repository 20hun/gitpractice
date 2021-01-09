import pywinauto
import pyautogui
import pyperclip
from pywinauto import application, Application

# app = Application(backend="uia").start("notepad.exe") 새로 실행
app = Application(backend="uia").connect(path="notepad.exe") # 이미 실행되어 있는
app['Dialog']['Edit'].set_text("Sample") # 인자 값 메모장에 작성

pywinauto.keyboard.send_keys('{ENTER}') # 키보드 버튼 클릭

app['Dialog'].menu_select("파일(F)->열기(O)") # 입력한 유사한 메뉴를 찾아서 순서대로 실행
app['Dialog'].저장안함.click() # 나타난 팝업 창 '저장안함'과 유사한 단어 찾아서 클릭

clipboardContent = pyperclip.paste() # 현재 클립보드에 있는 것 저장
print(clipboardContent)

pyperclip.copy('과연?') # 클립보드에 인자 값 저장

print(pyautogui.position()) # 화면의 내 마우스 좌표(x, y) 출력
pyautogui.moveTo(670, 300, 1) # 지정한 좌표로 마우스 옮김


