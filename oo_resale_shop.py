from computer import *  
from typing import Optional

class ResaleShop:

    # What attributes will it need?
    inventory = []
    item_id = 0
    
    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)

    def __init__(self):
        # initialize an empty list of inventory
        self.inventory = []


    # What methods will you need?

    def buy(self, description:str, processor_type:str, hard_drive_capacity:int, memory:int, operating_system:str, year_made:int, price:int):
        comp = Computer(description,
                processor_type,
                hard_drive_capacity,
                memory,
                operating_system,
                year_made,
                price)
        # call constructor to create a new computer instance
        self.inventory.append(comp)
        self.item_id += 1 # assign an ID to the computer
        # add new computer instance to the inventory
        return self.inventory.index(comp)
    
    def update_price(self, item_id: int, new_price: int):
        if item_id in self.inventory:
            self.inventory[item_id].price = new_price
            print("Updated ", item_id, " to $", new_price)
        else:
            print("Item", item_id, "not found. Cannot update price.")

    def sell(self, item_id: int) :
        if item_id in self.inventory:
            self.inventory.pop(item_id)
            print("Item", item_id, "sold!")
        else: 
            print("Item", item_id, "not found. Please select another item to sell.")

    def print_inventory(self):
        # If the inventory is not empty
        if self.inventory:
            # For each item
            for item in self.inventory:
                # Print its details
                print(f'Item ID: {self.inventory.index(item)} : {item.print_comp()}')
        else:
            print("No inventory to display.")

    def refurbish(self, item_id: int, new_OS: Optional[str] = None):
        if self.inventory[item_id] is not None:
            computer = self.inventory[item_id] # locate the computer
            if int(computer.year_made) < 2000:
                computer.price = 0 # too old to sell, donation only
            elif int(computer.year_made) < 2012:
                computer.price = 250 # heavily-discounted price on machines 10+ years old
            elif int(computer.year_made) < 2018:
                computer.price = 550 # discounted price on machines 4-to-10 year old machines
            else:
                computer.price = 1000 # recent stuff

            if new_OS is not None:
                computer.operating_system = new_OS # update details after installing new OS
        else:
            print("Item", item_id, "not found. Please select another item to refurbish.")
        

def main():
    shop = ResaleShop()
    
    # buy some computers
    bought1 = shop.buy("2012 MacBook Air", "Intel i5", 128, 4, "macOS Lion", 2012, 600)
    bought2 = shop.buy("2022 MacBook Pro", "M2", 256, 6, "Sequoia 15.0", 2022, 1000)
    
    # current inventory after purchase
    print("\n Inventory after purchase:")
    shop.print_inventory()

    # update price
    shop.update_price(bought2, 1100)

    # refurbish old computer's OS
    shop.refurbish(bought1, new_OS = "Catalina")

    # current inventory
    print("\nCurrent Inventory after price updating and refurbishing:")
    shop.print_inventory()

    # sell the 2022 mac
    shop.sell(bought2)

    # current inventory
    print("\nInventory after selling a computer:")
    shop.print_inventory()


if __name__ == "__main__":
    main()