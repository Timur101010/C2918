import flet as ft
import page as page


# pip install flet
def main (page: ft. Page) :
    page.title = "Flet counter example"
    page.vertical_alignment = ft. MainAxisAlignment. CENTER
    
    txt_number = ft. TextField (value="g", text_align=ft. TextAlign.RIGHT, width=100)
def minus_click(e, txt_number=None):
    txt_number .value = strint (txt_number. value) - 1
    page.update ()
def plus_click(e, page=None):
    txt_number.value = str (int (txt_number. value) + 1)
    page.update ()
    page.add()