class OnlineShop:
    def __init__(self):
        self.products = {}  # mahsulotlar lug'ati

    def add_product(self, name, price):
        self.products[name] = price
        print(f"{name} qo‘shildi, narxi: {price}")

    def buy(self, name):
        if name in self.products:
            price = self.products[name]
            print(f"{name} xarid qilindi, narxi: {price}")
            return price
        else:
            print(f"{name} mavjud emas.")
            return None

    def list_products(self):
        if self.products:
            print("Mahsulotlar:")
            for name, price in self.products.items():
                print(f"- {name}: {price}")
        else:
            print("Mahsulotlar mavjud emas.")

# Test
shop = OnlineShop()
shop.add_product("Olma", 5000)
shop.add_product("Banan", 3000)

shop.list_products()

shop.buy("Olma")
shop.buy("Anor")
