from tkinter import Grid
from kivy.app import App
from kivy.core import text
from kivy.uix.layout import Layout
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window

class InterfaceApp(App):
    def build(self):

        id = "123549"

        n_coments = 3

        n_results = 10

        Layout = FloatLayout()
        ###TOP BAR ####
        top_bar = GridLayout(cols=3, row_force_default=True, row_default_height=40)

        id_label = Label(text="Id: "+id)
        top_bar.add_widget(id_label)
        pass_button = Button(text = "Passar questão")
        top_bar.add_widget(pass_button)
        
        go_btn = Button(text = "Gravar")
        top_bar.add_widget(go_btn)

        Layout.add_widget(top_bar)
        ###TOP BAR ####

        ## CONTENT LAYOUT ##

        layout = GridLayout(cols=3, spacing=10, size_hint_y=None)
        # Make sure the height is such that there is something to scroll.
        layout.bind(minimum_height=layout.setter('height'))
        
        for i in range(n_coments):
            layout_coments = GridLayout(rows=2)

        btn = Label(text = "Art. 1º A República Federativa do Brasil, formada pela união indissolúvel dos Estados e Municípios e do Distrito Federal, constitui-se em Estado Democrático de Direito e tem como fundamentos:", height =50,multiline=True )
        layout.add_widget(btn)
        
        root = ScrollView(size_hint=(1, None), size=(Window.width, Window.height))
        root.add_widget(layout)


        Layout.add_widget(root)


        ##



        

        return Layout
        


if __name__ == '__main__':
    Window.maximize()
    InterfaceApp().run()