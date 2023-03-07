import Modules

 
class Olives():
    def __init__(self, pizza):
        Modules.Decorator.__init__(self, pizza)
        self.description = "Olives"
        self.cost = 2.0

class Mushrooms():
    def __init__(self, pizza):
        Modules.Decorator.__init__(self, pizza)
        self.description = "Mushrooms"
        self.cost = 3.0

class GoatCheese():
    def __init__(self, pizza):
        Modules.Decorator.__init__(self, pizza)
        self.description = "GoatCheese"
        self.cost = 4.0

class Meat():
    def __init__(self, pizza):
        Modules.Decorator.__init__(self, pizza)
        self.description = "Meat"
        self.cost = 4.0

class Onions():
    def __init__(self, pizza):
        Modules.Decorator.__init__(self, pizza)
        self.description = "Onions"
        self.cost = 4.0
        
class Corn():
    def __init__(self, pizza):
        Modules.Decorator.__init__(self, pizza)
        self.description = "Corn"
        self.cost = 4.0


