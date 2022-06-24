import sys, tty, os

terminal_size = os.get_terminal_size()
cols = terminal_size.columns
rows = terminal_size.rows

class Renderer:
    def __init__(self, body):
        self.body = body

    def main_looper(self, panel):
        layout = self.panel.layout
        dividing = [element.size for element in self.panel.elements]
        percentage = 100
        remaining = 0
        for i in dividing:
            if type(i) == int:
                percentage -= i
            else:
                remaining += 1
        percentage_remaining  = percentage//remaining
        for k,v in enumerate(dividing):
            if i == 'normal':
                dividing[k] = percentage_remaining
        
        
        for k,v in self.panel.elements:
            dividing[k] = 
