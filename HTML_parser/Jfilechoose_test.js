from Tkinter import *
import tkFileDialog

Tk().withdraw()
options = {}
# options['filetype'] = [("allfiles" , "*") , ("text" , "*.txt")]
options['multiple'] = False

options['title'] = "input file"
inputDir = tkFileDialog.askopenfilename(**options)
print isinstance(inputDir, str)