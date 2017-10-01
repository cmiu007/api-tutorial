class Store:
    def __init__(self, name):
        self.name = name
        self.items = []
        # You'll need 'name' as an argument to this method.
        # Then, initialise 'self.name' to be the argument, and 'self.items' to be an empty list.
    
    def add_item(self, name, price):
        #self.items.append({"name": name, "price": price})
        item = {'name': name, 'price': price}
        self.items.append(item)
        # Create a dictionary with keys name and price, and append that to self.items.

    def stock_price(self):
        # total = 0
        # for item in self.items:
        #     total += item['price']
        # return total
        return sum( item['price'] for item in self.items)
        # Add together all item prices in self.items and return the total.

