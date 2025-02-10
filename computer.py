# create a computer class with computer characteristics 

class Computer:

    # attributes that class Computer uses
   
    description: str
    processor_type: str
    hard_drivec_capacity: int
    memory: int
    operating_system: str
    year_made: int
    price: int
                                                                                                                                                                                                                                                                                                                                                   
    # constructor for class Computer that initialize attributes
    
    def __init__(self, description:str, processor_type:str, hard_drive_capacity:int, memory:int, operating_system:str, year_made:int, price:int):
        self.description = description
        self.processor_type = processor_type
        self.hard_drive_capacity = hard_drive_capacity
        self.memory = memory
        self.operating_system = operating_system
        self.year_made = year_made
        self.price = price
    
    # methods for class Computer

    # print computer descriptions in readable format
    def print_comp(self):
        return {'description': self.description,
                'processor_type': self.processor_type,
                'hard_drive_capacity': self.hard_drive_capacity,
                'memory': self.memory,
                'operating_system': self.operating_system,
                'year_made': self.year_made,
                'price': self.price
        }
    
    # update the operating system of the computer
    def update_os(self, newOS:str) :
        self.operating_system = newOS
        print("\nNew System is: ",  self.operating_system)

# use class Computer
   
def main():

    # store information about a specific computer
    myComp = Computer(
        "Mac Pro (Late 2013)",
        "3.5 GHc 6-Core Intel Xeon E5",
        1024, 64,
        "macOS Big Sur", 2013, 1500
    )

    # print a little banner
    print("-" * 21)
    print("COMPUTER SHOW-OFF")
    print("-" * 21)

    # current computer
    print("\nHere is my computer: \n", myComp.print_comp())

    # update operating system of the computer
    myComp.update_os("Seqouia")
    print("\nHere is my new computer: \n", myComp.print_comp())

if __name__ == "__main__":
    main()