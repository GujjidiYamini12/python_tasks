"""12. Smart Home Devices (Multiple Inheritance)
A smart home device may have both WiFi connectivity and Voice control features.
Create classes WiFiDevice and VoiceAssistant, and a class SmartSpeaker that
inherits from both using multiple inheritance.
"""
class WiFiDevice:
    def connect(self):
        print("Wifi connected")
class VoiceAssistant:
    def voice(self):
        print("voice assistant")
class SmartSpeaker(WiFiDevice, VoiceAssistant):
    def display(self):
        print("I was connected to wifi and voice assistance is given to me")
s=SmartSpeaker()
s.connect()
s.voice()
s.display()