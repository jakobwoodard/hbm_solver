from PIL import Image, ImageGrab
import pytesseract
import pyautogui
import time

# 450  340
# 1460 560

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
ss = ImageGrab.grab(bbox=(450, 340, 1460, 560))
paragraph_pre = pytesseract.image_to_string(ss)

# click on paragraph first
pyautogui.click(900, 445)

paragraph_post = paragraph_pre.replace("|", "I")
paragraph_post = " ".join(paragraph_post.split())

pyautogui.write(paragraph_post, interval=0.01)

print(paragraph_post)
