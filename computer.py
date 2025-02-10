class Computer:

    # What attributes will it need?
   
    description: str
    processor_type: str
    hard_drivec_capacity: int
    memory: int
    operating_system: str
    year_made: int
    price: int
                                                                                                                                                                                                                                                                                                                                                   
    # How will you set up your constructor?
        # Remember: in python, all constructors have the same name (__init__)
    
    def __init__(self, description:str, processor_type:str, hard_drive_capacity:int, memory:int, operating_system:str, year_made:int, price:int):
        self.description = description
        self.processor_type = processor_type
        self.hard_drive_capacity = hard_drive_capacity
        self.memory = memory
        self.operating_system = operating_system
        self.year_made = year_made
        self.price = price
    
    # What methods will you need?
    def print_comp(self):
        return {'description': self.description,
                'processor_type': self.processor_type,
                'hard_drive_capacity': self.hard_drive_capacity,
                'memory': self.memory,
                'operating_system': self.operating_system,
                'year_made': self.year_made,
                'price': self.price
        }
    
    def update_os(self, newOS:str) :
        self.operating_system = newOS
        print("\nNew System is: ",  self.operating_system)
    
def main():
    myComp = Computer(
        "Mac Pro (Late 2013)",
        "3.5 GHc 6-Core Intel Xeon E5",
        1024, 64,
        "macOS Big Sur", 2013, 1500
    )
    print("\nHere is my computer: \n", myComp.print_comp())
    myComp.update_os("Seqouia")
    print("\nHere is my new computer: \n", myComp.print_comp())

if __name__ == "__main__":
    main()