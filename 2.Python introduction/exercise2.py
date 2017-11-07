class Store:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_item(self, name, price):
        self.items.append({
            'name': name,
            'price': price
        })

    def stock_price(self):
        total = 0
        for item in self.items:
            total += item['price']
        return total

    @classmethod
    def franchise(cls, store):
        newStore = cls(store.name + ' - franchise')
        #newStore = Store(store.name + ' - franchise')
        return newStore
        # Return another store, with the same name as the argument's name, plus " - franchise"

    @staticmethod
    def store_details(store):
        # text = store.name + ', total stock price: '
        # total = str(store.stock_price())
        # #total = sum(item['price'] for item in store.items)
        # return(text + str(total))

        # or 
        return '{}, total stock price: {}'.format(store.name, store.stock_price())

        # Return a string representing the argument
        # It should be in the format 'NAME, total stock price: TOTAL'
    
    
store = Store("Test")
store2 = Store("Amazon")

print(Store.franchise(store).name)
print(Store.franchise(store2).name)

store2.add_item("Keyboard", 160)

Store.store_details(store)  # returns "Test, total stock price: 0"
Store.store_details(store2)  # returns "Amazon, total stock price: 160"