"""
Copyright (C) 2015, MuChu Hsu
Contributed by Muchu Hsu (muchu1983@gmail.com)
This file is part of BSD license

<https://opensource.org/licenses/BSD-3-Clause>
"""
"""
程式進入點 (main)
"""
import kivy
kivy.require('1.9.0')

from kivy.app import App
from kivy.uix.label import Label

class MyApp(App):

    def build(self):
        return Label(text='hello mops')


if __name__ == '__main__':
    MyApp().run()