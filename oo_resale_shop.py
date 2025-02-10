# import necessary materials
from computer import *  
from typing import Optional

# create a resale shop that buys and sells computers

class ResaleShop:

    # attributes of the Resale Shop
    inventory = []
    item_id = 1
    
    # constructor of the Resale Shop

    def __init__(self):
        
        self.inventory = []     # initialize an empty list of inventory
        self.item_id = 1        # computer ID start from 1

    # methods of the Resale Shop

    # buy a computer
    def buy(self, description:str, processor_type:str, hard_drive_capacity:int, memory:int, operating_system:str, year_made:int, price:int):
        # create a computer
        comp = Computer(description,
                processor_type,
                hard_drive_capacity,
                memory,
                operating_system,
                year_made,
                price)
        # call constructor to create a new computer instance
        self.inventory.append(comp)
        self.item_id += 1  # assign an ID to the computer
        # add new computer ID to the inventory
        return self.inventory.index(comp)
    
    # update price of the computer
    def update_price(self, item_id: int, new_price: int):
        # check whether id exist in inventory
        if len(self.inventory) > item_id and self.inventory[item_id] is not None:
            # change to new price
            self.inventory[item_id].price = new_price
            print("\nUpdated ", item_id, " to $", new_price)
        # print error message
        else:
            print("\nItem", item_id, "not found. Cannot update price.")

    # sell the computer
    def sell(self, item_id: int) :
        # check whether id exist in inventory
        if len(self.inventory) > item_id and self.inventory[item_id] is not None:
            # remove item
            self.inventory.pop(item_id)
            print("\nItem", item_id, "sold!")
        # print error message
        else: 
            print("\nItem", item_id, "not found. Please select another item to sell.")

    # print the inventory
    def print_inventory(self):
        # check whether the inventory is empty
        if self.inventory:
            # print details of every item in the inventory
            for item in self.inventory:
                print(f'Item ID: {self.inventory.index(item)} : {item.print_comp()}')
        else:
            print("No inventory to display.")

    # refurbish the computer
    def refurbish(self, item_id: int, new_OS: Optional[str] = None):
        # check whether id exist in inventory
        if len(self.inventory) > item_id and self.inventory[item_id] is not None:
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
        # error message
        else:
            print("\nItem", item_id, "not found. Please select another item to refurbish.")
        

def main():

    # store the shop
    shop = ResaleShop()

    # print a little banner
    print("-" * 21)
    print("COMPUTER RESALE STORE")
    print("-" * 21)

    # current inventory after purchase
    print("\n Inventory before purchase:")
    shop.print_inventory()

    # buy some computers
    bought1 = shop.buy("2012 MacBook Air", "Intel i5", 128, 4, "macOS Lion", 2012, 600)
    bought2 = shop.buy("2022 MacBook Pro", "M2", 256, 6, "Sequoia 15.0", 2022, 1000)

    # current inventory after purchase
    print("\n Inventory - Purchased 2 computers:")
    shop.print_inventory()

    # update price
    shop.update_price(bought2, 1100)

    # current inventory
    print("\nInventory - price updating:")
    shop.print_inventory()

    # refurbish old computer's OS
    shop.refurbish(bought1, new_OS = "Catalina")

    # current inventory
    print("\nInventory - refurbishing:")
    shop.print_inventory()

    # sell the 2022 mac
    shop.sell(bought2)

    # current inventory
    print("\nInventory - selling a computer:")
    shop.print_inventory()

    # try error messages
    print("\n-------------")
    print("Check errors")
    print("-------------")
    shop.update_price(5, 100)
    shop.sell(5)
    shop.refurbish(5)


if __name__ == "__main__":
    main()