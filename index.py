#!/usr/bin/env python

from gpiozero import Button
from __future__ import unicode_literals

from twilio.rest import Client
import os

def load_twilio_config():
    twilio_account_sid = 'AC91e34ed986c55316d3075d8c0e7ceadc'
    twilio_auth_token = '3cb19b7887b1bcec785feb2d6e103ddc'
    twilio_number = '+4915735984770'

    return (twilio_number, twilio_account_sid, twilio_auth_token)

class MessageClient(object):
    def __init__(self):
        (twilio_number, twilio_account_sid,
         twilio_auth_token) = load_twilio_config()

        self.twilio_number = twilio_number
        self.twilio_client = Client(twilio_account_sid,
                                              twilio_auth_token)

    def send_message(self, body, to):
        self.twilio_client.messages.create(body=body, to=to,
                                           from_=self.twilio_number,
                                           # media_url=['https://demo.twilio.com/owl.png'])
                                           )
client = MessageClient()


lucy_beer_button = Button(23)
joe_beer_button = Button(18)

def lucy_press():
    client.send_message('bier bitte', '+4915166420930')

def joe_press():
    client.send_message('bier bitte', '+4915166420930')

lucy_beer_button.when_pressed = lucy_press
joe_beer_button.when_pressed = joe_press
