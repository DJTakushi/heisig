#Accepts kanji text string
#Outputs heisig string
 #heisig word in place of each kanji, separated by a space
 #if no heisig found, kana

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

try:
    # for Python2
    from Tkinter import *   ## notice capitalized T in Tkinter 
except ImportError:
    # for Python3
    from tkinter import *   ## notice lowercase 't' in tkinter here

importFileName = 'heisig.csv'
if len(sys.argv) > 1: #use user-specified filename
    importFileName = sys.argv[1]
print(importFileName)

heisig = {}
import csv

with open(importFileName, newline='', encoding='utf-8') as csvfile:
    heisigReader = csv.DictReader(csvfile)
    for row in heisigReader:
        heisig[row['Kanji']] = row['Heisig_Keyword']

if len(sys.argv) > 1: #use user-specified filename
    print(heisig.items())

## Window class documentation
class Window(Frame):
    def __init__(self, master = None):
        Frame.__init__(self,master)
        self.master = master

        self.master.title("Takushi's Heisig App") #changes title
        self.pack(fill=BOTH,expand = 1)#uses full space of root window
        menu = Menu(self.master)
        self.master.config(menu = menu)

        self.mainTextFont = ('times',40,'bold')
        self.secondaryTextFont = ('times',10,'bold')

        self.inText = StringVar()
        self.outText = StringVar()
        self.inText.set("<KANJI_HERE>")
        self.outText.set("<HEISIG_HERE>")

        self.kanjiTextBox = Entry(master, textvariable=self.inText)
        self.kanjiTextBox.pack()
        self.kanjiTextBox.config(font = self.mainTextFont)

        self.outputTextBox = Entry(master, textvariable=self.outText)
        self.outputTextBox.pack()
        self.outputTextBox.config(font = self.mainTextFont)

        master.bind('<Escape>', self.client_exit)
        master.bind('<Return>', self.printOutput)

    ##exits
    def client_exit(self, event=None):
        exit()

    ## prints outputstring
    def printOutput(self, event=None):
        thisCharacter = "?"
        outString = ""
        first = True
        for elem in self.inText.get():
            thisCharacter = heisig.get(elem)
            if thisCharacter is not None:
                if first:
                    first = False
                else:
                    outString=outString+"+"
                outString=outString+thisCharacter
        self.outText.set(outString)

Root = Tk()
app = Window(Root)
Root.mainloop()