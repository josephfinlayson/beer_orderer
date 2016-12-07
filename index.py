#!/usr/bin/env python

from gpiozero import Button

lucy_beer_button = Button(10)
joe_beer_button = Button(10)

def lucy_press():
 # call twilio

def joe_press():
#     call twilio

lucy_beer_button.when_pressed = lucy_press
joe_beer_button.when_pressed = joe_press

