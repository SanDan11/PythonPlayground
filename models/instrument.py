class Instrument:
    def __init__(self,id, name, brand, category, condition, price):
        self.id = id
        self.name = name
        self.brand = brand
        self.category = category
        self.condition = condition
        self.price = price

    def __str__(self):
        return f"{self.name} by {self.brand} ({self.category}, {self.condition}) - ${self.price:.2f}"
    
