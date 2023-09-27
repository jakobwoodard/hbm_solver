from PIL import Image, ImageGrab
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
string = pytesseract.image_to_string(Image.open("typing_test.png"))
print(string)
