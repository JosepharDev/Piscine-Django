class HotBeverage():
    price=0.30
    name="hot beverage"
    
    def description(self):
        return "Just some hot water in a cup."

    def __str__(self):
        return "name: " + self.name + "\nprice : " + "{:.2f}".format(self.price) + "\ndescription : " + self.description()

class Coffee(HotBeverage):
    name = "coffee"
    price = 0.40

    def description(self):
        return "A coffee, to stay awake."

class Tea(HotBeverage):
    name = 'tea'

class Chocolate(HotBeverage):
    name = "chocolate"
    price = 0.50

    def description(self):
        return "chocolate, sweet chocolate..."

class Cappuccino(HotBeverage):
    name = "cappuccino"
    price = 0.45

    def description(self):
        return "Un po’ di Italia nella sua tazza!"

if __name__ == "__main__":
    hot_beverage = HotBeverage()
    coffee = Coffee()
    tea = Tea()
    chocolate = Chocolate()
    cappuccino = Cappuccino()

    print(hot_beverage)
    print(coffee)
    print(tea)
    print(chocolate)
    print(cappuccino)
