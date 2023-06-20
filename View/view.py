from tkinter import *
from tkinter import ttk
import tkinter as tk


class visualInterface:
    __ventana= None
    __title = None
    __overview = None
    __originalLang = None
    __releaseDate = None
    __genre = None


    def __init__(self, ctrl):
        self.__ctrl = ctrl
        self.__ventana = Tk()
        self.__ventana.title("Movie List")
        self.__ventana.geometry("650x250")
        #listbox
        self.listbox = tk.Listbox(self.__ventana, width=35, height=15)
        scroll = tk.Scrollbar(self.__ventana, command=self.listbox.yview)
        self.listbox.config(yscrollcommand=scroll.set)
        scroll.grid(row=1, column=3,rowspan=2, sticky=(N,S))
        self.listbox.grid(row=1, column=1, columnspan=2)
        self.__title = StringVar()
        self.__overview = StringVar()
        self.__originalLang = StringVar()
        self.__releaseDate = StringVar()
        self.__genre = StringVar()
        self.listBoxMovie()
        self.detailsFrame()
        
        #EVENT DOUBLE CLICK
        self.listbox.bind("<Double-Button-1>", self.selection_DoubleClick)

    def listBoxMovie(self):
        for i in range(self.__ctrl.getListLen()):
            self.listbox.insert(tk.END, self.__ctrl.getTitle(i))

    def detailsFrame(self):
        self.detailsframe = tk.Frame(self.__ventana, borderwidth=2, relief="sunken", width=50, height=50)
        self.detailsframe.grid(row=1, column=4, rowspan=5, sticky=(N,S))
        ttk.Label(self.detailsframe, text= "Title: ").grid(row=1, column=1, sticky=W)
        ttk.Label(self.detailsframe, text="Overview: ").grid(row=2, column=1, sticky=W)
        ttk.Label(self.detailsframe, text="Original Lenguage: ").grid(row=3, column=1, sticky=W)
        ttk.Label(self.detailsframe, text="Release Date: ").grid(row=4, column=1, sticky=W)
        ttk.Label(self.detailsframe, text="Genre: ").grid(row=5, column=1, sticky=W)

        ttk.Label(self.detailsframe, textvariable=self.__title).grid(row=1, column=2, sticky=W)
        ttk.Label(self.detailsframe, textvariable=self.__overview, wraplength=300).grid(row=2, column=2, sticky=W)
        ttk.Label(self.detailsframe, textvariable=self.__originalLang).grid(row=3, column=2, sticky=W)
        ttk.Label(self.detailsframe, textvariable=self.__releaseDate).grid(row=4, column=2, sticky=W)
        ttk.Label(self.detailsframe, textvariable=self.__genre).grid(row=5, column=2, sticky=W)

    def selection_DoubleClick(self, event):
        movieSelected = self.listbox.curselection()
        if movieSelected:
            index = int(movieSelected[0])
            movieSelected = self.listbox.get(index)
            self.showMovie(movieSelected, index)

    def showMovie(self, movieSelected, index):
        self.__title.set(movieSelected)
        self.__originalLang.set(self.__ctrl.getLenguage(index))
        self.__overview.set(self.__ctrl.getOverV(index))
        self.__releaseDate.set(self.__ctrl.getRDate(index))
        self.__genre.set(self.__ctrl.getGen(index))
        
    def run(self):
        self.__ventana.mainloop()