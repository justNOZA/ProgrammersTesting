import sys
sys.path.append("C:\\Users\\jaron\\Desktop\\ComputerStudy\\ProgrammersTEST_Python\Python_Study_files\\Python_Basic_18_package")
import product #파일명으로 부름 같은 위치에 존재할 때

x = product.Product('A22', '키보드', 20000)
print(x)
product.test()


import wx

app = wx.App()
frame = wx.Frame(None,0, "파이썬 만세")

frame.Show(True)
app.MainLoop()
