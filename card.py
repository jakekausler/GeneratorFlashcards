from formatter import underline

class Card:
    def __init__(self, id):
        self.id = id
        self.fields = []
    
    def __str__(self):
        return " ".join([underline(f) for f in self.fields])
