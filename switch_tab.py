import webbrowser
import pyautogui
import time

chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
webbrowser.get('chrome').open_new_tab('test')
while True:
    pyautogui.hotkey('ctrl', 'tab')
    time.sleep(2.5)