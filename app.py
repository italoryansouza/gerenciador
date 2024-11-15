import customtkinter as ctk # type: ignore
from tkinter import *
from tkinter import messagebox

import openpyxl, xlrd
import pathlib

from openpyxl import Workbook

#Aparência do Sistema

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.layout_config()
        self.appearance()
        self.main_system()

    def layout_config(self):
        self.title("Adicionar Cliente")
        self.geometry("700x500")

    def appearance(self):
        self.lb_apm = ctk.CTkLabel(self, text="Tema:", bg_color="transparent", text_color=['#000', '#fff']).place(x=50, y=430)

        self.opt_apm = ctk.CTkOptionMenu(self, values=["Light", "Dark", "System"], command=self.change_apm).place(x=50, y=460)

    def change_apm(self, new_appearence_mode):
        ctk.set_appearance_mode(new_appearence_mode)



    def main_system(self):
        frame = ctk.CTkFrame(self, width=700, height=50, corner_radius=0, bg_color="teal", fg_color="teal").place(x=0, y=10)

        title = ctk.CTkLabel(frame, text="Sistema de Adicionar Clientes", font=("Century Gothic Bold", 24), text_color="#fff", bg_color="transparent").place(x=100, y= 20)

        span = ctk.CTkLabel(self, text="Por favor, preencer todos os campos do formulário!", font=("Century Gothic Bold", 16), text_color=["#000", "#fff"]).place(x=50 , y=70)


if __name__=="__main__":
    app = App()
    app.mainloop()