from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.app import runTouchApp

layout = GridLayout(cols=1, spacing=10, size_hint_y=None)
# Make sure the height is such that there is something to scroll.
layout.bind(minimum_height=layout.setter('height'))

btn1 = Button(text=str("I am The Best"), size_hint_y=None, height=100)
btn2 = Button(text=str("Science"), size_hint_y=None, height=100)
btn3 = Button(text=str("Sport"), size_hint_y=None, height=100)
btn4 = Button(text=str("99.9"), size_hint_y=None, height=100)
btn5 = Button(text=str("University"), size_hint_y=None, height=100)
btn6 = Button(text=str("Apps"), size_hint_y=None, height=100)
btn7 = Button(text=str("99999.7777 Billion"), size_hint_y=None, height=100)
btn8 = Button(text=str("Big Big Metaverse"), size_hint_y=None, height=100)
btn9 = Button(text=str("I am the Biggest"), size_hint_y=None, height=100)
btn10 = Button(text=str("Now"), size_hint_y=None, height=100)


layout.add_widget(btn1)
layout.add_widget(btn2)
layout.add_widget(btn3)
layout.add_widget(btn4)
layout.add_widget(btn5)
layout.add_widget(btn6)
layout.add_widget(btn7)
layout.add_widget(btn8)
layout.add_widget(btn9)
layout.add_widget(btn10)



root = ScrollView(size_hint=(1, None), size=(Window.width, Window.height))
root.add_widget(layout)

runTouchApp(root)
