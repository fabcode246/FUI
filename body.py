class Panel:
    def __init__(self, elements=None, layout='vertical', size='normal', border=False):
        self.elements = [] if elements == None else elements
        self.layout = layout
        self.border = border
        self.size = size

    def add_element(self, element, pos=None):
        pos = pos if pos else len(self.elements)
        self.elements.insert(pos, element)

class Text:
    def __init__(self, text):
        self.text = text
        self.links = self.get_links()

    def get_links(self):
        txt = self.text
        links = []
        while txt:
            txt = txt[txt.index('http'):]
            end = txt.index(' ')
            links.append(txt[:end])
            txt = [end:]
        return links
