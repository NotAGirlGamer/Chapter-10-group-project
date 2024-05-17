class CashRegister:
    def __init__(self):
        self.__cart = []

    def purchase_item(self, item):
        self.__cart.append(item)

    def get_total(self):
        total = sum(item.get_price() for item in self.__cart)
        return total

    def show_cart(self):
        for item in self.__cart:
            print(item)

    def empty(self):
        self.__cart = []