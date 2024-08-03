import subprocess
import os
from pyfiglet import Figlet

class AsciiArt:
    def __init__(self, text, font="standard"):
        self.text = text
        self.font = font

    def display(self):
        f = Figlet(font=self.font)
        print(f.renderText(self.text))
def test(self):
    art = AsciiArt("Test TEST test", font="isometric2")
    art.display()

