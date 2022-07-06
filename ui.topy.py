
from PyQt5 import uic

with open('Window.py', 'w', encoding="utf-8") as fout:
   uic.compileUi('Window.ui', fout)