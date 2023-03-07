
class Pizza():
    def __init__(self, description, cost):
        self._description = description
        self._cost = cost
    
    def get_description(self):
        return self._description
    
    def get_cost(self):
        return self._cost



class Decorator:
    def __init__(self, component):
        self.component = component

    def get_description(self):
        return self.component.get_description()

    def get_cost(self):
        return self.component.get_cost()
