import customtkinter as ctk
from tkinter import *
from tkinter import messagebox

import openpyxl, xmld
import pathlib

from openpyxl import Workbook

#Aparência do Sistema

ctk.set_appearence_mode("System")
ctk.set_default_theme("blue")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()



if __name__=="__main__":
    app = App()
    app.mainloop()