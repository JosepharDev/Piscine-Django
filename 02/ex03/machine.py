from beverages import HotBeverage, Coffee, Tea, Chocolate, Cappuccino
import random
class CoffeeMachine:
    def __init__(self):
        self.served_count = 0
    
    class EmptyCup(HotBeverage):
        name = "empty cup"
        price = 0.90
        
        def description(self):
            return "An empty cup?! Gimme my money back!"
    
    class BrokenMachineException(Exception):
        def __init__(self):
            super().__init__("This coffee machine has to be repaired.")
        
    def repair(self):
        self.served_count = 0
        print("\n[Repairing Machine... All systems green.]\n")

    def serve(self, drink_class):
        if self.served_count >= 10:
            raise self.BrokenMachineException()

        self.served_count +=1

        if random.randint(0,1) == 0:
            return drink_class()
        else:
            return self.EmptyCup()


if __name__ == '__main__':
    machine = CoffeeMachine()
    
    menu = [Coffee, Tea, Chocolate, Cappuccino]

    print("--- FIRST ROUND OF SERVICE ---")
    try:
        for i in range(12):
            drink_request = random.choice(menu)
            print(f"Requesting: {drink_request.name}...")
            result = machine.serve(drink_request)
            print(result)
            print("-" * 20)
    except CoffeeMachine.BrokenMachineException as e:
        print(f"\nERROR: {e}")

    machine.repair()

    print("--- SECOND ROUND OF SERVICE ---")
    try:
        for i in range(12):
            drink_request = random.choice(menu)
            print(f"Requesting: {drink_request.name}...")
            result = machine.serve(drink_request)
            print(result)
            print("-" * 20)
    except CoffeeMachine.BrokenMachineException as e:
        print(f"\nERROR: {e}")