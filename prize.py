#!/usr/bin/env python

# Randomly select one line of a csv file. Used to select the winner of a raffle
# @antiadriano 2014

from Tkinter import Frame, Tk, BOTH, Text, Menu, END
import tkFileDialog 
import random

class Example(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)   

        self.parent = parent        
        self.initUI()

    def initUI(self):

        self.parent.title("Ganador del sorteo!")
        self.pack(fill=BOTH, expand=1)

        menubar = Menu(self.parent)
        self.parent.config(menu=menubar)

        fileMenu = Menu(menubar)
        fileMenu.add_command(label="Abrir", command=self.onOpen)
        menubar.add_cascade(label="Archivo", menu=fileMenu)        

        self.txt = Text(self)
        self.txt.pack(fill=BOTH, expand=1)


    def onOpen(self):

        ftypes = [('Archivos CSV', '*.csv'), ('Todos los archivos', '*')]
        dlg = tkFileDialog.Open(self, filetypes = ftypes)
        fl = dlg.show()

        if fl != '':
            text = self.readFile(fl)
            self.txt.insert(END, text)

    def readFile(self, filename):

        f = open(filename, "r")
        text = f.readlines()
        winners = random.sample(text, 3)
        return "Ganador del sorteo: " + winners[0] + "\n\nFelicidades!!!\n\n"


def main():

    root = Tk()
    ex = Example(root)
    root.geometry("300x250+300+300")
    root.mainloop()  


if __name__ == '__main__':
    main()  
