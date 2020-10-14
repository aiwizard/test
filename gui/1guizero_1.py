'''
https://lawsie.github.io/guizero/
https://lawsie.github.io/guizero/about/

'''

from guizero import App, Text, PushButton, TextBox

window = App(title="guizero")

intro = Text(window, text="Have a go with guizero and see what you can create.")
dir_box = TextBox(window, grid=[2,3], width=30)
ok = PushButton(window, text="Ok")

window.display()
