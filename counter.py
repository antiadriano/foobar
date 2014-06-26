#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Using cocos & piglet libraries, is a small counter program 
where when you push the up key it will add a number to the displayed value, and the down key will substract one """

# @antiadriano 2014

import cocos
import sys
from cocos.actions import *
import pyglet
from pyglet.window import key

class tempBackground(cocos.layer.Layer):

    is_event_handler = True

    def on_key_press(self, symbol, modifiers):
        if symbol == key.UP:
            self.counter = self.counter + 1
        elif symbol == key.DOWN:
            self.counter = self.counter - 1
        elif symbol == key.ESCAPE:
            SystemExit()
            
        self.updateText()
        
    def updateText(self):
        self.label.element.text = str(self.counter)
    
    def __init__(self):
        self.startBackground = super(tempBackground, self).__init__()
        self.counter = 0
        self.label = cocos.text.Label(str(self.counter),
                                 font_name='Arial',
                                 font_size=150,
                                 anchor_x='center',
                                 anchor_y='center')
        self.label.position = 320,240
        self.updateText()
        self.add(self.label)

if __name__ == "__main__":
    cocos.director.director.init(resizable=False, fullscreen=False)
    tempLayer = tempBackground()
    mainScene = cocos.scene.Scene(tempLayer)
    cocos.director.director.run(mainScene)
