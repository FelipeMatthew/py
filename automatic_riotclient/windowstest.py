import pyautogui
windows = pyautogui.getAllWindows()
for window in windows:
    print(window.title)