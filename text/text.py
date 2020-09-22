# 文字辨識
import pytesseract
# 影像處理套件 Pillow
from PIL import Image
# 作業系統介面
import os
# 系統相關
import sys
# GUI，用於選擇檔案
import tkinter
from tkinter import filedialog

# 設定 pytesseract 執行檔位置
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

# 隱藏 GUI 視窗
root = tkinter.Tk()
root.withdraw()

# 選擇檔案對話框
paths = filedialog.askopenfilename(title='Select an image', filetypes=[('JPG', '*.jpg'), ('PNG', '*.png')], multiple=True)

# 沒有選檔案的話退出
if len(paths) == 0:
  sys.exit()

# 輸出結果
print('Results:')

for p in paths:
  print('===================================')
  img = Image.open(p)
  text = pytesseract.image_to_string(img, lang='chi_tra+en')
  text = text.replace('\n\n', '\n')
  print(text)

print('===================================')
print('Finished!\n')
input("Press Enter to close...")
