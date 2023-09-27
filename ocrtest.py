from PIL import Image, ImageGrab
import pytesseract
import pyautogui

# 600 1250
# 330 440

# Seen: 880, 475
# New: 1020, 475

count = 50
words = []

for i in range(count):
    pytesseract.pytesseract.tesseract_cmd = (
        r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    )
    ss = ImageGrab.grab(bbox=(600, 330, 1250, 420))
    new_word = pytesseract.image_to_string(ss)
    if new_word not in words:
        words.append(new_word)
        pyautogui.moveTo(1020, 475, duration=1)
    else:
        pyautogui.click(880, 475)
